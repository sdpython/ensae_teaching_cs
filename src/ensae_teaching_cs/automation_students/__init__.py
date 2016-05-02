"""
@file
@brief Shortcuts for automation_students
"""

from .projects_repository import ProjectsRepository
from .mail_helper import grab_addresses, extract_students_mail_and_name_from_gmail
from .projects_helper import extract_students_mails_from_gmail_and_stores_in_folders
from .send_feedback import enumerate_feedback
