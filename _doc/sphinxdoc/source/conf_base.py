# -*- coding: utf-8 -*-
import sys
import os
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet

source_path = os.path.normpath(os.path.join(
    os.path.abspath(os.path.split(__file__)[0])))

try:
    from conf_base import *
except ImportError:
    sys.path.append(source_path)
    from conf_base import *


set_sphinx_variables(__file__, "Python dans tous ses états", "Xavier Dupré",
                     2018, "sphinx_rtd_theme", None,
                     locals(), add_extensions=None,
                     github_repo="https://github.com/sdpython/ensae_teaching_cs.git",
                     extlinks=dict(
                         issue=('https://github.com/sdpython/ensae_teaching_cs/issues/%s', 'issue')),
                     book=True, nblayout='table')

# do not put it back otherwise sphinx import matplotlib before setting up its backend
# for the sphinx command .. plot::
# import pyquickhelper
# import pyensae
# import pymmails
# import pyrsslocal

custom_preamble = """\n\\newcommand{\\girafedec}[3]{ \\begin{array}{ccccc} #1 &=& #2 &+& #3 \\\\ a' &=& a &-& o  \\end{array}}
\\newcommand{\\vecteur}[2]{\\pa{#1,\\dots,#2}}
\\newcommand{\\N}[0]{\\mathbb{N}}
\\newcommand{\\indicatrice}[1]{\\mathbf{1\\!\\!1}_{\\acc{#1}}}
\\usepackage[all]{xy}
\\newcommand{\\infegal}[0]{\\leqslant}
\\newcommand{\\supegal}[0]{\\geqslant}
\\newcommand{\\ensemble}[2]{\\acc{#1,\\dots,#2}}
\\newcommand{\\fleche}[1]{\\overrightarrow{ #1 }}
\\newcommand{\\intervalle}[2]{\\left\\{#1,\\cdots,#2\\right\\}}
\\newcommand{\\loinormale}[2]{{\\cal N}\\pa{#1,#2}}
\\newcommand{\\independant}[0]{\\;\\makebox[3ex]{\\makebox[0ex]{\\rule[-0.2ex]{3ex}{.1ex}}\\!\\!\\!\\!\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}\\makebox[.5ex][l]{\\rule[-.2ex]{.1ex}{2ex}}} \\,\\,}
\\newcommand{\\esp}{\\mathbb{E}}
\\newcommand{\\pr}[1]{\\mathbb{P}\\pa{#1}}
\\newcommand{\\loi}[0]{{\\cal L}}
\\newcommand{\\vecteurno}[2]{#1,\\dots,#2}
\\newcommand{\\norm}[1]{\\left\\Vert#1\\right\\Vert}
\\newcommand{\\dans}[0]{\\rightarrow}
\\newcommand{\\partialfrac}[2]{\\frac{\\partial #1}{\\partial #2}}
\\newcommand{\\partialdfrac}[2]{\\dfrac{\\partial #1}{\\partial #2}}
\\newcommand{\\loimultinomiale}[1]{{\\cal M}\\pa{#1}}
\\newcommand{\\trace}[1]{tr\\pa{#1}}
\\newcommand{\\abs}[1]{\\left|#1\\right|}
"""
# \\usepackage{eepic}
imgmath_latex_preamble += custom_preamble
latex_elements['preamble'] += custom_preamble

project_var_name_t = "ENSAE<br />Xavier Dupré"
project_var_name = "ensae_teaching_cs"
project_var_name_1l = project_var_name_t.replace("<br />", " - ")
html_search_language = "fr"
html_split_index = True

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

# cross references

epkg_dictionary.update({
    'antiseches_ml_basic_plot_binary_classification': "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/plots/plot_roc.html#sphx-glr-gyexamples-plots-plot-roc-py",
    'antiseches_ml_basic_plot_clustering': "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_clustering.html#sphx-glr-gyexamples-ml-basic-plot-clustering-py",
    'ml_basic_plot_binary_classification': "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_binary_classification.html#sphx-glr-gyexamples-ml-basic-plot-binary-classification-py",
    'ml_basic_plot_grid_search': "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_grid_search.html#sphx-glr-gyexamples-ml-basic-plot-grid-search-py",
    'ml_basic_plot_roc': "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/plots/plot_roc.html#sphx-glr-gyexamples-plots-plot-roc-py",
})

# packages and links

