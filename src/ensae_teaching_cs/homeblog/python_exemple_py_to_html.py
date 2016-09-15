#-*- coding: utf-8 -*-
"""
@file
@brief Helper for HTML
"""

import os
import os.path
from pyquickhelper.loghelper import fLOG
from .clean_python_script_before_exporting_outside import cleanFileFromtohtmlreplace
from .py2html import file2HTML, makeBlock, readStyleFile
from .py2html import __version__ as py2html__version__


py_page = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1 (Latin-1)" >
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
<h1>Programme %s</h1>
<hr>
%s
<hr>
created avec py2html version:%s
<p>
</p>
__GOOGLETRACKER__
</body>
</html>"""

googleTrackerMarker = "__GOOGLETRACKER__"
### tohtmlreplace BEGIN ###
googleTrackerFooter = ""
### tohtmlreplace ELSE ###
googleTrackerFooter = """
<script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
<script type="text/javascript">_uacct = "UA-2815364-1";urchinTracker();</script>
"""
### tohtmlreplace END ###


def get_first_col(file):
    """
    function related to my teachings, it tries to associate a file
    to a chapter of my book

    @param      file        file name (python script)
    @return                 a chapter
    """
    f = open(file, "r")  # , encoding="utf8")
    sall = f.readlines()
    f.close()
    s = ""
    for l in sall:
        s += l
    if "thread" in s:
        return "Chapitre 10 : thread"
    elif "Tkinter" in s:
        return "Chapitre 9 : interface"
    elif "struct" in s:
        return "Chapitre 8 : fichiers"
    elif "glob" in s:
        return "Chapitre 8 : fichiers"
    elif "import Tix" in s:
        return "Chapitre 9 : interface"
    elif "selection" in file:
        return "Chapitre 9 : interface"
    elif "filelist" in file:
        return "Chapitre 9 : interface"
    elif "class" in file:
        return "Chapitre 5 : classes"
    elif "exemple" in file:
        return "Chapitre 7 : modules"
    elif "setup" in file:
        return "Chapitre 7 : modules"
    elif "PythonSample" in file:
        return "Chapitre 7 : modules"
    elif "init" in file:
        return "Chapitre 7 : modules"
    else:
        return "-"


def py_to_html_folder(folder, addGoogleTracking=True):
    """
    convert all python files from a folder into html files

    @param      folder              folder
    @param      addGoogleTracking   add some code for the Google tracking (related to www.xavierdupre.fr), @see fn py_to_html_file
    @return                         list of processed files
    """
    res = []
    l = os.listdir(folder)
    for f in l:
        fullf = folder + "/" + f
        racine, ext = os.path.splitext(fullf)
        if ext == ".py":
            r = py_to_html_file(fullf, addGoogleTracking=addGoogleTracking)
            res.append(r)
    return res


def py_to_html_file(file, writehtml="", addGoogleTracking=True, title=None):
    """
    convert a python script into a html file

    @param      folder              folder
    @param      addGoogleTracking   add some code for the Google tracking (related to www.xavierdupre.fr), it looks like:

                                    ::

                                        <script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
                                        <script type="text/javascript">_uacct = "UA-XXXXXXX-X";urchinTracker();</script>

    @return                         the processed file (same file but with extension .html)
    """
    googlet = googleTrackerFooter if addGoogleTracking else ""

    fLOG("converting pyfile in html ", file)
    f = file
    racine, ext = os.path.splitext(file)

    try:
        with open(file, "r", encoding="utf-8") as tf:
            content = tf.read()
        encoding = "utf-8"
    except UnicodeDecodeError as e:
        try:
            with open(file, "r", encoding="latin-1") as tf:
                content = tf.read()
            encoding = "utf-8"
        except UnicodeDecodeError:
            with open(file, "r", encoding="utf-8", errors="utf-8") as tf:
                content = tf.read()
            encoding = "utf-8"

    content = cleanFileFromtohtmlreplace(content)

    appliedstyle = readStyleFile(None)
    try:
        data = file2HTML(content, "0", appliedstyle,
                         False, "1", encoding=encoding)
        block = makeBlock(data)
        page = py_page.replace(googleTrackerMarker, googlet)
        html = page % (title or f, title or f, block, py2html__version__)
    except Exception as e:
        raise Exception(
            "not python file, running it again {0}".format(file)) from e

    if len(writehtml) > 0:
        outfile = writehtml
    else:
        outfile = racine + ".html"

    with open(outfile, "w", encoding=encoding) as f:
        f.write(html)

    return outfile
