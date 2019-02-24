# bookbook2

[![lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)

**bookbook2** convert ipython notebooks to html or pdf chapters, initting from [bookbook](https://github.com/takluyver/bookbook) package,
preserving cross references within and between notebooks.

This code is in early development, so use it at your own risk.

Installation
------------

Bookbook requires Python 3.7.

Install from PyPI (<https://pypi.org/project/bookbook2/>) with pip:

```
pip install bookbook2
```

Install from Github with:

```
git clone https://github.com/ShixiangWang/bookbook2
cd bookbook2
pip install .
# or
pip install -r requirements.txt
```

Running bookbook
----------------
bookbook expects a directory of notebooks whose names indicate their order.  Specifically,
**the file names must have the form `x-y.ipynb`**, where typically `x` is a number
indicating the order and `y` is a chapter title; e.g.:
`01-introduction.ipynb`. 

To run `bookbook`:

    python3 -m bookbook2.html           # HTML output under html/
    python3 -m bookbook2.latex [--pdf]  # Latex/PDF output as combined.(tex|pdf)

Add `--help` to either command for more options.

Chapters and sections
---------------------
Each top-level header (`# xyz` in markdown) will be converted to a top-level
latex section (a chapter if using the book or report document class).  Lower-level
headers (`##`, `###`, etc.) are converted to subsections, subsubsections, etc.
A latex label will also be inserted for each.  **The first cell of each notebook
must start with a top-level header**.

Cross-references
----------------
Markdown references will be converted automatically to latex references.  For instance,
if the markdown contains the hyperlink `[02-foo](02-foo.ipynb)` and `02-foo.ipynb` is
a notebook in the same directory, the link will appear as `Chapter \ref{sec:02-foo}`.
The label `\label{sec:02-foo}` will be inserted at the start of that notebook,
so when the latex is compiled to PDF it will appear as `Chapter 2`.

References to sections within a notebook work similarly.  If a notebook contains 
(in markdown) the section heading `## bar` within the notebook starting with top-level
header `# foo`, then the markdown hyperlink `[foo](foo.ipynb#bar)` will be
converted to the latex reference `Section \ref{bar}` and when compiled to PDF it will
be rendered as something like `Section 2.1`.

Latex formatting
----------------
bookbook uses nbconvert under the hood.  Custom formatting of latex output
can be accomplished by using a template, in the same way as would be done
using nbconvert by itself.  See `the nbconvert
documentation <http://nbconvert.readthedocs.io/en/latest/customizing.html>` for
more details.


Examples of projects using bookbook
-----------------------------------
- `Book on Riemann solvers <http://github.com/clawpack/riemann_book>` (in development) by David Ketcheson, Mauricio del Razo, and Randall LeVeque.  This example uses a custom nbconvert template and shows how to store your notebooks with no output (for version control) while automatically executing them before running bookbook, so that PDF and HTML versions include the output.

Related tools
-------------
If you are writing a book in Jupyter notebooks, you may also find these to be useful:

- [nbopen](https://github.com/takluyver/nbopen): open notebooks from the command line without launching a new notebook server.  We find it useful to launch a single server in your home directory; then nbopen will use that to open each notebook.
- [nbdime](https://github.com/jupyter/nbdime): diff/merge for notebooks; includes terminal or graphical output.
- [nbstripout](https://github.com/kynan/nbstripout): remove output from notebooks before committing them.


*** 

<h3 align="center">License</h3>

<h5 align="center">MIT &copy; Shixiang Wang, Thomas Kluyver</h5>