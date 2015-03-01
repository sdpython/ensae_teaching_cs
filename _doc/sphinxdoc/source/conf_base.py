#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  documentation build configuration file, created by
# sphinx-quickstart on Fri May 10 18:35:14 2013.
#

import sys
import os
import datetime
import re
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "ensae_teaching_cs")))
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

import pyquickhelper
import pyensae
import pymmails

from pyquickhelper.helpgen.default_conf import set_sphinx_variables

project_var_name_t = "ENSAE<br />Xavier Dupré"
project_var_name = "ensae_teaching_cs"
project_var_name_1l = project_var_name_t.replace("<br />", " - ")


set_sphinx_variables(__file__,
                     "ensae_teaching_cs",
                     "Xavier Dupré",
                     2014,
                     "sphinx_rtd_theme",
                     None,
                     locals(),
                     add_extensions=None)


texinfo_documents = [
    ('index',
     '%s' % project_var_name,
     '%s' % project_var_name_t,
     author,
     '%s' % project_var_name,
     'ENSAE, contenu des enseignements',
     'teachings'),
]


autoclass_content = 'both'
autosummary_generate = True
graphviz_output_format = "svg"
