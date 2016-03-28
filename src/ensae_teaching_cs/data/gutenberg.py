#-*- coding: utf-8 -*-
"""
@file
@brief Link to data from `Gutenberg <http://www.gutenberg.org/>`_,
provides an automated way to get the data from this website.
Some data may be replicated here to unit test notebooks.
"""
import os
import urllib.request
from urllib.error import URLError


def gutenberg_name(name="condamne", local=False, load=False):
    """
    Retrieves data from `Gutenberg <http://www.gutenberg.org/>`_.

    @param      name        name of the requested data
    @param      local       use local version
    @param      load        load the data
    @return                 content or filename or url

    List of available datasets:

    * ``condamne``: `Le dernier jour d'un condamné <http://www.gutenberg.org/ebooks/6838>`_, Victor Hugo
    """
    this = os.path.abspath(os.path.dirname(__file__))
    data = os.path.join(this, "data_gutenberg")
    if name == "condamne":
        url = "http://www.gutenberg.org/cache/epub/6838/pg6838.txt"
        loc = os.path.join(data, "pg6838.txt")
        if load:
            if not local:
                try:
                    with urllib.request.urlopen(url) as u:
                        text = u.read()
                        u.close()
                except URLError:
                    # we switch to local
                    text = None
                if text is not None:
                    text = text.decode("utf8")
                    return text
            if not os.path.exists(loc):
                raise FileNotFoundError(loc)
            with open(loc, "r", encoding="utf8") as f:
                text = f.read()
            return text
        else:
            if local:
                if not os.path.exists(loc):
                    raise FileNotFoundError(loc)
                return loc
            else:
                return url
    else:
        raise ValueError(
            "unknown name '{0}', check the code of the function".format(name))
