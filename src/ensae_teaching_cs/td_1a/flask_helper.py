# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for :epkg:`Flask`.
"""
import traceback
import threading
from flask import Response


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
    return Text2Response("Exception: {0}\nSTACK:\n{1}".format(str(e), text))


class FlaskInThread(threading.Thread):

    """
    Defines a thread for the server.
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
        self._app.run(host=self._host, port=self._port)

    def shutdown(self):
        """
        Shuts down the server, the function could work if:

        * method run keeps a pointer on a server instance
          (the one owning method
          `serve_forever <https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.serve_forever>`_)
        * module `werkzeug <http://werkzeug.pocoo.org/>`_
          returns this instance in function
          `serving.run_simple <https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/serving.py>`_
        * module `Flask <http://flask.pocoo.org/>`_
          returns this instance in method
          `app.Flask.run <https://github.com/mitsuhiko/flask/blob/master/flask/app.py>`_
        """
        raise NotImplementedError()
        # self.server.shutdown()
        # self.server.server_close()
