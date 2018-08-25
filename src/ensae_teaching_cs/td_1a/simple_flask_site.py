# -*- coding: utf-8 -*-
"""
@file
@brief Defines a simple web site in Flask which allows unit testing
"""
import logging
from flask import Flask, request
from .flask_helper import Text2Response, Exception2Response


def create_application():
    """
    Creates a :epkg:`Flask` application.
    """
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app = Flask(__name__)

    @app.route('/shutdown/', methods=['POST'])
    def shutdown():  # pylint: disable=W0612
        """
        shuts down the service
        """
        shutdown_server()
        return Text2Response('Server shutting down...')

    @app.route('/help/<path:command>')
    def help_command(command):  # pylint: disable=W0612
        """
        return a very basic help message on command command

        @param      command     command
        @return                 help
        """
        try:
            if command is None or command == "exception":
                raise Exception("no help for command: {0}".format(command))
            return Text2Response("help for command: {0}".format(command))
        except Exception as e:
            return Exception2Response(e)

    @app.route('/form/', methods=['POSTS'])
    def form():  # pylint: disable=W0612
        """
        process a form
        """
        try:
            rows = []
            for k, v in request.form.to.dict().items():
                rows.append("{0}={1}".format(k, v))
            return Text2Response("\n".join(rows))
        except Exception as e:
            return Exception2Response(e)

    @app.route('/')
    def main_page():  # pylint: disable=W0612
        """
        defines the main page
        """
        message = """Simple Flask Site
                                /                   help on command
                                /help/<command>     help on command command
                                /upload/            upload a file (use post)
                                /shutdown/          shutdown the server (for unit test)
                                /form/              process a form
                """.replace("                            ", "")
        return Text2Response(message)

    return app


def shutdown_server():
    """
    to shutdown the service
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
