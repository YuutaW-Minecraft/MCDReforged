"""
This type stub file was generated by pyright.
"""

LIST_MD_SYMBOLS = "*_`["
MD_SYMBOLS = ((LIST_MD_SYMBOLS[0], LIST_MD_SYMBOLS[0]), (LIST_MD_SYMBOLS[1], LIST_MD_SYMBOLS[1]), (LIST_MD_SYMBOLS[2], LIST_MD_SYMBOLS[2]), (LIST_MD_SYMBOLS[2] * 3 + "\n", "\n" + LIST_MD_SYMBOLS[2] * 3), ("<b>", "</b>"), ("<i>", "</i>"), ("<code>", "</code>"), ("<pre>", "</pre>"))
HTML_QUOTES_MAP = { "<": "&lt;",">": "&gt;","&": "&amp;",'"': "&quot;" }
_HQS = HTML_QUOTES_MAP.keys()
def quote_html(*content, sep=...) -> str:
    """
    Quote HTML symbols

    All <, >, & and " symbols that are not a part of a tag or
    an HTML entity must be replaced with the corresponding HTML entities
    (< with &lt; > with &gt; & with &amp and " with &quot).

    :param content:
    :param sep:
    :return:
    """
    ...

def escape_md(*content, sep=...) -> str:
    """
    Escape markdown text

    E.g. for usernames

    :param content:
    :param sep:
    :return:
    """
    ...

def text(*content, sep=...):
    """
    Join all elements with a separator

    :param content:
    :param sep:
    :return:
    """
    ...

def bold(*content, sep=...) -> str:
    """
    Make bold text (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hbold(*content, sep=...) -> str:
    """
    Make bold text (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def italic(*content, sep=...) -> str:
    """
    Make italic text (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hitalic(*content, sep=...) -> str:
    """
    Make italic text (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def code(*content, sep=...) -> str:
    """
    Make mono-width text (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hcode(*content, sep=...) -> str:
    """
    Make mono-width text (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def pre(*content, sep=...) -> str:
    """
    Make mono-width text block (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hpre(*content, sep=...) -> str:
    """
    Make mono-width text block (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def underline(*content, sep=...) -> str:
    """
    Make underlined text (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hunderline(*content, sep=...) -> str:
    """
    Make underlined text (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def strikethrough(*content, sep=...) -> str:
    """
    Make strikethrough text (Markdown)

    :param content:
    :param sep:
    :return:
    """
    ...

def hstrikethrough(*content, sep=...) -> str:
    """
    Make strikethrough text (HTML)

    :param content:
    :param sep:
    :return:
    """
    ...

def link(title: str, url: str) -> str:
    """
    Format URL (Markdown)

    :param title:
    :param url:
    :return:
    """
    ...

def hlink(title: str, url: str) -> str:
    """
    Format URL (HTML)

    :param title:
    :param url:
    :return:
    """
    ...

def hide_link(url: str) -> str:
    """
    Hide URL (HTML only)
    Can be used for adding an image to a text message

    :param url:
    :return:
    """
    ...

