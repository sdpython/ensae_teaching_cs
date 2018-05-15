# -*- coding: utf-8 -*-
import sys
import os
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet


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

epkg_dictionary['antiseches_ml_basic_plot_binary_classification'] = "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/plots/plot_roc.html#sphx-glr-gyexamples-plots-plot-roc-py"
epkg_dictionary['antiseches_ml_basic_plot_clustering'] = "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_clustering.html#sphx-glr-gyexamples-ml-basic-plot-clustering-py"
epkg_dictionary['ml_basic_plot_binary_classification'] = "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_binary_classification.html#sphx-glr-gyexamples-ml-basic-plot-binary-classification-py"
epkg_dictionary['ml_basic_plot_grid_search'] = "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/ml_basic/plot_grid_search.html#sphx-glr-gyexamples-ml-basic-plot-grid-search-py"
epkg_dictionary['ml_basic_plot_roc'] = "http://www.xavierdupre.fr/app/papierstat/helpsphinx/gyexamples/plots/plot_roc.html#sphx-glr-gyexamples-plots-plot-roc-py"

# packages and links

epkg_dictionary["ACP"] = 'https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales'
epkg_dictionary["Anaconda"] = 'https://www.continuum.io/downloads'
epkg_dictionary["anaconda"] = 'https://www.continuum.io/downloads'
epkg_dictionary["Arduino"] = 'https://www.arduino.cc/'
epkg_dictionary["Bresenham"] = 'https://fr.wikipedia.org/wiki/Algorithme_de_trac%C3%A9_de_segment_de_Bresenham'
epkg_dictionary["array"] = 'https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html'
epkg_dictionary["AUC"] = 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html#aire-sous-la-courbe'
epkg_dictionary["basemap"] = 'https://matplotlib.org/basemap/'
epkg_dictionary["blockchain"] = 'https://fr.wikipedia.org/wiki/Blockchain'
epkg_dictionary["C++"] = 'https://fr.wikipedia.org/wiki/C%2B%2B'
epkg_dictionary["catboost"] = "https://github.com/catboost/catboost"
epkg_dictionary["CNTK"] = 'https://www.microsoft.com/en-us/research/product/cognitive-toolkit/'
epkg_dictionary["dask"] = 'http://dask.pydata.org/en/latest/'
epkg_dictionary["dlib"] = 'http://dlib.net/'
epkg_dictionary['Elysees'] = 'http://www.elysee.fr/'
epkg_dictionary["ENSAE"] = 'http://www.ensae.fr/'
epkg_dictionary["falcon"] = 'https://falconframework.org/'
epkg_dictionary["FastText"] = 'https://fasttext.cc/'
epkg_dictionary["Flask"] = 'http://flask.pocoo.org/'
epkg_dictionary["folium"] = 'https://folium.readthedocs.io/en/latest/'
epkg_dictionary["fortran"] = 'https://fr.wikipedia.org/wiki/Fortran'
epkg_dictionary["geopandas"] = 'http://geopandas.org/'
epkg_dictionary["GIL"] = 'https://wiki.python.org/moin/GlobalInterpreterLock'
epkg_dictionary["keyring"] = 'https://github.com/jaraco/keyring'
epkg_dictionary["Lasso"] = 'https://fr.wikipedia.org/wiki/Lasso_(statistiques)'
epkg_dictionary["lightgbm"] = "https://github.com/Microsoft/LightGBM/"
epkg_dictionary["lightmlboard"] = 'http://www.xavierdupre.fr/app/lightmlboard/helpsphinx/index.html'
epkg_dictionary["lightmlrestapi"] = 'http://www.xavierdupre.fr/app/lightmlrestapi/helpsphinx/index.html'
epkg_dictionary["Linux"] = 'https://fr.wikipedia.org/wiki/Linux'
epkg_dictionary["linux"] = 'https://fr.wikipedia.org/wiki/Linux'
epkg_dictionary["mlinsights"] = 'http://www.xavierdupre.fr/app/mlinsights/helpsphinx/index.html'
epkg_dictionary["mlprodict"] = 'http://www.xavierdupre.fr/app/mlprodict/helpsphinx/index.html'
epkg_dictionary["machine learning"] = 'https://fr.wikipedia.org/wiki/Apprentissage_automatique'
epkg_dictionary["manydataapi"] = 'http://www.xavierdupre.fr/app/manydataapi/helpsphinx/index.html'
epkg_dictionary["matrice de confusion"] = "https://fr.wikipedia.org/wiki/Matrice_de_confusion"
epkg_dictionary["miniconda"] = 'https://conda.io/miniconda.html'
epkg_dictionary["MPI"] = 'https://en.wikipedia.org/wiki/Message_Passing_Interface'
epkg_dictionary["notebook"] = 'http://jupyter.org/'
epkg_dictionary["Notepad++"] = "https://notepad-plus-plus.org/"
epkg_dictionary["numba"] = "https://numba.pydata.org/"
epkg_dictionary["open source"] = 'http://fr.wikipedia.org/wiki/Open_source'
epkg_dictionary["OpenMP"] = 'https://en.wikipedia.org/wiki/OpenMP'
epkg_dictionary["OpenStreetMap"] = 'https://www.openstreetmap.org/'
epkg_dictionary["OSM"] = 'https://www.openstreetmap.org/'
epkg_dictionary["OS/X"] = 'https://fr.wikipedia.org/wiki/MacOS'
epkg_dictionary["pickle"] = 'https://docs.python.org/3/library/pickle.html'
epkg_dictionary["PTVS"] = 'https://microsoft.github.io/PTVS/'
epkg_dictionary["PyCharm"] = 'https://www.jetbrains.com/pycharm/'
epkg_dictionary["pyenbc"] = 'http://www.xavierdupre.fr/app/pyenbc/helpsphinx/'
epkg_dictionary["pyensae"] = 'http://www.xavierdupre.fr/app/pyensae/helpsphinx/'
epkg_dictionary["pygame"] = 'https://www.pygame.org/'
epkg_dictionary["pyproj"] = 'https://github.com/jswhit/pyproj'
epkg_dictionary["pytorch"] = 'http://pytorch.org/'
epkg_dictionary["R"] = 'https://www.r-project.org/'
epkg_dictionary["RaspberryPI"] = 'https://www.raspberrypi.org/'
epkg_dictionary["requests"] = 'http://docs.python-requests.org/en/latest/'
epkg_dictionary['REST API'] = "https://en.wikipedia.org/wiki/Representational_state_transfer"
epkg_dictionary["ROC"] = 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html'
epkg_dictionary["SciTE"] = 'http://www.scintilla.org/SciTE.html'
epkg_dictionary["spark"] = 'https://spark.apache.org/'
epkg_dictionary["sparkouille"] = 'http://www.xavierdupre.fr/app/sparkouille/helpsphinx/index.html'
epkg_dictionary["Spyder"] = 'https://github.com/spyder-ide/spyder'
epkg_dictionary["teachpyx"] = 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/'
epkg_dictionary["TensorFlow"] = 'https://www.tensorflow.org/'
epkg_dictionary["tkinter"] = 'https://docs.python.org/3/library/tkinter.html'
epkg_dictionary["theano"] = 'http://deeplearning.net/software/theano/'
epkg_dictionary["thorpy"] = 'http://www.thorpy.org/'
epkg_dictionary["TSP"] = 'https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce'
epkg_dictionary["Windows"] = 'https://fr.wikipedia.org/wiki/Microsoft_Windows'
epkg_dictionary["xgboost"] = "https://xgboost.readthedocs.io/en/latest/"
