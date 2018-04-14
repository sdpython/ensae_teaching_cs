# -*- coding: utf-8 -*-
"""
@file
@brief Function to capture RSS stream from modules for this teachings.
"""

import os
from pyrsslocal import rss_update_run_server


def rss_teachings_update_run_server(dbfile=None, xml_blogs=None, port=8093, browser=None,
                                    period="week", server=None, thread=False):
    """
    create a database if it does not exists, add a table for blogs and posts,
    update the database, starts a server and open a browser,
    if *dbfile* is None, it is set to a default values (in your user directory),
    if *xml_blogs* is None, it is given a default value corresponding the the blogs
    the modules developped for these teachings.

    @param      dbfile      (str) sqllite database to create
    @param      xml_blogs   (str) xml description of blogs (google format)
    @param      port        the main page will be ``http://localhost:port/``
    @param      browser     (str) to choose a different browser than the default one
    @param      period      (str) when opening the browser, it can show the results for last day or last week
    @param      server      to set up your own server
    @param      thread      to start the server in a separate thread

    Example::

        from ensae_teaching_cs.automation import rss_teachings_update_run_server
        rss_teachings_update_run_server(browser="firefox")
    """
    if xml_blogs is None:
        raise ValueError("xml_blogs cannot be None")
    if dbfile is None:
        user = os.path.abspath(os.environ["HOMEPATH"])
        dbfile = os.path.join(user, "ensae_teaching_cs_blogs.db3")
    if not os.path.exists(xml_blogs):
        raise FileNotFoundError(xml_blogs)
    return rss_update_run_server(dbfile=dbfile, xml_blogs=xml_blogs, port=port, browser=browser, period=period,
                                 server=server, thread=thread)
