# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for ipython, inspired from `nbopen.py <https://github.com/takluyver/nbopen/blob/master/nbopen.py>`_

"""

import os
import os.path
import warnings
import webbrowser
from notebook import notebookapp
from notebook.utils import url_path_join
from pyquickhelper.loghelper import fLOG


def find_best_server(filename, profile='default'):
    """
    find existing running server

    @param      filename        notebook
    @param      profile         profile to use
    @return                     a running server or None if not found
    """
    kwargs = {}
    if profile != 'default':
        warnings.warn("Jupyter doesn't have profiles")
        kwargs['profile'] = profile
    servers = [si for si in notebookapp.list_running_servers(**kwargs)
               if filename.startswith(si['notebook_dir'])]
    try:
        return max(servers, key=lambda si: len(si['notebook_dir']))
    except ValueError:
        return None


def nb_open(filename, profile='default', open_browser=True, fLOG=fLOG):
    """
    open a notebook with an existing server,
    if no server can be found, it starts a new one
    (and the function runs until the server is closed)

    @param      filename        notebook
    @param      profile         profile to use
    @param      open_browser    open browser or not
    @param      fLOG            logging function
    @return                     a running server or None if not found
    """
    filename = os.path.abspath(filename)
    server_inf = find_best_server(filename, profile)
    if server_inf is not None:
        fLOG("Using existing server at", server_inf['notebook_dir'])
        path = os.path.relpath(filename, start=server_inf['notebook_dir'])
        url = url_path_join(server_inf['url'], 'notebooks', path)
        webbrowser.open(url, new=2)
        return server_inf
    else:
        fLOG("Starting new server")
        home_dir = os.path.dirname(filename)
        server = notebookapp.launch_new_instance(file_to_run=os.path.abspath(filename),
                                                 notebook_dir=home_dir,
                                                 open_browser=open_browser,
                                                 # Avoid it seeing our own argv
                                                 argv=[],
                                                 )
        return server
