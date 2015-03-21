# -*- coding: utf-8 -*-
"""
@file
@brief Defines a simple web site in Flask which allows unit testing
"""


from flask import Flask, request

try:
    from .flask_helper import Text2Response, Exception2Response
except ImportError:
    pass


# -- HELP BEGIN EXCLUDE --

app = Flask(__name__)

if __name__ == "__main__":
    import sys
    sys.path.append("../..")
    from ensae_teaching_cs.td_1a.flask_helper import Text2Response
else:
    from .flask_helper import Text2Response

if __name__ != "__main__":
    app.debug = False
    app.logger.disabled = True
    app.logger_name = 'custom_logger'

    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

# -- HELP END EXCLUDE --


def shutdown_server():
    """
    to shutdown the service
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


# -- HELP BEGIN EXCLUDE --

@app.route('/shutdown/', methods=['POST'])
def shutdown():
    """
    shuts down the service
    """
    shutdown_server()
    return Text2Response('Server shutting down...')


@app.route('/help/<path:command>')
def help_command(command):
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
def form():
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
def main_page():
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

# -- HELP END EXCLUDE --


# -- HELP BEGIN EXCLUDE --

if __name__ == "__main__":
    app.run(host="localhost", port=8019)

# -- HELP END EXCLUDE --
