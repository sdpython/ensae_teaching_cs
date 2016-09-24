"""
@file
@brief Data mostly for the first year.
"""
from .data_helper import any_local_file


def anyfile(name, local=True, cache_folder=".", filename=True):
    """
    Returns any file in sub folder `data_1a <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/data/data_1a>`_.

    @param          name            file to download
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return any_local_file(name, "data_1a", cache_folder=cache_folder, filename=filename)


def marathon(local=True, cache_folder=".", filename=True):
    """
    Time about marathons over cities and years

    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return anyfile("marathon.txt", local=local, cache_folder=cache_folder, filename=filename)


def donnees_enquete_2003_television(local=True, cache_folder=".", filename=True):
    """
    Time about marathons over cities and years

    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return anyfile("donnees_enquete_2003_television.txt", local=local, cache_folder=cache_folder, filename=filename)
