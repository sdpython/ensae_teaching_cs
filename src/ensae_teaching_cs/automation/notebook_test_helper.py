#-*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to test notebooks and check they are still working fine.
"""
import os
import shutil
from pyquickhelper.loghelper import noLOG
from pyquickhelper.ipythonhelper.notebook_helper import install_python_kernel_for_unittest
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut
from pyquickhelper.pycode import is_travis_or_appveyor


def ls_notebooks(subfolder):
    """
    list the notebooks in a particular subfolder

    @param      subfolder   subfolder (related to this module)
    @return                 list of files
    """
    this = os.path.abspath(os.path.dirname(__file__))
    docnote = os.path.join(
        this,
        "..",
        "..",
        "..",
        "_doc",
        "notebooks",
        subfolder)
    notes = [
        os.path.normpath(
            os.path.join(
                docnote,
                _)) for _ in os.listdir(docnote)]

    keepnote = []
    for i, note in enumerate(notes):
        ext = os.path.splitext(note)[-1]
        if ext != ".ipynb":
            continue
        keepnote.append(note)
    return keepnote


def get_additional_paths():
    """
    returns a list of paths to add before running the notebooks,
    paths to pyquickhelper, pyensae, pymmails

    @return             list of paths
    """
    import pyquickhelper
    import pyensae
    import pymmails
    import pymyinstall
    import jyquickhelper
    addpath = [os.path.dirname(pyquickhelper.__file__),
               os.path.dirname(pyensae.__file__),
               os.path.dirname(pymmails.__file__),
               os.path.dirname(pymyinstall.__file__),
               os.path.dirname(jyquickhelper.__file__),
               os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."),
               ]
    try:
        import mlstatpy
        addpath.append(os.path.dirname(mlstatpy.__file__))
    except ImportError:
        pass
    addpath = [os.path.normpath(os.path.join(_, "..")) for _ in addpath]
    return addpath


def clean_function_1a(code):
    """
    function which clean cells when unittesting notebooks 1A

    @param      code        cell content
    @return                 modified code
    """
    code = code.replace(
        'run_cmd("exemple.xlsx"',
        'skip_run_cmd("exemple.xlsx"')

    skip = ["faire une chose avec la probabilité 0.7",
            "# déclenche une exception",
            "# pour lancer Excel",
            "for k in list_exercice_1 :",
            "return ....",
            "return [ .... ]",
            "def __init__(self, ...) :",
            "if random.random() <= 0.7 :",
            "dictionnaire_depart.items() [0]",
            "iterateur(0,10) [0]",
            "# ...... à remplir",
            'String.Join(",", a.Select(c=>c.ToString()).ToArray())',
            "# elle n'existe pas encore",
            "from ggplot import *",
            "print(tab[i] + tab[i+1])",
            "if n = 1:",
            "clenche une exception",
            'y = "a" * 3 + 1',
            "i = list_exercice_1.index(k)",
            "raise KeyError('Arrêtons-nous...')",
            # ggplot calls method show and it opens window blocking the offline
            # execution
            ]
    rep = [("# ...", "pass # "),
           ("%timeit", "#%timeit"),
           ]
    spl = ["# ......",
           "# elle n'existe pas encore",
           ]

    for s in skip:
        if s in code:
            return ""

    for s in spl:
        if s in code:
            code = code.split(s)[0]

    for s in rep:
        code = code.replace(s[0], s[1])

    return code


def execute_notebooks(folder, notebooks, filter, clean_function=None,
                      fLOG=noLOG, deepfLOG=noLOG, replacements=None, dump=None,
                      additional_path=None):
    """
    Execute a list of notebooks.

    @param      folder          folder
    @param      notebooks       list of notebooks
    @param      filter          function which validates the notebooks to test (True means will be tested)
    @param      clean_function  cleaning function to apply to the code before running it
    @param      fLOG            logging function
    @param      deepfLOG        logging function used to run the notebook
    @param      replacements    replacements
    @param      dump            see function `execute_notebook_list_finalize_ut <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/ipythonhelper/run_notebook.html#pyquickhelper.ipythonhelper.run_notebook.execute_notebook_list_finalize_ut>`_
    @param      additional_path additional path to add
    @return                     dictionary { notebook_file: (isSuccess, outout) }

    The signature of function ``filter`` is::

        def filter(i, filename):
            return True or False
    """

    def valid_cell(cell):
        if "%system" in cell:
            return False
        if "df.plot(...)" in cell:
            return False
        if 'df["difference"] = ...' in cell:
            return False
        if 'remote_open' in cell:
            return None
        if 'blobpassword' in cell:
            return None
        if 'String.Join(",", a.Select(c=>c.ToString()).ToArray())' in cell:
            return False
        if 'Speech.VocalSynthesis("ENSAE", "fr-FR","","")' in cell:
            return False
        if 'Speech.VocalSynthesis(text, lang, voice, filename)' in cell:
            return False
        if "%%SPEAK fr-FR" in cell:
            return False
        return True

    addpaths = get_additional_paths()
    if additional_path is not None:
        addpaths += additional_path
    kernel_name = None if is_travis_or_appveyor() else install_python_kernel_for_unittest(
        "ensae_teaching_cs")
    if filter:
        notebooks = [_ for i, _ in enumerate(notebooks) if filter(i, _)]
    if len(notebooks) == 0:
        raise ValueError("Empty list of notebooks.")
    res = execute_notebook_list(folder, notebooks, fLOG=fLOG, clean_function=clean_function,
                                valid=valid_cell, additional_path=addpaths, kernel_name=kernel_name,
                                replacements=replacements)
    execute_notebook_list_finalize_ut(
        res, fLOG=fLOG, dump=dump)
    return res


def copy_data_file(notebook_folder, filename, dest, fLOG=noLOG):
    """
    copy a data file from a notebook folder to the current folder

    @param      notebook_folder     notebook_folder
    @param      filename            filename or list of file names
    @param      destination         destination folder
    @parm       fLOG                logging function
    @return                         copied files
    """
    if isinstance(filename, list):
        return [copy_data_file(notebook_folder, f, dest) for f in filename]
    else:
        src = os.path.abspath(os.path.join(os.path.dirname(
            __file__), "..", "..", "..", "_doc", "notebooks", notebook_folder, filename))
        if not os.path.exists(src):
            raise FileNotFoundError(src)
        if not os.path.exists(dest):
            raise FileNotFoundError(dest)
        shutil.copy(src, dest)
        res = os.path.join(dest, os.path.split(src)[-1])
        fLOG("copy", res)
        return res
