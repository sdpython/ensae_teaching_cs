"""
@file
@brief Shortcuts for homeblog
"""

from .buildrss import file_build_rss
from .buildkeywords import file_all_keywords, build_process_all_pages
from .copyfile import CopyFileForFtp
from .filename_helper import normalize_folder, music_statistics
from .latex_helper import explore_folder_produce_code_html
from .modifypost import modify_all_posts
from .python_exemple_py_to_html import py_to_html_folder, py_to_html_file
from .table_formula import TableFormula
