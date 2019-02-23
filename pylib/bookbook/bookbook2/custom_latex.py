"""
See here: https://github.com/jupyter/nbconvert/issues/323
"""

from nbconvert.exporters.latex import LatexExporter

def nice_breaks(line, size):
    """
    Allows breaking long lines. Adds ellipsis to words
    that have to be cut short
    """
    words = line.split(" ")
    current_string = ""
    for word in words:
        if len(word) > size:
            # word to long, can't do anything
            if len(current_string):
                yield current_string[:size] + " ..."
            yield word[:size] + " ..."
            continue
        if len(word) + len(current_string) + 1 <= size:
            current_string = current_string + " " + word
        else:
            yield current_string
            current_string = word
    yield current_string


def break_lines(text):
    """
    Break lines function wrapper. See nice_breaks for the
    action
    """
    width = 65
    lines = []

    for line in text.split("\n"):
        if len(line) > width:
            lines.extend(list(nice_breaks(line, width)))
        else:
            lines.append(line)
    return "\n".join(lines)

def make_sidenotes(text):
    """
    Picks sidenotes wrapped by `!sidenote` `!endsidenote` inside
    text
    """

    if text.find("!sidenote") > -1:
        start = text.find("!sidenote")
        end = text.find("!endsidenote")
        note = text[start:end].strip("!sidenote")
        sidenote = r"\marginnote{"+ note.strip() +"}"
        text = text[:start] + sidenote + text[end:].strip("!sidenote")

    return text


class CustomLatexExporter(LatexExporter):
    """
    Custom style for making a LaTeX file compatible with the Tufte
    Book Style Class
    """
    def from_notebook_node(self, nb, resources=None, **kw):
        self.register_filter('break_lines', break_lines)
        self.register_filter('make_sidenotes', make_sidenotes)
        return super(CustomLatexExporter, self).from_notebook_node(nb, resources, **kw)
