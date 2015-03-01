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
import sphinxjp.themes.basicstrap

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

from pyquickhelper.helpgen.default_conf import set_sphinx_variables
import pyensae
import pymmails

set_sphinx_variables(__file__,
                     "ensae_teaching_cs",
                     "Xavier Dupré",
                     2014,
                     "sphinx_rtd_theme",
                     None,
                     locals(),
                     add_extensions=None)
                     
                     
if False:
    import sys, os, datetime, re
    import sphinx_bootstrap_theme


    source_path = os.path.normpath(os.path.join(os.path.abspath(os.path.split(__file__)[0])))

    try :
        from conf_base import *
    except ImportError :
        sys.path.append(source_path)
        from conf_base import *

    import sphinxjp.themes.basicstrap
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    templates_path = [ os.path.join(source_path,'phdoc_static') ]
    html_static_path = [ os.path.join(source_path,'phdoc_static') ]

    if not os.path.exists(templates_path[0]):
        raise FileNotFoundError(templates_path[0])