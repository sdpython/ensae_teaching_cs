
.. _l-ipython_notebook_commandline:

Command line for IPython notebook
=================================

It comes from ``ipython notebook --help``.

The IPython HTML Notebook.

This launches a Tornado based HTML Notebook Server that serves up an
HTML5/Javascript Notebook client.

Subcommands
-----------

Subcommands are launched as `ipython-notebook cmd [args]`. For information on
using subcommand 'cmd', do: `ipython-notebook cmd -h`.

    list

        List currently running notebook servers in this profile.


Options
-------

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'::

    --pylab

        DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.

    --no-browser

        Don't open the notebook in a browser after startup.

    --no-mathjax

        Disable MathJax
        
        MathJax is the javascript library IPython uses to render math/LaTeX. It is
        very large, so you may want to disable it if you have a slow internet
        connection, or for offline use of the notebook.
        
        When disabled, equations etc. will appear as their untransformed TeX source.

    --debug

        set log level to logging.DEBUG (maximize logging output)

    --script

        DEPRECATED, IGNORED

    --quiet

        set log level to logging.CRITICAL (minimize logging output)

    --init

        Initialize profile with default config files.  This is equivalent
        to running `ipython profile create <profile>` prior to startup.

    --no-script

        DEPRECATED, IGNORED
        
    --pylab=<Unicode> (NotebookApp.pylab)

        Default: 'disabled'

        DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.

    --config=<Unicode> (BaseIPythonApplication.extra_config_file)

        Default: ''

        Path to an extra config file to load.

        If specified, load this config file in addition to any other IPython config.

    --ip=<Unicode> (NotebookApp.ip)

        Default: 'localhost'

        The IP address the notebook server will listen on.

    --profile=<Unicode> (BaseIPythonApplication.profile)

        Default: 'default'

        The IPython profile to use.

    --port=<Int> (NotebookApp.port)

        Default: 8888

        The port the notebook server will listen on.

    --ipython-dir=<Unicode> (BaseIPythonApplication.ipython_dir)

        Default: ''

        The name of the IPython directory. This directory is used for logging

        configuration (through profiles), history storage, etc. The default is

        usually $HOME/.ipython. This option can also be specified through the

        environment variable IPYTHONDIR.

    --profile-dir=<Unicode> (ProfileDir.location)

        Default: ''

        Set the profile location directly. This overrides the logic used by the

        `profile` option.

    --transport=<CaselessStrEnum> (KernelManager.transport)

        Default: 'tcp'

        Choices: ['tcp', 'ipc']

    --certfile=<Unicode> (NotebookApp.certfile)

        Default: ''

        The full path to an SSL/TLS certificate file.

    --log-level=<Enum> (Application.log_level)

        Default: 30

        Choices: (0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL')

        Set the log level by value or name.

    --browser=<Unicode> (NotebookApp.browser)

        Default: ''

        Specify what command to use to invoke a web browser when opening the

        notebook. If not specified, the default browser will be determined by the

        `webbrowser` standard library module, which allows setting of the BROWSER

        environment variable to override it.

    --notebook-dir=<Unicode> (NotebookApp.notebook_dir)

        Default: ''

        The directory to use for notebooks and kernels.

    --keyfile=<Unicode> (NotebookApp.keyfile)

        Default: ''

        The full path to a private key file for usage with SSL/TLS.

    --port-retries=<Int> (NotebookApp.port_retries)

        Default: 50

        The number of additional ports to try if the specified port is not

        available.

To see all available configurables, use `--help-all`

Examples
--------

::

    ipython notebook                       # start the notebook
    ipython notebook --profile=sympy       # use the sympy profile
    ipython notebook --certfile=mycert.pem # use SSL/TLS certificate

