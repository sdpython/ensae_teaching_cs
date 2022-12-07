# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for :epkg:`Flask`.
"""
import ctypes
import traceback
import threading
from flask import Response


def Text2Response(text):
    """
    Converts a text into plain text.

    @param      text        text to convert
    @return                 textReponse
    """
    return Response(text, mimetype='text/plain')


def Exception2Response(e):
    """
    Converts an exception into plain text and display the stack trace.

    @param      e           Exception
    @return                 textReponse
    """
    text = traceback.format_exc()
    return Text2Response(f"Exception: {str(e)}\nSTACK:\n{text}")


class FlaskInThread(threading.Thread):

    """
    Defines a thread for the server.

    :param app: :epkg:`Flask` application
    """

    def __init__(self, app, host="localhost", port=8081, debug=False):
        threading.Thread.__init__(self)
        self._app = app
        self._host = host
        self._port = port
        self.daemon = True
        self.debug = debug

    def run(self):
        """
        Starts the server.
        """
        self._app.run(host=self._host, port=self._port, debug=self.debug)

    def shutdown(self):
        """
        Shuts down the server, the function could work if:

        * method run keeps a pointer on a server instance
          (the one owning method
          `serve_forever
          <https://docs.python.org/3/library/socketserver.html#socketserver.BaseServer.serve_forever>`_)
        * module `werkzeug <http://werkzeug.pocoo.org/>`_
          returns this instance in function
          `serving.run_simple
          <https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/serving.py>`_
        * module `Flask <http://flask.pocoo.org/>`_
          returns this instance in method
          `app.Flask.run
          <https://github.com/mitsuhiko/flask/blob/master/flask/app.py>`_
        """
        raise NotImplementedError()
        # self.server.shutdown()
        # self.server.server_close()

    def raise_exception(self):
        thread_id = self.native_id
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
