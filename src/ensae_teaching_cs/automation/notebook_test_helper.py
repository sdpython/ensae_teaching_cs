#-*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to test notebooks and check they are still working fine.
"""
import os
import sys
from pyquickhelper import noLOG
from pyquickhelper.ipythonhelper.notebook_helper import run_notebook


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
    addpath = [os.path.dirname(pyquickhelper.__file__),
               os.path.dirname(pyensae.__file__),
               os.path.dirname(pymmails.__file__),
               os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."),
               ]
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


def execute_notebooks(folder, notebooks, filter,
                      clean_function=None,
                      fLOG=noLOG,
                      deepfLOG=noLOG):
    """
    execute a list of notebooks

    @param      folder          folder
    @param      notebooks       list of notebooks
    @param      filter          function which validate the notebooks
    @param      clean_function  cleaning function to apply to the code before running it
    @param      fLOG            logging function
    @param      deepfLOG        logging function used to run the notebook
    @return                     dictionary { notebook_file: (isSuccess, outout) }

    The signature of function ``filter`` is::

        def filter( i, filename) : return True or False

    """

    def valid_cell(cell):
        if "%system" in cell:
            return False
        if "df.plot(...)" in cell:
            return False
        if 'df["difference"] = ...' in cell:
            return False
        return True

    addpath = get_additional_paths()
    results = {}
    for i, note in enumerate(notebooks):
        if filter(i, note):
            fLOG("******", i, os.path.split(note)[-1])
            outfile = os.path.join(folder, "out_" + os.path.split(note)[-1])
            try:
                out = run_notebook(note, working_dir=folder, outfilename=outfile,
                                   additional_path=addpath,
                                   valid=valid_cell,
                                   clean_function=clean_function,
                                   fLOG=deepfLOG
                                   )
                if not os.path.exists(outfile):
                    raise FileNotFoundError(outfile)
                results[note] = (True, out)
            except Exception as e:
                results[note] = (False, e)
    return results
