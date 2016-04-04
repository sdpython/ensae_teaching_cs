# -*- coding: utf-8 -*-
import sys
import os
import datetime
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyensae",
            "src")))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pymmails",
            "src")))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyrsslocal",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables


set_sphinx_variables(__file__,
                     "ensae_teaching_cs",
                     "Xavier Dupré",
                     2016,
                     "sphinx_rtd_theme",
                     None,
                     locals(),
                     add_extensions=None)

# do not put it back otherwise sphinx import matplotlib before setting up its backend
# for the sphinx command .. plot::
# import pyquickhelper
# import pyensae
# import pymmails
# import pyrsslocal

imgmath_latex_preamble += "\n\\newcommand{\\girafedec}[3]{ \\begin{array}{ccccc} #1 &=& #2 &+& #3 \\\\ a' &=& a &-& o  \\end{array}}"

project_var_name_t = "ENSAE<br />Xavier Dupré"
project_var_name = "ensae_teaching_cs"
project_var_name_1l = project_var_name_t.replace("<br />", " - ")
html_search_language = "fr"

texinfo_documents = [
    ('index',
     '%s' % project_var_name,
     '%s' % project_var_name_t,
     author,
     '%s' % project_var_name,
     'ENSAE, contenu des enseignements',
     'teachings'),
]

language = "fr"
