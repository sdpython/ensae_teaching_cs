# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for Flask
"""

from flask import Response

import traceback, threading

def Text2Response(text):
    """
    convert a text into plain text

    @param      text        text to convert
    @return                 textReponse
    """
    return Response(text, mimetype='text/plain')

def Exception2Response(e):
    """
    convert an exception into plain text and display the stack trace

    @param      e           Exception
    @return                 textReponse
    """
    text = traceback.format_exc()
    return Text2Response("Exception: {0}\nSTACK:\n{1}".format(str(e),text))


class FlaskInThread (threading.Thread):
    """
    defines a thread for the server
    """
    def __init__(self, app, host="localhost", port=8080):
        """
        constructor

        @param      app     Flask application
        """
        threading.Thread.__init__(self)
        self._app = app
        self._host = host
        self._port = port
        self.daemon = True

    def run(self):
        """
        start the server
        """
        self._app.run(host=self._host,port=self._port)