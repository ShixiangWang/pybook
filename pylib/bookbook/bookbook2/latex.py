"""
Convert a collection of notebooks to a single PDF, via Latex.

- Combines notebooks into one document
- Inserts Latex labels for each document
- Converts links between notebooks to Latex \\ref{}
- Runs pdflatex to make a PDF (actually, nbconvert does this)

Requirements:
- nbconvert pandocfilters  (pip installable)
- pandoc
- pdflatex
"""
import argparse
import logging
import os
from pathlib import Path
from tempfile import mkdtemp
from typing import Sequence

import nbformat
from nbformat import NotebookNode
from nbformat.v4 import new_notebook, new_markdown_cell
from nbconvert.exporters import PDFExporter, LatexExporter
from nbconvert.writers import FilesWriter
from nbconvert.utils.pandoc import pandoc
from .filter_links import convert_links
from .custom_latex import CustomLatexExporter

log = logging.getLogger(__name__)


def new_latex_cell(source=''):
    return NotebookNode(
        cell_type='raw',
        metadata=NotebookNode(raw_mimetype='text/latex'),
        source=source,
    )


class NoHeader(Exception):
    pass


def add_sec_label(cell: NotebookNode, nbname) -> Sequence[NotebookNode]:
    """Adds a Latex \\label{} under the chapter heading.

    This takes the first cell of a notebook, and expects it to be a Markdown
    cell starting with a level 1 heading. It inserts a label with the notebook
    name just underneath this heading.
    """
    assert cell.cell_type == 'markdown', cell.cell_type
    lines = cell.source.splitlines()
    if lines[0].startswith('# '):
        header_lines = 1
    elif len(lines) > 1 and lines[1].startswith('==='):
        header_lines = 2
    else:
        raise NoHeader

    header = '\n'.join(lines[:header_lines])
    intro_remainder = '\n'.join(lines[header_lines:]).strip()
    res = [
        new_markdown_cell(header),
        new_latex_cell('\label{sec:%s}' % nbname)
    ]
    res[0].metadata = cell.metadata
    if intro_remainder:
        res.append(new_markdown_cell(intro_remainder))
    return res


def combine_notebooks(notebook_files: Sequence[Path]) -> NotebookNode:
    combined_nb = new_notebook()

    count = 0
    for filename in notebook_files:
        count += 1
        log.debug('Adding notebook: %s', filename)
        nbname = filename.stem
        nb = nbformat.read(str(filename), as_version=4)

        try:
            combined_nb.cells.extend(add_sec_label(nb.cells[0], nbname))
        except NoHeader:
            raise NoHeader("Failed to find header in {}".format(filename))

        combined_nb.cells.extend(nb.cells[1:])

        if not combined_nb.metadata:
            combined_nb.metadata = nb.metadata.copy()

    log.info('Combined %d files' % count)
    return combined_nb


mydir = os.path.dirname(os.path.abspath(__file__))
filter_links = os.path.join(mydir, 'filter_links.py')

listings = Path('listings.tex')
if not listings.is_file():
    with open('listings.tex', w) as f:
        f.write("% listings style")


def pandoc_convert_links(source):
    return pandoc(source, 'markdown', 'latex',
                  extra_args=['--filter', filter_links,
                              '--listings -H', listings,
                              ]
                  )

class MyLatexExporter(CustomLatexExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ('resolve_references', convert_links)


class MyLatexPDFExporter(PDFExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ('resolve_references', convert_links)


def add_preamble(extra_preamble_file, exporter):
    if extra_preamble_file is None:
        return

    with extra_preamble_file.open() as f:
        extra_preamble = f.read()

    td = mkdtemp()
    print(td)
    template_path = Path(td, 'with_extra_preamble.tplx')
    with template_path.open('w') as f:
        f.write("((* extends 'article.tplx' *))\n"
                '((* block header *))\n'
                '((( super() )))\n'
                )
        f.write(extra_preamble)
        f.write('((* endblock header *))\n'
                )

    # Not using append because we need an assignment to trigger traitlet change
    exporter.template_path = exporter.template_path + [td]
    exporter.template_file = 'with_extra_preamble'


def export(combined_nb: NotebookNode, output_file: Path, pdf=False,
           template_file=None):
    resources = {}
    resources['unique_key'] = 'combined'
    resources['output_files_dir'] = 'combined_files'

    log.info('Converting to %s', 'pdf' if pdf else 'latex')
    exporter = MyLatexPDFExporter() if pdf else MyLatexExporter()
    if template_file is not None:
        exporter.template_file = str(template_file)
    writer = FilesWriter(build_directory=str(output_file.parent))
    output, resources = exporter.from_notebook_node(combined_nb, resources)
    writer.write(output, resources, notebook_name=output_file.stem)


def combine_and_convert(source_dir: Path, output_file: Path, pdf=False, template_file=None):
    notebook_files = sorted(source_dir.glob('*-*.ipynb'))
    combined_nb = combine_notebooks(notebook_files)
    export(combined_nb, output_file, pdf=pdf, template_file=template_file)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Convert a set of notebooks to PDF via Latex')
    ap.add_argument('source_dir', nargs='?', type=Path, default='.',
                    help='Directory containing the .ipynb files')
    ap.add_argument('--output-file', type=Path, default='combined',
                    help='Base name of the output file.')
    ap.add_argument('--pdf', action='store_true',
                    help='Run Latex to convert to PDF.')
    ap.add_argument('--template', type=Path,
                    help='Latex template file to use for nbconvert.')
    args = ap.parse_args(argv)

    logging.basicConfig(level=logging.INFO)
    combine_and_convert(args.source_dir, args.output_file, args.pdf, args.template)


if __name__ == '__main__':
    main()
