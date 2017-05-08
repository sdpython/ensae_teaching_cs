"""
@file
@brief Shortcuts for homeblog

Some shortcuts I use for windows.

Launch `Scite <http://www.scintilla.org/SciTE.html>`_:

::

    set CURRENT=%~dp0
    set PYTHONPATH=%CURRENT%\\__home_\\GitHub\\pyquickhelper\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\actuariat_python\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\code_beatrix\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\ensae_projects\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\ensae_teaching_cs\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\jupytalk\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\jyquickhelper\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\mlstatpy\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\pyensae\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\pymmails\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\pyquickhelper\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\pyrsslocal\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\pysqllike\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\teachpyx\\src
    set PYTHONPATH=%PYTHONPATH%;%CURRENT%\\__home_\\GitHub\\tkinterhelper\\src
    start wscite\\scite.exe

"""

from .buildrss import file_build_rss
from .buildkeywords import file_all_keywords, build_process_all_pages
from .copyfile import CopyFileForFtp
from .filename_helper import normalize_folder, music_statistics
from .latex_helper import explore_folder_produce_code_html
from .modifypost import modify_all_posts
from .python_exemple_py_to_html import py_to_html_folder, py_to_html_file
from .table_formula import TableFormula
