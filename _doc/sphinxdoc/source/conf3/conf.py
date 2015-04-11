# -*- coding: utf-8 -*-
#
#  documentation build configuration file, created by
# sphinx-quickstart on Fri May 10 18:35:14 2013.
#

import sys
import os
import datetime
import re
#import solar_theme
import sphinx_bootstrap_theme


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

#html_theme = 'solar_theme'
#html_theme_path = [solar_theme.theme_path]

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

templates_path = [os.path.join(source_path, 'phdoc_static3')]
html_static_path = templates_path

if not os.path.exists(templates_path[0]):
    raise FileNotFoundError(templates_path[0])


html_logo = "project_ico_small.png"

html_sidebars = {}

if html_theme == "bootstrap":
    html_theme_options = {
        'navbar_title': "home",
        'navbar_site_name': "Site",
        'navbar_links': [
            ("XD", "http://www.xavierdupre.fr", True),
            ("blog", "http://www.xavierdupre.fr/blog/xd_blog_nojs.html", True),
            ("pyensae",
             "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html",
             True),
        ],
        'navbar_sidebarrel': False,
        'navbar_pagenav': True,
        'navbar_pagenav_name': "Page",
        'globaltoc_depth': 3,
        'globaltoc_includehidden': "true",
        'navbar_class': "navbar navbar-inverse",
        'navbar_fixed_top': "true",
        'source_link_position': "nav",
        'bootswatch_theme': "spacelab",
        'bootstrap_version': "3",
    }
