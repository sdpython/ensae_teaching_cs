# -*- coding: utf-8 -*-
"""
@file
@brief Module *ensae_teaching_cs*.
Functions, examples, for the lectures at the
:epkg:`ENSAE`. See :epkg:`ensae_teaching_cs`.
"""

import sys
import os
if sys.version_info[0] < 3:
    raise ImportError("ensae_teaching_cs only works with Python 3")

__version__ = "0.10.3385"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/ensae_teaching_cs"
__url__ = "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html"
__license__ = "MIT License"
__blog__ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "rss_teachings.xml"))


def _setup_hook(add_print=False, unit_test=False):
    """
    function executed before running the unit tests and the documentation,
    does nothing
    """
    pass
