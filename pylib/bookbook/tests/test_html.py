from pathlib import Path
from tempfile import TemporaryDirectory
from testpath import assert_isfile

from bookbook import html

sample_dir = Path(__file__).parent / 'sample'

def test_sampledir():
    with TemporaryDirectory() as td:
        td = Path(td)
        html.convert_directory(sample_dir, td)

        assert_isfile(td / '01-introduction.html')

def test_convert_link():
    sample = "[link](01-abc.ipynb)"
    res = html.markdown2html_custom(sample)
    assert '01-abc.html' in res
    assert '.ipynb' not in res

    sample = "[link](02-def.ipynb#foo)"
    res = html.markdown2html_custom(sample)
    assert '02-def.html#foo' in res
    assert '.ipynb' not in res

    # Links to external sites shouldn't be converted
    sample = "[link](http://example.com/01-abc.ipynb)"
    assert '01-abc.ipynb' in html.markdown2html_custom(sample)
