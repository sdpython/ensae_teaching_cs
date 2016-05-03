
.. _l-jupyter_notebook_commandline:

Command line for Jupyter notebook
=================================

It comes from ``jupyter notebook --help``.

The Jupyter HTML Notebook.

This launches a Tornado based HTML Notebook Server that serves up an
HTML5/Javascript Notebook client.

Subcommands
-----------

Subcommands are launched as `jupyter-notebook cmd [args]`. For information on
using subcommand 'cmd', do: `jupyter-notebook cmd -h`.

list
    List currently running notebook servers.

Options
-------

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--no-browser
    Don't open the notebook in a browser after startup.
-y
    Answer yes to any questions instead of prompting.
--debug
    set log level to logging.DEBUG (maximize logging output)
--pylab
    DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
--script
    DEPRECATED, IGNORED
--no-script
    DEPRECATED, IGNORED
--generate-config
    generate default config file
--no-mathjax
    Disable MathJax

    MathJax is the javascript library Jupyter uses to render math/LaTeX. It is
    very large, so you may want to disable it if you have a slow internet
    connection, or for offline use of the notebook.

    When disabled, equations etc. will appear as their untransformed TeX source.
--config=<Unicode> (JupyterApp.config_file)
    Default: ''
    Full path of a config file.
--port=<Int> (NotebookApp.port)
    Default: 8888
    The port the notebook server will listen on.
--log-level=<Enum> (Application.log_level)
    Default: 30
    Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')
    Set the log level by value or name.
--keyfile=<Unicode> (NotebookApp.keyfile)
    Default: ''
    The full path to a private key file for usage with SSL/TLS.
--pylab=<Unicode> (NotebookApp.pylab)
    Default: 'disabled'
    DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
--ip=<Unicode> (NotebookApp.ip)
    Default: 'localhost'
    The IP address the notebook server will listen on.
--browser=<Unicode> (NotebookApp.browser)
    Default: ''
    Specify what command to use to invoke a web browser when opening the
    notebook. If not specified, the default browser will be determined by the
    `webbrowser` standard library module, which allows setting of the BROWSER
    environment variable to override it.
--client-ca=<Unicode> (NotebookApp.client_ca)
    Default: ''
    The full path to a certificate authority certifificate for SSL/TLS client
    authentication.
--certfile=<Unicode> (NotebookApp.certfile)
    Default: ''
    The full path to an SSL/TLS certificate file.
--port-retries=<Int> (NotebookApp.port_retries)
    Default: 50
    The number of additional ports to try if the specified port is not
    available.
--notebook-dir=<Unicode> (NotebookApp.notebook_dir)
    Default: ''
    The directory to use for notebooks and kernels.
--transport=<CaselessStrEnum> (KernelManager.transport)
    Default: 'tcp'
    Choices: ['tcp', 'ipc']

To see all available configurables, use `--help-all`

Examples
--------

::

    jupyter notebook                            # start the notebook
    jupyter notebook --certfile=mycert.pem      # use SSL/TLS certificate
    jupyter notebook --notebook-dir=<folder>    # change the notebook folder
