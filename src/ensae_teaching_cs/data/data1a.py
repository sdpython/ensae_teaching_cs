"""
@file
@brief Data mostly for the first year.
"""
import os


def marathon(local=True, cache_folder=".", filename=False):
    """
    Time about marathons over cities and years

    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    if local:
        this = os.path.abspath(os.path.dirname(__file__))
        this = os.path.join(this, "data_1a", "marathon.txt")
        if not os.path.exists(this):
            raise FileNotFoundError(this)
    else:
        import pyensae
        this = pyensae.download_data("marathon.txt", whereTo=cache_folder)
    if filename:
        return this
    else:
        with open(this, "r") as f:
            return f.read()
