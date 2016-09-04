"""
@file
@brief Data mostly for the first year.
"""
import os


def anyfile(name, local=True, cache_folder=".", filename=True):
    """
    Time about marathons over cities and years

    @param          name            file to download
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    if local:
        this = os.path.abspath(os.path.dirname(__file__))
        this = os.path.join(this, "data_1a", name)
        if not os.path.exists(this):
            raise FileNotFoundError(this)
    else:
        import pyensae
        this = pyensae.download_data(name, whereTo=cache_folder)
    if filename:
        return this
    else:
        with open(this, "r") as f:
            return f.read()


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
