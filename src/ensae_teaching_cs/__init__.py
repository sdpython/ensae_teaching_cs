#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

import sys
import os
if sys.version_info[0] < 3:
    raise ImportError("ensae_teaching_cs only works with Python 3")

__version__ = "0.6"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/ensae_teaching_cs"
__url__ = "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#ensae_teaching_cs"
__license__ = "BSD License"
__blog__ = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "rss_teachings.xml"))

from .faq.faq_matplotlib import graph_ggplot_with_label
from .td_2a.session_pandas import dfs2excel
from .td_2a.parallel_thread import ParallelThread
from .td_2a.serialization import load_object, dump_object, df2list
from .faq.faq_pandas import read_csv
