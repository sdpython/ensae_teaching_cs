"""
@file
@brief Various function about processing latex file
"""
import os
from .latex_file import LatexFile


def explore_folder_produce_code_html(files, header, footer, destination,
                                     classpre="prettyprint", classpre_type="brush: {0}",
                                     classcom="codeintro", skip_missing=False):
    """
    explore a list of files, extract all pieces of code and produces html page
    for each latex file

    @param      files           list of 2uple [ (file, title) ]
    @param      header          header for html file, must contain two ``%s`` for the title (header + body)
    @param      footer          footer
    @param      destination     where to put the produced html file, name is the file with the extension replaced by .html
    @param      classpre        class for pre
    @param      classpre_type   if the type can be guessed, then this template will used instead of the first one
    @param      classcoom       class for the comment
    @param      skip_missing    skip missing file (True) or raise an exception (False)
    @return                     list of produced file
    """
    res = []
    for file in files:

        tex, title = file
        lat = LatexFile(tex)
        html = [header % (title, title)]
        html.append(lat.code_in_html(
            classpre=classpre,
            classpre_type=classpre_type,
            classcom=classcom,
            skip_missing=skip_missing))
        html.append(footer)

        filh = os.path.split(tex)[-1]
        filh = os.path.splitext(filh)[0]
        filh = os.path.join(destination, filh + ".html")

        with open(filh, "w", encoding="utf8") as h:
            h.write("\n".join(html))

        res.append(filh)
    return res
