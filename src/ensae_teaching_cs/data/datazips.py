"""
@file
@brief Data mostly for the first year.
"""
import os
from pyquickhelper.loghelper import noLOG
from pyensae.filehelper.decompress_helper import decompress_zip


def anyzip(filename, local=True, cache_folder=".", fLOG=noLOG, **kwargs):
    """
    Any zip.

    @param          filename        filename
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          fLOG            logging function
    @param          kwargs          downloading arguments
    @return                         filename (str)
    """
    if local:
        this = os.path.abspath(os.path.dirname(__file__))
        this = os.path.join(this, "zips", filename)
        if not os.path.exists(this):
            raise FileNotFoundError(this)
        res = decompress_zip(this, whereTo=cache_folder, fLOG=fLOG)
        if cache_folder is not None:
            res = [os.path.join(cache_folder, _) for _ in res]
    else:
        import pyensae
        this = pyensae.download_data(
            filename, whereTo=cache_folder, fLOG=fLOG, **kwargs)
        if cache_folder is not None:
            res = [os.path.join(cache_folder, _) for _ in this]
        else:
            res = this
    if isinstance(res, list):
        res = res[0]
    return res


def besancon_df(local=True, cache_folder=".", fLOG=noLOG):
    """
    Retrieves ``Besancon.df.zip``.

    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          fLOG            logging function
    @return                         filename (str)
    """
    return anyzip("besancon.df.txt.zip", local=local, cache_folder=cache_folder,
                  fLOG=fLOG, website="xdtd")


def added(local=True, cache_folder=".", fLOG=noLOG):
    """
    Retrieves ``added.zip``.

    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          fLOG            logging function
    @return                         filename (str)
    """
    return anyzip("added.zip", local=local, cache_folder=cache_folder, fLOG=fLOG)
