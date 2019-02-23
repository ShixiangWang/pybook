"""Converts a collection of notebooks to HTML files."""
import argparse
import logging
from pathlib import Path
import re

import nbformat
from nbconvert.exporters import HTMLExporter
from nbconvert.writers import FilesWriter
from nbconvert.filters.markdown_mistune import MarkdownWithMath, IPythonRenderer
from jinja2 import Environment, FileSystemLoader

_PKGDIR = Path(__file__).parent
log = logging.getLogger(__name__)


class MyMarkdownRenderer(IPythonRenderer):
    def link(self, link, title, text):
        m = re.match(r'(\d+\-.+)\.ipynb(#.+)?$', link)
        if m:
            link = m.expand(r'\1.html\2')
        return super().link(link, title, text)


def markdown2html_custom(source):
    """Convert a markdown string to HTML using mistune"""
    return MarkdownWithMath(renderer=MyMarkdownRenderer(escape=False)).render(source)


class MyHTMLExporter(HTMLExporter):
    def default_filters(self):
        yield from super().default_filters()
        yield ('markdown2html', markdown2html_custom)


class IndexEntry:
    def __init__(self, chapter_no, title, filename):
        self.chapter_no = chapter_no
        self.title = title
        self.filename = filename

    @classmethod
    def from_notebook_file(cls, path: Path):
        chapter_no = int(re.match('(\d+)\-', path.stem).group(1))
        nb = nbformat.read(str(path), as_version=4)

        assert nb.cells[0].cell_type == 'markdown', nb.cells[0].cell_type
        lines = nb.cells[0].source.splitlines()
        if lines[0].startswith('# '):
            header = lines[0][2:]
        elif len(lines) > 1 and lines[1].startswith('==='):
            header = lines[0]
        else:
            assert False, "No heading found in %s" % str(path)

        assert path.suffix == '.ipynb', path
        html_filename = path.stem + '.html'
        return cls(chapter_no, header, html_filename)


def convert(source_path: Path, output_dir: Path):
    exporter = MyHTMLExporter()
    writer = FilesWriter(build_directory=str(output_dir))
    output, resources = exporter.from_filename(str(source_path))
    notebook_name = source_path.stem
    writer.write(output, resources, notebook_name=notebook_name)


def write_index(index_entries, output_dir):
    env = Environment(loader=FileSystemLoader(str(_PKGDIR)))
    template = env.get_template('html_index.tpl')

    index_entries.sort(key=lambda e: e.chapter_no)
    log.info('Writing table of contents')
    with (output_dir / 'index.html').open('w') as f:
        f.write(template.render(index_entries=index_entries))


def convert_directory(source_dir: Path, output_dir: Path):
    index_entries = []
    for nbfile in source_dir.glob('*-*.ipynb'):
        convert(nbfile, output_dir)
        index_entries.append(IndexEntry.from_notebook_file(nbfile))

    output_dir.mkdir(exist_ok=True, parents=True)

    write_index(index_entries, output_dir)


def main(argv=None):
    ap = argparse.ArgumentParser(description='Convert a set of notebooks to HTML')
    ap.add_argument('source_dir', nargs='?', type=Path, default='.',
                    help='Directory containing the .ipynb files')
    ap.add_argument('--output-dir', type=Path, default='html',
                    help='Directory where output files will be written')
    args = ap.parse_args(argv)

    logging.basicConfig(level=logging.INFO)
    convert_directory(args.source_dir, args.output_dir)


if __name__ == '__main__':
    main()
