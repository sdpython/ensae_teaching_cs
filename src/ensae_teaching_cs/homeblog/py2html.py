"""
@file
@brief Mark-up Python code file using HTML for syntax highlighting.
Syntax highlighting rules are in the spirit of IDLE.

Unless the -r 0 option is used it will also format the code by
applying some of the PEP8 spacing guidelines to expressions and
assignments.

For those that want a GUI you can try py2htmTk.pyw -
(it's minimal but functional).

::
    USAGE in command line mode:
        py2html [options] [-i filename]|-I]

    OPTIONS:
        -h          Print this command line summary
        --help      Print more detailed help on styles and
                    revision info.
        -o filename Output file (default is "py2html.html")
        -i filename Source file. See -I.
        -p filename HTML page template (must include a %s for inserting
                    the code). If not specified then a default is used.
        -s filename Use a style-file otherwise use built in styles
                    (see --help for details)
        -r 0|1|2    Reformat expressions and definitions.
                    -r 0  No formatting
                    -r 1  Format as  a = 3+4; b = [1, 2, 3]  (default)
                    -r 2  Format as  a = 3 + 4; b = [1 , 2 , 3]
        -R          Replace newlines with <br>, tabs and multi-spaces
                    with &nbsp;
        -B          Just make a block (ignores -p)
        -O          Print to sys.stdout (ignores -o, no file created)
        -I          Use stdin as source file (ignore -i option)
        -E 0|1|2|3|4    0 - Don't do entity substitution.
                        1 - Substitute < > and & (default)
                        2 - Substitute < > & and "
                        3 - Substitute <> & " and '
                        4 - Substitute all non-ASCIIalphanumeric
"""


import tokenize
import os

appliedstyle = None

help_styles = """
The default styles applied are as follows:
    <style type="text/css">
        h1 {    color: green;
                position: center;
            }
        .python_code {  font-family: monospace;
                    font-size: 10pt;
                    }
        .py_key {}
        .py_num {}
        .py_str { color: #00AA00;}
        .py_op {}
        .py_com { color: red;}
        .py_res { color: #FF7700;}
        .py_def { color: blue;}
    </style>

Where:
    .python_code  is the style applied to the whole block
    .py_key    is used for words that are not reserved words
    .py_num    for numeric values
    .py_str    for strings
    .py_op     for operators
    .py_res    for reserved words
    .py_com    for comments
    .py_def    used for words that are names in function and class definitions.

Optionally you can define a style-file, a text file with the following format:

    #User editable style substitutions
    # This style-file assumes a css is used.
    # Format:
    # styleName | start | end
    # examples:
    # block | <pre> | </pre>
    # key | <span class="key">'| </span>
    # str | <span style = "color: #00AA00"> | </span>

    block | <pre class="python_code" id="pycode"> | </pre>
    key | <span class="py_key"> | </span>
    num | <span class="py_num"> | </span>
    str | <span class="py_str"> | </span>
    op  | <span class="py_op">  | </span>
    com | <span class="py_com"> | </span>
    res | <span class="py_res"> | </span>
    def | <span class="py_def"> | </span>
    brk | <span class="py_brk"> | </span>
    #End

This example does not use css:

    # User editable HTML style substitutions
    # This file uses font tags
    # Undefined tags will use the default character colour
    block | <pre> | </pre>
    key | |
    num |  |
    str | <font color="green"> | </font>
    op  |  |
    com | <font color="red"> | </font>
    res | <font color="orange"> | </font>
    def | <font color="blue"> | </font>
    brk |  |


Revisions:
0.51 First release.
0.6 7 Mar '04
    Fixed   -   now supports \\ character properly
    Changes -   The styles now use a py_ prefix
    Added   -   Extended and added to formatting options
            -   External style-file support
0.61 Added  -   support for disabling entity translator
0.62 Added  -   additional entity replacement options
"""

__author__ = "Paul Hardwick <paul@peck.org.uk>"
__date__ = "07 March 2004"
__version__ = "0.62"

