from pathlib import Path
from tempfile import TemporaryDirectory
from testpath import assert_isfile

from nbformat.v4 import new_markdown_cell

from bookbook import latex

sample_dir = Path(__file__).parent / 'sample'


def test_sampledir():
    with TemporaryDirectory() as td:
        td = Path(td)
        latex.combine_and_convert(sample_dir, td / 'combined.pdf', pdf=True)

        assert_isfile(td / 'combined.pdf')


def test_convert_link():
    sample = "[link](01-abc.ipynb)"
    res = latex.pandoc_convert_links(sample)
    assert '\\ref{sec:01-abc}' in res
    assert '.ipynb' not in res

    sample = "[link](02-def.ipynb#Foo-bar)"
    res = latex.pandoc_convert_links(sample)
    assert '\\ref{foo-bar}' in res
    assert '.ipynb' not in res

    # Links to external sites shouldn't be converted
    sample = "[link](http://example.com/01-abc.ipynb)"
    assert '01-abc.ipynb' in latex.pandoc_convert_links(sample)


def test_exporter_converts_links():
    out, res = latex.MyLatexExporter().from_filename(
                    str(sample_dir / '01-introduction.ipynb'))
    assert 'Chapter \\ref{sec:02-in-which-we}' in out
    assert 'Section \\ref{just-a-subheading}' in out


def test_add_sec_label():
    sample = ("# Foo\n"
              "\n"
              "Bar")
    res = latex.add_sec_label(new_markdown_cell(sample), '05-test')
    assert len(res) == 3
    assert res[0].cell_type == 'markdown'
    assert res[0].source.strip() == '# Foo'
    assert res[1].cell_type == 'raw'
    assert res[1].source.strip() == '\\label{sec:05-test}'
    assert res[2].cell_type == 'markdown'

    sample = ("Foo\n"
              "===\n")
    res = latex.add_sec_label(new_markdown_cell(sample), '05-test')
    assert len(res) == 2
    assert res[0].cell_type == 'markdown'
    assert res[0].source.strip() == 'Foo\n==='
    assert res[1].cell_type == 'raw'
    assert res[1].source.strip() == '\\label{sec:05-test}'
