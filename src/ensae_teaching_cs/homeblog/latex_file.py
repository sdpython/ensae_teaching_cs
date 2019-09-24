"""
@file
@brief Ths file contains some functions to extract pieces of codes from a latex file
"""

import re
import os

from pyquickhelper.loghelper import fLOG
from .program_helper import guess_language_code


class LatexCode:
    """
    many latex contains examples of codes
    this describes one of them
    """

    comment_analysis = re.compile("([(][-]{2}([a-z]+)[-]{2}[)])")

    def __init__(self, parent, line, content, comment=None, content_type=None):
        """
        constructor
        @param      parent      (LatexFile) object
        @param      line number (int), 0 is the first one
        @param      content     code content
        @param      comment     comment for the piece of code

        if comment contains ``(--<something>--)``, it indicates the content type of the zone (ie: py)
        """
        self.parent = parent
        self.line = line
        self.content = content
        self.comment = comment
        if not isinstance(line, tuple):
            raise TypeError("we expect tuple for the line number")
        if content_type is not None:
            self.content_type = content_type
        elif self.comment is None:
            self.content_type = ""
        else:
            se = LatexCode.comment_analysis.search(self.comment)
            if se:
                self.content_type = se.groups()[1]
                self.comment = self.replace(se.groups()[0], "")
            else:
                guess = guess_language_code(self.content)
                self.content_type = guess[
                    0] if guess is not None and guess[1] > 0.66 else ""

    def __str__(self):
        """
        usual
        """
        comment = (", comment: %s (-t:%s)" % (self.comment,
                                              self.content_type)) if self.comment is not None else ""
        return "  File \"%s\", line %d%s" % (self.parent.file, self.line[-1] + 1, comment)


