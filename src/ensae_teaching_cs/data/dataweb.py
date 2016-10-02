"""
@file
@brief Data from the web
"""
import pandas
from io import StringIO
from .data_helper import any_local_file


def anyfile(name, local=True, cache_folder=".", filename=True, unzip=False, encoding=None):
    """
    Returns any file in sub folder `data_web <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/data/data_web>`_.

    @param          name            file to download
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @param          unzip           unzip the file
    @param          encoding        encoding
    @return                         text content (str)
    """
    return any_local_file(name, "data_web", cache_folder=cache_folder, filename=filename, unzip=unzip, encoding=encoding)


def google_trends(name="macron", local=True, cache_folder=".", filename=True):
    """
    Returns some google trends example.

    @param          name            expression
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @return                         text content (str)
    """
    return anyfile("google_trends_%s.csv" % name, local=local, cache_folder=cache_folder, filename=filename)


def twitter_zip(name="tweets_macron_sijetaispresident_201609", local=True, cache_folder=".",
                filename=False, unzip=True, as_df=True, encoding="utf-8"):
    """
    Returns zipped twitter

    @param          name            filename
    @param          local           local data or web
    @param          cache_folder    where to cache or unzip the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @param          unzip           unzip the file
    @return                         text content (str)
    """
    res = anyfile(name + ".zip", local=local,
                  cache_folder=cache_folder, filename=filename, unzip=unzip, encoding=encoding)
    if as_df:
        st = StringIO(res)
        return pandas.read_csv(st, sep="\t")
    else:
        if isinstance(res, list):
            if len(res) > 1:
                raise ValueError("too many files: {0}".format(res))
            res = res[0]
        return res
