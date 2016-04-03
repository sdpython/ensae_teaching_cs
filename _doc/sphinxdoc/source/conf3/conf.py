import sys
import os
import datetime
import re
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
            ("blog site", "blog/main_0000", True),
            ("blog XD", "http://www.xavierdupre.fr/blog/xd_blog_nojs.html", True),
            ("pyensae",
             "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html",
             True),
            ("index", "genindex"),
        ],
        'navbar_sidebarrel': False,
        'navbar_pagenav': True,
        'navbar_pagenav_name': "Page",
        'globaltoc_depth': 3,
        'globaltoc_includehidden': "true",
        'navbar_class': "navbar navbar-inverse",
        'navbar_fixed_top': "true",
        'source_link_position': "nav",
        'bootswatch_theme': "yeti",
        # united = weird colors, sandstone=green, simplex=red, paper=trop bleu
        # lumen: OK
        # to try, yeti, flatly, paper
        'bootstrap_version': "3",
    }

blog_root = "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/"
blog_background = False
