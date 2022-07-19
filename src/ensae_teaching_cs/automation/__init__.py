"""
@file
@brief Shortcuts for automation
"""

try:
    from .jenkins_helper import setup_jenkins_server, default_jenkins_jobs
except ImportError as e:
    import warnings
    warnings.warn(f"Could not import jenkins_helper '{e}'")

from .ftp_publish_helper import publish_documentation, publish_teachings_to_web
from .notebook_test_helper import execute_notebooks
from .modules_documentation import rst_table_modules
from .module_backup import ftp_list_modules
from .teaching_modules import get_teaching_modules