epkg_dictionary.update({
    "ACP": 'https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales',
    "Anaconda": 'https://www.continuum.io/downloads',
    "anaconda": 'https://www.continuum.io/downloads',
    "Arduino": 'https://www.arduino.cc/',
    "array": 'https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html',
    "AUC": 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html#aire-sous-la-courbe',
    "basemap": 'https://matplotlib.org/basemap/',
    "blockchain": 'https://fr.wikipedia.org/wiki/Blockchain',
    "bokeh": 'https://fr.wikipedia.org/wiki/Bokeh',
    "Bresenham": 'https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham',
    "C++": 'https://fr.wikipedia.org/wiki/C%2B%2B',
    "C#": 'https://fr.wikipedia.org/wiki/C_sharp',
    "cartopy": "http://scitools.org.uk/cartopy/",
    "dask": 'http://dask.pydata.org/en/latest/',
    "catboost": "https://github.com/catboost/catboost",
    "cartopy": "https://scitools.org.uk/cartopy/docs/latest/",
    "CNIL": 'https://www.cnil.fr/',
    "CNTK": 'https://www.microsoft.com/en-us/research/product/cognitive-toolkit/',
    "cpyquickhelper": 'https://github.com/sdpython/cpyquickhelper/',
    "csharpy": 'http://www.xavierdupre.fr/app/csharpy/helpsphinx/index.html',
    "csharpyml": 'http://www.xavierdupre.fr/app/csharpyml/helpsphinx/index.html',
    "cvxopt": 'https://cvxopt.org/',
    "Cython": 'http://cython.org/',
    'Debian 9': 'https://fr.wikipedia.org/wiki/Debian',
    'deep learning': 'https://en.wikipedia.org/wiki/Deep_learning',
    'dirty-cat': 'https://dirty-cat.github.io/stable/',
    "dlib": 'http://dlib.net/',
    'Elysees': 'http://www.elysee.fr/',
    "ensae_teaching_cs": 'http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html',
    "ensae_teaching_dl": 'http://www.xavierdupre.fr/app/ensae_teaching_dl/helpsphinx/index.html',
    "ENSAE": 'http://www.ensae.fr/',
    'Excel': 'https://fr.wikipedia.org/wiki/Microsoft_Excel',
    "falcon": 'https://falconframework.org/',
    "FastText": 'https://fasttext.cc/',
    "Flask": 'http://flask.pocoo.org/',
    "flask": 'http://flask.pocoo.org/',
    "folium": 'https://folium.readthedocs.io/en/latest/',
    "fortran": 'https://fr.wikipedia.org/wiki/Fortran',
    "Freakeconometrics": "https://freakonometrics.hypotheses.org/",
    "geopandas": 'http://geopandas.org/',
    "GIL": 'https://wiki.python.org/moin/GlobalInterpreterLock',
    "github/sdpython": "https://github.com/sdpython",
    "gmail": 'https://fr.wikipedia.org/wiki/Gmail',
    "javascript": 'https://fr.wikipedia.org/wiki/JavaScript',
    "Jinja2": 'http://jinja.pocoo.org/docs/',
    "Julia": 'https://julialang.org/',
    "Kaggle": 'https://www.kaggle.com/',
    "keras": 'https://keras.io/',
    "keyring": 'https://github.com/jaraco/keyring',
    "Lasso": 'https://fr.wikipedia.org/wiki/Lasso_(statistiques)',
    "lightgbm": "https://github.com/Microsoft/LightGBM/",
    "lightmlboard": 'http://www.xavierdupre.fr/app/lightmlboard/helpsphinx/index.html',
    "lightmlrestapi": 'http://www.xavierdupre.fr/app/lightmlrestapi/helpsphinx/index.html',
    "Linux": 'https://fr.wikipedia.org/wiki/Linux',
    "linux": 'https://fr.wikipedia.org/wiki/Linux',
    "machine learning": 'https://fr.wikipedia.org/wiki/Apprentissage_automatique',
    "MacOS": "https://fr.wikipedia.org/wiki/MacOS",
    "mako": 'http://www.makotemplates.org/',
    "manydataapi": 'http://www.xavierdupre.fr/app/manydataapi/helpsphinx/index.html',
    "mathenjeu": 'http://www.xavierdupre.fr/app/mathenjeu/helpsphinx/index.html',
    "matrice de confusion": "https://fr.wikipedia.org/wiki/Matrice_de_confusion",
    "Microsoft": 'https://fr.wikipedia.org/wiki/Microsoft',
    "miniconda": 'https://conda.io/miniconda.html',
    "mlinsights": 'http://www.xavierdupre.fr/app/mlinsights/helpsphinx/index.html',
    "mlprodict": 'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/index.html',
    'ML.net': 'https://github.com/dotnet/machinelearning',
    "MPI": 'https://en.wikipedia.org/wiki/Message_Passing_Interface',
    "moviepy": "https://zulko.github.io/moviepy/",
    "notebook": 'http://jupyter.org/',
    "Notepad++": "https://notepad-plus-plus.org/",
    "numba": "https://numba.pydata.org/",
    "open source": 'http://fr.wikipedia.org/wiki/Open_source',
    "OpenCV": 'https://opencv.org/',
    "opencv": 'https://opencv.org/',
    "OpenMP": 'https://en.wikipedia.org/wiki/OpenMP',
    "OpenStreetMap": 'https://www.openstreetmap.org/',
    "OSM": 'https://www.openstreetmap.org/',
    "OS/X": 'https://fr.wikipedia.org/wiki/MacOS',
    "PDF": 'https://fr.wikipedia.org/wiki/Portable_Document_Format',
    "pep8": 'https://www.python.org/dev/peps/pep-0008/?',
    "PGCD": 'https://fr.wikipedia.org/wiki/Plus_grand_commun_diviseur',
    "pickle": 'https://docs.python.org/3/library/pickle.html',
    "PPCM": 'https://fr.wikipedia.org/wiki/Plus_petit_commun_multiple',
    "PTVS": 'https://microsoft.github.io/PTVS/',
    "pybind11": 'https://github.com/pybind/pybind11',
    "PyCharm": 'https://www.jetbrains.com/pycharm/',
    "pyecharts": 'https://github.com/pyecharts/pyecharts',
    "pyenbc": 'http://www.xavierdupre.fr/app/pyenbc/helpsphinx/',
    "pyensae": 'http://www.xavierdupre.fr/app/pyensae/helpsphinx/',
    "pymmails": 'http://www.xavierdupre.fr/app/pymmails/helpsphinx/',
    "pygame": 'https://www.pygame.org/',
    "pyproj": 'https://github.com/jswhit/pyproj',
    "pytorch": 'http://pytorch.org/',
    "R": 'https://www.r-project.org/',
    "RaspberryPI": 'https://www.raspberrypi.org/',
    "requests": 'http://docs.python-requests.org/en/latest/',
    'REST API': "https://en.wikipedia.org/wiki/Representational_state_transfer",
    "ROC": 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html',
    "RSA": 'https://fr.wikipedia.org/wiki/Chiffrement_RSA',
    "scikit-plot": 'https://scikit-plot.readthedocs.io/en/stable/',
    "Scikit.ML": 'https://github.com/xadupre/machinelearningext',
    "SciTE": 'http://www.scintilla.org/SciTE.html',
    "Scipy": 'https://www.scipy.org/',
    "seaborn": 'https://seaborn.pydata.org/',
    "spark": 'https://spark.apache.org/',
    "Spark": 'https://spark.apache.org/',
    "sparkouille": 'http://www.xavierdupre.fr/app/sparkouille/helpsphinx/index.html',
    "statsmodels": 'https://www.statsmodels.org/stable/index.html',
    "Spyder": 'https://github.com/spyder-ide/spyder',
    "teachpyx": 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/',
    "TensorFlow": 'https://www.tensorflow.org/',
    "test unitaire": 'https://fr.wikipedia.org/wiki/Test_unitaire',
    "tests unitaires": 'https://fr.wikipedia.org/wiki/Test_unitaire',
    "tkinter": 'https://docs.python.org/3/library/tkinter.html',
    "theano": 'http://deeplearning.net/software/theano/',
    "thorpy": 'http://www.thorpy.org/',
    "TSP": 'https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce',
    "UCI": 'https://archive.ics.uci.edu/ml/datasets.html',
    "Unofficial Windows Binaries for Python Extension Packages": 'https://www.lfd.uci.edu/~gohlke/pythonlibs/',
    "Windows": 'https://fr.wikipedia.org/wiki/Microsoft_Windows',
    "xgboost": "https://xgboost.readthedocs.io/en/latest/",
    "XGBoost": "https://xgboost.readthedocs.io/en/latest/",
    "XML": "https://fr.wikipedia.org/wiki/Extensible_Markup_Language",
})
