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
#import sphinx_rtd_theme
import sphinx_py3doc_enhanced_theme

source_path = os.path.normpath(
    os.path.join(
        os.path.abspath(
            os.path.split(__file__)[0]),
        ".."))

try:
    from conf_base import *
except ImportError:
    sys.path.append(source_path)
    from conf_base import *

#html_theme = 'basicstrap'
html_theme = 'sphinx_py3doc_enhanced_theme'
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
templates_path = [os.path.join(source_path, 'phdoc_static2')]
html_static_path = templates_path

if not os.path.exists(templates_path[0]):
    raise FileNotFoundError(templates_path[0])