entities = {  # 34: '&quot;', 38: '&amp;', 60: '&lt;', 62: '&gt;',
    # 160: '&nbsp;,
    161: '&iexcl;', 162: '&cent;', 163: '&pound;',
    164: '&curren;', 165: '&yen;', 166: '&brvbar;',
    167: '&sect;', 168: '&uml;', 169: '&copy;',
    170: '&ordf;', 171: '&laquo;', 172: '&not;',
    173: '&shy;', 174: '&reg;', 175: '&macr;',
    176: '&deg;', 177: '&plusmn;', 178: '&sup2;',
    179: '&sup3;', 180: '&acute;', 181: '&micro;',
    182: '&para;', 183: '&middot;', 184: '&cedil;',
    185: '&sup1;', 186: '&ordm;', 187: '&raquo;',
    188: '&frac14;', 189: '&frac12;', 190: '&frac34;',
    191: '&iquest;', 192: '&Agrave;', 193: '&Aacute;',
    194: '&Acirc;', 195: '&Atilde;', 196: '&Auml;',
    197: '&Aring;', 198: '&AElig;', 199: '&Ccedil;',
    200: '&Egrave;', 201: '&Eacute;', 202: '&Ecirc;',
    203: '&Euml;', 204: '&Igrave;', 205: '&Iacute;',
    206: '&Icirc;', 207: '&Iuml;', 208: '&ETH;',
    209: '&Ntilde;', 210: '&Ograve;', 211: '&Oacute;',
    212: '&Ocirc;', 213: '&Otilde;', 214: '&Ouml;',
    215: '&times;', 216: '&Oslash;', 217: '&Ugrave;',
    218: '&Uacute;', 219: '&Ucirc;', 220: '&Uuml;',
    221: '&Yacute;', 222: '&THORN;', 223: '&szlig;',
    224: '&agrave;', 225: '&aacute;', 226: '&acirc;',
    227: '&atilde;', 228: '&auml;', 229: '&aring;',
    230: '&aelig;', 231: '&ccedil;', 232: '&egrave;',
    233: '&eacute;', 234: '&ecirc;', 235: '&euml;',
    236: '&igrave;', 237: '&iacute;', 238: '&icirc;',
    239: '&iuml;', 240: '&eth;', 241: '&ntilde;',
    242: '&ograve;', 243: '&oacute;', 244: '&ocirc;',
    245: '&otilde;', 246: '&ouml;', 247: '&divide;',
    248: '&oslash;', 249: '&ugrave;', 250: '&uacute;',
    251: '&ucirc;', 252: '&uuml;', 253: '&yacute;',
    254: '&thorn;', 255: '&yuml;'}
BSLASH = chr(92)

WORD = 1
NUMBER = 2
STRING = 3
OPERATOR = 50
COMMENT = 52
RESERVED = "reserved"
DEFINING = "defining"
BRACKETS = "brackets"
BLOCK = "block"

skeys = {WORD: "key", NUMBER: "num", STRING: "str", COMMENT: "com",
         OPERATOR: "op", RESERVED: "res", DEFINING: "def", BRACKETS: "brk", BLOCK: "block"}

#######################################
# The styles wrapping each token using css
#######################################
py_style = {skeys[WORD]: ['<span class="py_key">', "</span>"],  # name
            skeys[NUMBER]: ['<span class="py_num">', "</span>"],  # number
            skeys[STRING]: ['<span class="py_str">', "</span>"],  # string
            skeys[OPERATOR]: ['<span class="py_op">', "</span>"],  # operator
            skeys[COMMENT]: ['<span class="py_com">', "</span>"],  # comment
            # reserved word
            skeys[RESERVED]: ['<span class="py_res">', "</span>"],
            # class and def names
            skeys[DEFINING]: ['<span class="py_def">', "</span>"],
            # all enclosing ops
            skeys[BRACKETS]: ['<span class="py_brk">', "</span>"],
            # wraps the block
            skeys[BLOCK]: ['<pre class="python_code" id="pycode">', "</pre>"]
            }

######################################
# The default web page
######################################

