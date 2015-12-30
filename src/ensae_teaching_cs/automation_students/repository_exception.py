"""
@file
@brief Some automation helpers to grab mails from students about projects.
"""


class RegexRepositoryException(Exception):
    """
    raised when it is impossible to get information from the repository
    """
    pass


class TooManyProjectsException(Exception):
    """
    raised when a group has too many projects
    """
    pass
