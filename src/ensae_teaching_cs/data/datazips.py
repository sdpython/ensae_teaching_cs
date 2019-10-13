# coding: utf-8
"""
@file
@brief Data mostly for the first and second years.
"""
import os
from pyquickhelper.loghelper import noLOG
from pyensae.filehelper.decompress_helper import decompress_zip


def anyzip(filename, local=True, cache_folder=".", multi=False,
           fLOG=noLOG, **kwargs):
    """
    Any zip.

    @param          filename        filename
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          fLOG            logging function
    @param          multi           multiple files
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
        return res if multi else res[0]
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


def deal_flow_espace_vert_2018_2019(local=True, cache_folder=".", fLOG=noLOG):
    """
    Retrieves ``deal_flow_espaces_verts_2018_2019.zip``.
    The sources compiles two files from pages:
    * `Deal flow des projets verts : projets notifiés et financés en 2018
      <https://data.ademe.fr/datasets/jeu-de-donnees-deal-flow-2018>`_
    * `Deal flow des projets verts - Projets financés en 2019 et investissements envisagés en 2019
      <https://data.ademe.fr/datasets/jeu-de-donnees-deal-flow-2019>`_
    See :ref:`dealflowespacevertrst`.
    """
    return anyzip("deal_flow_espaces_verts_2018_2019.zip", local=local,
                  cache_folder=cache_folder, multi=True, fLOG=fLOG)
