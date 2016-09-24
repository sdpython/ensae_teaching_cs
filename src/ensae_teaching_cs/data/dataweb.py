"""
@file
@brief Data mostly for the first year.
"""
from .data_helper import any_local_file


def anyfile(name, local=True, cache_folder=".", filename=True):
    """
    Returns any file in sub folder `data_web <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/data/data_web>`_.

    @param          name            file to download
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return any_local_file(name, "data_web", cache_folder=cache_folder, filename=filename)


def google_trends(name="macron", local=True, cache_folder=".", filename=True):
    """
    Returns some google trends example.

    @param          name            expresion
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return anyfile("google_trends_%s.csv" % name, local=local, cache_folder=cache_folder, filename=filename)
