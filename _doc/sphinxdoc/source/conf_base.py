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

from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet


set_sphinx_variables(__file__, "Python dans tous ses états", "Xavier Dupré",
                     2017, "sphinx_rtd_theme", None,
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
#\\usepackage{eepic}
imgmath_latex_preamble += custom_preamble
latex_elements['preamble'] += custom_preamble

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

epkg_dictionary["Anaconda"] = 'https://www.continuum.io/downloads'
epkg_dictionary["anaconda"] = 'https://www.continuum.io/downloads'
epkg_dictionary["Arduino"] = 'https://www.arduino.cc/'
epkg_dictionary["AUC"] = 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html#aire-sous-la-courbe'
epkg_dictionary["C++"] = 'https://fr.wikipedia.org/wiki/C%2B%2B'
epkg_dictionary["CNTK"] = 'https://www.microsoft.com/en-us/research/product/cognitive-toolkit/'
epkg_dictionary["dask"] = 'http://dask.pydata.org/en/latest/'
epkg_dictionary["dlib"] = 'http://dlib.net/'
epkg_dictionary["ENSAE"] = 'http://www.ensae.fr/'
epkg_dictionary["falcon"] = 'https://falconframework.org/'
epkg_dictionary["Flask"] = 'http://flask.pocoo.org/'
epkg_dictionary["keyring"] = 'https://github.com/jaraco/keyring'
epkg_dictionary["Linux"] = 'https://fr.wikipedia.org/wiki/Linux'
epkg_dictionary["lightmlboard"] = 'http://www.xavierdupre.fr/app/lightmlboard/helpsphinx/index.html'
epkg_dictionary["lightmlrestpi"] = 'http://www.xavierdupre.fr/app/lightmlrestpi/helpsphinx/index.html'
epkg_dictionary["mlinsights"] = 'http://www.xavierdupre.fr/app/mlinsights/helpsphinx/index.html'
epkg_dictionary["linux"] = 'https://fr.wikipedia.org/wiki/Linux'
epkg_dictionary["matrice de confusion"] = "https://fr.wikipedia.org/wiki/Matrice_de_confusion"
epkg_dictionary["miniconda"] = 'https://conda.io/miniconda.html'
epkg_dictionary["notebook"] = 'http://jupyter.org/'
epkg_dictionary["open source"] = 'http://fr.wikipedia.org/wiki/Open_source'
epkg_dictionary["OS/X"] = 'https://fr.wikipedia.org/wiki/MacOS'
epkg_dictionary["RaspberryPI"] = 'https://www.raspberrypi.org/'
epkg_dictionary["PTVS"] = 'https://microsoft.github.io/PTVS/'
epkg_dictionary["PyCharm"] = 'https://www.jetbrains.com/pycharm/'
epkg_dictionary["pyensae"] = 'http://www.xavierdupre.fr/app/pyensae/helpsphinx/'
epkg_dictionary["pytorch"] = 'http://pytorch.org/'
epkg_dictionary["requests"] = 'http://docs.python-requests.org/en/latest/'
epkg_dictionary["R"] = 'https://www.r-project.org/'
epkg_dictionary['REST API'] = "https://en.wikipedia.org/wiki/Representational_state_transfer"
epkg_dictionary["ROC"] = 'http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html'
epkg_dictionary["Spyder"] = 'https://github.com/spyder-ide/spyder'
epkg_dictionary["teachpyx"] = 'http://www.xavierdupre.fr/app/teachpyx/helpsphinx/'
epkg_dictionary["TensorFlow"] = 'https://www.tensorflow.org/'
epkg_dictionary["theano"] = 'http://deeplearning.net/software/theano/'
epkg_dictionary["Windows"] = 'https://fr.wikipedia.org/wiki/Microsoft_Windows'
