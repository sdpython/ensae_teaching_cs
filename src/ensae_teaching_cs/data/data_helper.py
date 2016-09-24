"""
@file
@brief Helpers to get data including in the module itself.
"""
import os


def any_local_file(name, subfolder, local=True, cache_folder=".", filename=True):
    """
    Returns a local data file, reads its content or returns its content.

    @param          name            file to download
    @param          subfolder       sub folder
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    if local:
        this = os.path.abspath(os.path.dirname(__file__))
        this = os.path.join(this, subfolder, name)
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
