"""
@file
@brief Shortcuts for automation
"""

from .jenkins_helper import setup_jenkins_server
from .ftp_publish_helper import publish_documentation
from .notebook_test_helper import execute_notebooks
from .module_documentation import rst_table_modules