class LatexIncludedFile:
    """
    describe a file included a latex file

    @var    parent      (LatexFile)
    @var    line        (int) line number
    @var    file        (str) file name
    @var    comment     (str) comment
    @var    obj         (LatexFile|LatexCode) object
    """

    def __init__(self, parent, line, file, comment):
        """
        constructor

        @param      parent  (LatexFile) which contains this file
        @param      line    line number where it was found in the late file it belongs to
        @param      file    file name
        @param      comment comment
        """
        self.parent = parent
        self.line = line
        self.file = file
        self.comment = comment
        self.init()

    def init(self):
        """
        complete the contructor
        """
        ext = os.path.splitext(self.file)[-1].lower()
        if ext == ".tex":
            self.obj = LatexFile(self.file, self.parent.root, line=self.line)
        elif ext in [".py", ".cpp", ".h", ".hpp", ".c", ".hhp", ".vba", ".sql",
                     ".r", ".hhk", ".iss", ".txt", ".xml", ".html", ".js"]:

            try:
                with open(self.file, "r", encoding="utf8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(self.file, "r", encoding="latin-1") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(self.file, "r") as f:
                        content = f.read()
            sexp = ext.strip(". ")
            typ = {"html": "xml", "hpp": "cpp", "h": "cpp", "vba": "vb",
                   "py": "py", "xml": "xml", "cpp": "cpp", "js": "js", "c": "cpp",
                   "sql": "sql"}. get(sexp, None)
            self.obj = LatexCode(self.parent, self.line,
                                 content, self.comment, content_type=typ)
        else:
            raise ValueError(
                "unable to read file %s, not python, not latex" % self.file)

    def enumerate_code(self, skip_missing=False):
        """
        enumerate all pieces of code (in ``verbatim``, ``verbatimx`` or ``\\inputcode`` sections

        @return         LatexCode
        """

        if isinstance(self.obj, LatexFile):
            for co in self.obj.enumerate_code(skip_missing=skip_missing):
                yield co
        elif isinstance(self.obj, LatexCode):
            yield self.obj
        else:
            raise TypeError("unexpected class for self.obj: %s" %
                            str(type(self.obj)))


class LatexFile:
    """
    description of a latex file

    @var    file        file name for the late file
    @var    root        every file referenced in the latex will use ``root`` as a root for the relative paths
    @var    filelines   for each line, we store every included file here,
                        it is a dictionary { line number : object file }
    @var    line        keeps line number in a stack (if this file is included by another one)
    """

    def __init__(self, file, root=None, line=tuple()):
        """
        constructor

        @param      file        file name
        @param      root        for included files, the root determines
                                the folder relative paths refer to,
                                if None, the file folder will be used as a root
        @param      line        if this file is included by another one, it keeps the line number in a stack
        """
        self.file = file
        self.root = root
        self.filelines = {}
        self.line = line

        if self.root is None:
            self.root = os.path.abspath(os.path.split(file)[0])

    def __str__(self):
        """
        usual
        """
        return "file: %s" % self.file

    def read(self):
        """
        read the latex file and stores into ``self.content``,
        if the method is called a second time,
        the function will use a member ``content``.

        @return         string (file content)
        """
        if "content" in self.__dict__ and self.content is not None:
            return self.content

        else:
            try:
                with open(self.file, "r", encoding="utf8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(self.file, "r", encoding="latin-1") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(self.file, "r") as f:
                        content = f.read()
            self.content = content

        return content

    @staticmethod
    def dichotomy_find(array, value):
        """
        find the greatest position which contains a value below ``value``

        @param      value       value
        @param      array       array of integers
        @return                 position p such as array[p] <= value < array[p+1]
        """
        a = 0
        b = len(array) - 1
        while a < b:
            m = (a + b) // 2
            if value == array[m]:
                return m
            elif value < array[m]:
                b = m
            elif a == m:
                return a
            else:
                a = m
        return a

    def enumerate_code(self, skip_missing=False):
        """
        enumerate all pieces of code (in ``verbatim``, ``verbatimx`` or ``\\inputcode`` sections

        @param      skip_missing        if True, avoids stopping whenever a file is not found
        @return                         LatexCode
        """
        try:
            content = self.read()
        except FileNotFoundError as e:
            if skip_missing:
                fLOG("w,unable to find file", self.file)
                content = " "
            else:
                raise e
        lines = content.split("\n")

        linebeginning = []
        s = 0
        for line in lines:
            linebeginning.append(s)
            s += len(line) + 1

        p = re.compile("(\\\\begin[{]verbatim(x|no|nocut)?[}]( *[%]{3}(.*?)[%]{3})?((.|\\n)*?)\\\\end[{]verbatim(x|no|nocut)??[}])|" +
                       "(\\\\inputcodes[{]([./a-zA-Z0-9_]+?)[}][{](.*?)[}][{](.*?)[}])|" +
                       "(\\\\input[{]([./a-zA-Z0-9_]+?)[}])|" +
                       "(\\\\inputcode[{]([./a-zA-Z0-9_]+?)[}][{](.*?)[}])")

        recom = re.compile("([%]{3}(.*?)[%]{3})")

        for m in p.finditer(content):
            a = m.span()[0]
            li = LatexFile.dichotomy_find(linebeginning, a)
            gs = tuple(m.groups())

            # if gs[0] is None :
            #    for i,g in enumerate(gs) : print (i,g)

            if gs[0] is not None:
                # verbatim
                #  0                                                           1   2       3        4
                # ('\\begin{verbatimx} ... \\end{verbatimx}', 'x', None, None,
                # '\n  x = 5\n  y = 10\n  z = x + y\n  print (z)    # affiche z\n  ', ' ', 'x',
                # None, None, None, None, None, None)
                #
                comment = gs[3].strip() if gs[3] is not None else gs[3]
                if comment is None or len(comment) == 0:
                    # we check the previous line
                    ci = li - 1
                    if ci > 0:
                        com = recom.search(lines[ci])
                        if com:
                            comment = com.groups()[1]
                c = LatexCode(self, self.line + (li,), gs[4], comment)
                yield c

            elif gs[7] is not None:
                # input code
                # (None, None, None, None, None,
                # "\\inputcodes{../data/td_note_2006.py}{exercice pour ...valuer}{, correction 2006}",
                # '../data/td_note_2006.py', "exercice pour ...", ', correction 2006')
                if li not in self.filelines:
                    fil = os.path.join(self.root, gs[8])
                    self.filelines[li] = LatexIncludedFile(
                        self, self.line + (li,), fil, gs[10])

                for co in self.filelines[li].enumerate_code():
                    yield co

            elif gs[11] is not None:
                if li not in self.filelines:
                    fil = os.path.join(self.root, gs[12])
                    self.filelines[li] = LatexIncludedFile(
                        self, self.line + (li,), fil, None)

                for co in self.filelines[li].enumerate_code(skip_missing=skip_missing):
                    yield co

            elif gs[13] is not None:
                # print (len(gs),gs)
                # input code
                # (None, None, None, None, None,
                # "\\inputcodes{../data/td_note_2006.py}{exercice pour ...valuer}{, correction 2006}",
                # '../data/td_note_2006.py', "exercice pour ...", ', correction 2006')
                if li not in self.filelines:
                    fil = os.path.join(self.root, gs[14])
                    self.filelines[li] = LatexIncludedFile(
                        self, self.line + (li,), fil, gs[15])

                for co in self.filelines[li].enumerate_code():
                    yield co

    def code_in_html(self, header=None, footer=None, classpre="prettyprint", classpre_type="brush: {0}",
                     classcom="codeintro", skip_missing=False, remove_unnecessary_indentation=True):
        """
        produces html format containing all the code example

        @param      header          if not None, it should end by ``<body>``
        @param      footer          if not None, it should start by ``</body>``
        @param      classpre        if not, use ``<pre>`` otherwise ``<pre class="classpre">``
        @param      classpre_type   if the type can be guessed, then this template will used instead of the first one
        @param      classcom        if the comment is not none, it will output ``<p class="classcom">`` (if classcom is not None)
        @param      skip_missing    if True, avoids stopping whenever a file is not found
        @param      remove_unnecessary_indentation  remove unnecessary indentation
        @return                     string string
        """
        res = []
        if header is not None:
            res.append(header)
        for code in self.enumerate_code(skip_missing=skip_missing):
            if code.comment is not None:
                com = ("<p class=\"%s\">%s</p>" % (classcom, code.comment)
                       ) if classcom is not None else ("<p>%s</p>" % code.comment)
            else:
                com = ("<p class=\"%s\">File: %s, line %d</p>" %
                       (classcom,
                           os.path.split(code.parent.file)[-1],
                           code.line[-1])) \
                    if classcom is not None else ("<p>line %s</p>" % code.line)
            res.append(com)
            res.append("<!-- File \"%s\", lines %s -->" %
                       (code.parent.file, str(code.line)))

            if classpre_type is not None and len(classpre_type) > 0 and \
               code.content_type is not None and len(code.content_type) > 0:
                pre = ("<pre class=\"%s\">") % classpre_type.format(
                    code.content_type)
            else:
                pre = (
                    "<pre class=\"%s\">") % classpre if classpre is not None else "<pre>"
            res.append(pre)

            memocode = code.content.replace("<", "&lt;").replace(">", "&gt;")
            if remove_unnecessary_indentation:
                lines = memocode.split("\n")
                mini = None
                for line in lines:
                    temp = line.lstrip()
                    if len(temp) > 0:
                        df = len(line) - len(temp)
                        mini = df if mini is None else min(mini, df)

                df = mini
                if df is not None and df > 0:
                    for i in range(len(lines)):
                        li = lines[i]
                        if len(li) >= df:
                            lines[i] = lines[i][df:]
                    memocode = "\n".join(lines)

            res.append(memocode)
            res.append("</pre>")

        return "\n".join(res)
