
.. _l-README:

README
======

.. image:: https://travis-ci.org/sdpython/ensae_teaching_cs.svg?branch=master
    :target: https://travis-ci.org/sdpython/ensae_teaching_cs
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/4chpamq95rh5h245?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-cs
    :alt: Build Status Windows

.. image:: https://badge.fury.io/py/ensae_teaching_cs.svg
    :target: http://badge.fury.io/py/ensae_teaching_cs

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/ensae_teaching_cs/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/ensae_teaching_cs?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/ensae_teaching_cs.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/ensae_teaching_cs/issues

.. image:: https://badge.waffle.io/sdpython/ensae_teaching_cs.png?label=ready&title=Ready
    :alt: Waffle
    :target: https://waffle.io/sdpython/ensae_teaching_cs

This page gives access to the content of practical sessions I give at the
`ENSAE <http://www.ensae.fr/>`_. They are based on Python. The project
is hosted on GitHub can be modified by sending me pull requests:

* `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs/>`_
* `documentation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/blog/main_0000.html#ap-main-0>`_

That will be probably one of the few pages in English.

Contributions
-------------

Started in 2014/04.

* Contributor: `Xavier Dupré <http://www.xavierdupre.fr/>`_, ENSAE's students

Setup
-----

* `7zip <http://www.7-zip.org/>`_
* `Anaconda <https://www.continuum.io/downloads>`_
  2 and 3 (to be installed on the same hard drive than the Jenkins build folder)
* `Chrome <https://www.google.fr/chrome/browser/desktop/>`_
* `CMake <https://cmake.org/>`_ (to build XGBoost)
* `Graphviz <http://www.graphviz.org/>`_
* `Git <https://git-scm.com/>`_
* `GitHub <https://desktop.github.com/>`_
* `Java 64 bit <https://www.java.com/fr/download/manual.jsp>`_ (for Spark)
* `Jenkins <https://jenkins.io/>`_ (CI)
* `Miktex Basic Installer 64 bit <https://miktex.org/download>`_ (formula in the documentation)
  (check the option to silently install new packages)
* `Pandoc <http://pandoc.org/>`_ (documentation)
* `Python <https://www.python.org/>`_ 3.5, 3.6, 2.7 64 bit
  (do not add the interpreter on the default PATH)
* `R 3.2 <https://cran.r-project.org/bin/windows/base/old/3.2.0/>`_
* `Scite <http://www.scintilla.org/SciTE.html>`_
* `Visual Studio 2015 Community Edition <https://www.visualstudio.com/fr/vs/community/>`_
  (check C++, C#, Python, CLang) (Cython)

For each Python, you need to install
`pymyinstall <https://pypi.python.org/pypi/pymyinstall/>`_
and type ``pymy_install`` and then remove the modules
being tested (such as this one).

Jenkins requires a few extensions:

* Last Console Output
* Next Jobs

For Jupyter :

::

    pip install widgetsnbextension
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

A local PyPi server needs to be installed:

::

    c:\Python35_x64\Scripts\pypi-server.exe -u -p 8067 --disable-fallback ..\..\local_pypi\local_pypi_server

If some Python scripts use *keyring* to retrieve passwords,
the Jenkins service needs to authentify. On Windows, it goes through ``services.msc``.
To test Python versions Python 2.7, il faut créer un environnement virtuel et installer
pyquickhelper :

::

    cd D:\jenkins\venv\py35
    c:\Python35_x64\scripts\virtualenv.exe pyq --system-site-packages
    cd pyq\Scripts
    pip install pyquickhelper

For some projects (such as the compilation of *pywin32*),
`Windows SDK <https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk>`_
needs to be installed.
