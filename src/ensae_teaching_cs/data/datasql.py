"""
@file
@brief Example of databases
"""
from .data_helper import any_local_file


def anyfile(name, local=True, cache_folder="."):
    """
    Returns any file in sub folder
    `data_web <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/data/data_sql>`_.

    @param          name            file to download
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @return                         text content (str)
    """
    return any_local_file(name, "data_sql", cache_folder=cache_folder, filename=True)


def simple_database(name="World.db3", local=True, cache_folder="."):
    """
    Returns a simple database.

    @param          name            filename
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @return                         text content (str)
    """
    return anyfile(name, local=local, cache_folder=cache_folder)
