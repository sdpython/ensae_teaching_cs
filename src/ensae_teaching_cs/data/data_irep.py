# -*- coding: utf-8 -*-
"""
@file
@brief Jeux de données reliés aux émissions polluantes.
"""


def load_irep(cache="."):
    """
    Télécharge les données du `registre des émissions polluantes (IREP)
    <http://www.georisques.gouv.fr/dossiers/irep/telechargement#>`_
    pour les années 2003-2017.

    @param          cache       where to cache or unzip the data if downloaded a second time
    @return                     list of files
    """
    from pyensae.datasource import download_data
    name = "irep.zip"
    res = download_data(name, whereTo=cache)
    return res