py_page = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
<title>%s</title>
<style type="text/css">
    h1 {    color: green;
            position: center;
        }
    .python_code {  font-family: monospace;
                font-size: 10pt;
                }
    .py_key {color: black;}
    .py_num color: black;{}
    .py_str { color: #00AA00;}
    .py_op {color: black; }
    .py_com { color: red;}
    .py_res { color: #FF7700;}
    .py_def { color: blue;}
    .py_brk { color: black;}
</style>
</head>
<body>
<h1>#### Source code for %s ####</h1>
<hr>
%s
<hr>
[Created with py2html Ver:%s]
<p>
      <a href="http://validator.w3.org/check/referer"><img border="0"
          src="http://www.w3.org/Icons/valid-html401"
          alt="Valid HTML 4.01!" height="31" width="88"></a>
</p></body>
</html>"""
######################################

# Some variables used for tracking states
command = False
prev = 0
prevres = False
prevtok = "#"  # previous token
defining = False  # check if previous toke was def or class
# Are we somewhere between def/class and : (for default assignment formating)


definingmode = False

# Operator formating


spaced_tokens = ["=", "==", ">", "<", ">=",
                 "<=", "+=", "-=", "<>", "!=", "&&", "||"]
monospaced_tokens = [":", ";", ","]
binops = ["+", "-", "*", "/", "//", "**", "%", "<<", ">>", "&", "^", "|"]
brackets = ["[", "]", "{", "}", "(", ")"]
spaced_fmt2 = spaced_tokens + binops

# reserved words
reserved = kwlist = [
    # --start keywords--
    'and', 'assert', 'break',
    'class', 'continue', 'def',
    'del', 'elif', 'else',
    'except', 'exec', 'finally',
    'for', 'from', 'global',
    'if', 'import', 'in',
    'is', 'lambda', 'not',
    'or', 'pass', 'print',
    'raise', 'return', 'try',
    'while', 'yield',
    # others languages
    "void", "double", "int", "throw", "template", "catch",
    "public", "protected", "float", "unsigned", "__int32", "short",
    # --end keywords--
]


def substituteEntities(token, level="1", char_set=None):
    """
    based on level setting do entity substitution
    and return revised. iso8859-1 ??:
        - "0" : Don't do entity substitution.
        - "1" : Substitute ``< > and & (default)``
        - "2" : Substitute ``< > & and "``
        - "3" : Substitute ``<> & " and '``
        - "4" : Substitute all non-ASCIIalphanumeric char_set not implemented yet
    """
    if level == "0":
        return token
    elif level in "1234":
        token = token.replace('&', "&amp;")
        token = token.replace('<', "&lt;")
        token = token.replace('>', "&gt;")
        if level in "234":
            token = token.replace('"', "&quot;")
        if level in "34":
            token = token.replace("'", "&#039;")

    if level == "4":
        dl = list(token)
        for index, char in enumerate(dl):
            value = ord(char)
            if value > 127:
                dl[index] = entities.get(value, "&#%3d;" % (value,))
        token = ''.join(dl)
    return token


def apply_style(index, token, start, src, format, style, entity="1"):
    """Supplied with an index this function applies
    the style using the format rules and returns a formatted
    verison of the token.
    'start' and 'src' are (not used yet) for appliance of
    intelligent line breaks for long lines
    entity is the replace entities flag"""
    global prev, prevres, defining, definingmode, prevtok
    # keyword handling
    isres = False
    if index == WORD:
        if token not in reserved:
            if defining:
                fmt = style[skeys[DEFINING]]
            else:
                fmt = style.get(skeys.get(index, 99), ['', ''])
            defining = False
        else:
            fmt = style[skeys[RESERVED]]
            isres = True
            if token in ['def', 'class']:
                defining = True
                definingmode = True
    elif index == OPERATOR and token in brackets:
        fmt = style[skeys[BRACKETS]]
    else:
        fmt = style.get(skeys.get(index, 99), ['', ''])

    if (token == ":") and definingmode:
        definingmode = False
    token = substituteEntities(token, entity, char_set=None)
    if format != "0":
        if format == "1":
            if token in spaced_tokens and not definingmode:
                token = " %s " % (token,)
            elif token in monospaced_tokens:
                token = "%s " % (token,)
            elif (isres or index == COMMENT) and prev in [WORD, NUMBER, STRING, OPERATOR]:
                token = " " + token
            elif index in [WORD, NUMBER, STRING] and prev == WORD:
                token = " " + token
            elif token in ["[", "("] and prevres:
                token = " " + token
        elif format == "2":
            if token in spaced_fmt2:
                if (prev == OPERATOR and token in "+-~"):
                    token = " %s" % (token,)
                else:
                    token = " %s " % (token,)
            elif token in monospaced_tokens:
                token = "%s " % (token,)
            elif isres and prev in [WORD, NUMBER, STRING, OPERATOR]:
                token = " " + token
            elif index in [WORD, NUMBER, STRING] and prev == WORD:
                token = " " + token
            elif token in ["[", "("] and prevres:
                token = " " + token

    text = fmt[0] + token + fmt[1]
    prev = index
    prevres = isres
    prevtok = token
    return text


def readStyleFile(filename):
    """Read a style file and return a style dictionary.
    The file format is::

        #User editable style substitutions
        # This style-file assumes a css is used.
        # Format:
        # styleName | start | end
        # examples:
        # block | <pre> | </pre>
        # key | <span class="key">'| </span>
        # str | <span style = "color: #00AA00"> | </span>

        block | <pre class="python_code" id="pycode"> | </pre>
        key | <span class="py_key"> | </span>
        num | <span class="py_num"> | </span>
        str | <span class="py_str"> | </span>
        op  | <span class="py_op">  | </span>
        com | <span class="py_com"> | </span>
        res | <span class="py_res"> | </span>
        def | <span class="py_def"> | </span>
        brk | <span class="py_brk"> | </span>
    """
    global appliedstyle
    if not filename:
        appliedstyle = py_style
        return py_style
    else:
        try:
            with open(filename, 'r') as ff:
                lines = ff.readlines()
            appliedstyle = {}
            for line in lines:
                line = line.strip()
                if line and line[0] != '#':
                    parts = line.split('|')
                    if len(parts) == 3 and len(parts[0].strip()):
                        appliedstyle[parts[0].strip()] = [
                            parts[1].strip(), parts[2].strip()]
                    else:
                        print("Error in style file:\n", line)
                        sys.exit(1)
            return appliedstyle
        except Exception:
            appliedstyle = py_style
            return py_style


def replaceCodes(text=""):
    """
    Helper function that does the ``\\n`` and space substition
    returning the changed text.
    """
    text = text.replace('\n', '<br>')
    text = text.replace('\t', ' ' * 4)
    text = text.replace(" " * 4, "&nbsp; &nbsp; ")
    text = text.replace(" " * 3, "&nbsp; &nbsp;")
    text = text.replace(" " * 2, "&nbsp; ")
    text = text.replace("<br><br>", "<br> <br>")
    return text


def file2HTML(file_name, format, style, Replace, entity="1", encoding="utf-8"):
    """
    Reads a file and returns the contents as a string,
    highlighted with :epkg:`HTML` styles. This function uses the
    output of the tokenize module to decide what to colour.
    It calls @see fn apply_style with the token index.

    - If format == '0' then the code will display as the author expected it to.
    - If format == '1' then spaces are added and removed around expressions to standardise the format.
    - If format == '2' as '1' but different rules
    - If style == style dictionary. Replace (boolean)
    - If True then replace ``\\n`` with ``<br>``, multiple spaces with ``&nbsp<space>combinations;``
    """
    removeFile = None
    if file_name == "<stdin>":
        file_name = "temp_stdin.py2html.tmp"
        lines = sys.stdin.readlines()
        with open(file_name, "w", encoding=encoding) as f:
            f.writelines(lines)
        removeFile = file_name
    elif len(file_name) < 1000 and os.path.exists(file_name):
        try:
            # , encoding="utf8").readlines() #copy all lines into lines list
            with open(file_name, 'r', encoding=encoding) as f:
                lines = f.readlines()
        except UnicodeDecodeError as e:
            print("issue with file ", file_name)
            raise e
    else:
        lines = file_name.split("\n")
        file_name = "temp_py2html.tmp"
        with open(file_name, "w", encoding=encoding) as f:
            f.writelines("\n".join(lines))
        removeFile = file_name

    lines = ['', ] + lines
    tempPointer = open(file_name, 'r', encoding=encoding)
    read_line = tempPointer.readline  # , encoding="utf8").readline
    # use tokenize to interate through tokens
    tok = tokenize.generate_tokens(read_line)

    page = []
    old_line = 1
    old_column = 0
    try:
        for tupe in tok:
            # first collect packing beween previous token and this one
            if old_line == tupe[2][0]:  # Another token on same line as last token
                if tupe[2][1] and (old_column < tupe[2][1]):
                    # handle when no reformat and when it is the first line
                    # processed
                    if (format == "0") or (prev == 0):
                        txt = lines[old_line][old_column:tupe[2][1]]
                        txt = txt.replace(BSLASH, BSLASH + '\n')
                        page.append(txt)
            else:
                # collect remains of old line
                subpage = lines[old_line][old_column:-1]
                subpage = subpage.replace(BSLASH, BSLASH + '\n')
                page.append(subpage)
                old_line += 1
                # now collect all the lines between last and current
                while old_line != tupe[2][0]:
                    txt = lines[old_line].replace(BSLASH, BSLASH + '\n')
                    page.append(txt)
                    old_line += 1
                # now get begining of line upto current column
                txt = lines[old_line][0:tupe[2][1]].replace(
                    BSLASH, BSLASH + '\n')
                page.append(txt)
            # now add formatted token
            page.append(apply_style(tupe[0], tupe[1], tupe[
                        2], tupe[4], format, style, entity))

            # now update pointers
            old_line = tupe[3][0]
            old_column = tupe[3][1]
    except tokenize.TokenError:
        return "File cannot be tokenized by tokenize"
    except IndexError:
        pass
    text = ''.join(page)
    if Replace:
        text = replaceCodes(text)
    tempPointer.close()

    if removeFile is not None and os.path.exists(removeFile):
        os.remove(removeFile)

    return text


def makeBlock(data):
    """Applies the block tags to text
    """
    global appliedstyle
    return "%s%s%s" % (appliedstyle['block'][0], data, appliedstyle['block'][1])


def cmdLine():
    '''This is the function that handles
    command line mode'''
    global appliedstyle
    help_ = ' PY2HTML - convert python code to HTML (version %s)\n\n%s' % (
        __version__, __doc__)

    try:
        opts, _ = getopt.getopt(sys.argv[1:], "ho:i:p:s:r:RBOIE:",
                                ["help", "output", "page", "input", "style", "reformat",
                                    "Replace", "Block", "STDOUT", "STDIN", "entities"])
    except getopt.GetoptError:
        # print help information and exit:
        print(help_)
        sys.exit(2)
    outfile = "py2html.html"
    page = None
    infile = ""
    reformat = "1"
    justdiv = False
    stylefile = None
    emit = False
    Replace = False
    stdin = False
    entity = "1"
    for o, a in opts:
        if o == "-h":
            print(help_)
            sys.exit()
        elif o == "--help":
            print(help_styles)
            sys.exit()
        elif o in ("-o", "--output"):
            outfile = a
        elif o in ("-i", "--input"):
            infile = a
        elif o in ("-p", "--page"):
            page = a
        elif o in ("-s", "--style"):
            stylefile = a
        elif o in ("-r", "--reformat") and a in "012":
            reformat = str(a)
        elif o in ("-B", "--Block"):
            justdiv = True
        elif o in ("-O", "--STDOUT"):
            emit = True
        elif o in ("-R", "--Replace"):
            Replace = True
        elif o in ("-I", "--STDIN"):
            stdin = True
        elif o in ("-E", "--entities") and a in "01234":
            entity = str(a)
        else:
            print(help_)
            sys.exit(1)

    if infile == "" and not stdin:
        print(help_)
        sys.exit()
    elif stdin:
        infile = "<stdin>"

    appliedstyle = readStyleFile(stylefile)
    data = file2HTML(infile, reformat, appliedstyle, Replace, entity)
    block = makeBlock(data)
    if infile == "<stdin>":
        infile = "stdin"
    if justdiv:
        html = block
    elif page:
        html = open(page, "r").read()  # , encoding="utf8").read()
        html = html % (block,)
    else:
        html = py_page % (infile, infile, block, __version__)
    if not emit:
        f = open(outfile, "w")  # , encoding="utf8")
        f.write(html)
        f.close()
    else:
        print(html)


if __name__ == "__main__":
    import getopt
    import sys
    cmdLine()
