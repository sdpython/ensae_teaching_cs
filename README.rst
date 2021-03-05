
.. image:: https://github.com/sdpython/ensae_teaching_cs/blob/master/_doc/sphinxdoc/source/phdoc_static/project_ico.png?raw=true
    :target: https://github.com/sdpython/ensae_teaching_cs/

.. _l-README:

ensae_teaching_cs: teaching materials, algorithmic, machine learning
====================================================================

.. image:: https://travis-ci.org/sdpython/ensae_teaching_cs.svg?branch=master
    :target: https://travis-ci.org/sdpython/ensae_teaching_cs
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/ko5g064idp5srm74?svg=true
    :target: https://ci.appveyor.com/project/sdpython/ensae-teaching-cs
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/ensae_teaching_cs/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/ensae_teaching_cs/tree/master

.. image:: https://badge.fury.io/py/ensae-teaching-cs.svg
    :target: https://pypi.org/project/ensae-teaching-cs/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/ensae_teaching_cs/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/ensae_teaching_cs?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/ensae_teaching_cs.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/ensae_teaching_cs/issues

.. image:: https://api.codacy.com/project/badge/Grade/80a874c0eafd4ea68f3493d73b43f0c5
    :target: https://www.codacy.com/app/sdpython/ensae_teaching_cs?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sdpython/ensae_teaching_cs&amp;utm_campaign=Badge_Grade
    :alt: Codacy Badge

.. image:: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://pepy.tech/badge/ensae_teaching_cs
    :target: https://pypi.org/project/ensae_teaching_cs/
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/ensae_teaching_cs.svg
    :target: https://github.com/sdpython/ensae_teaching_cs/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/ensae_teaching_cs.svg
    :target: https://github.com/sdpython/ensae_teaching_cs/
    :alt: Stars

.. image:: https://img.shields.io/github/repo-size/sdpython/ensae_teaching_cs
    :target: https://github.com/sdpython/ensae_teaching_cs/
    :alt: size

This page gives access to the content of practical sessions I give at the
`ENSAE <http://www.ensae.fr/>`_. They are based on Python. The project
is hosted on GitHub can be modified by sending me pull requests:

* `GitHub/ensae_teaching_cs <https://github.com/sdpython/ensae_teaching_cs/>`_
* `documentation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/blog/main_0000.html#ap-main-0>`_

Contributions
-------------

Started in 2014/04. **Contributors:** `Xavier Dupré <http://www.xavierdupre.fr/>`_,
Anne Muller, Elodie Royant, Matthieu Bizien,
Nicolas Rousset, Jérémie Jakubowicz, Gilles Drigout,
Gaël Varoquaux, Xavier Dupré, ENSAE's students.

Setup
-----

Continuous files
`travis.yml <https://github.com/sdpython/ensae_teaching_cs/blob/master/.travis.yml>`_ or
`appveyor.yml <https://github.com/sdpython/ensae_teaching_cs/blob/master/appveyor.yml>`_
give indications on how to setup a machine to run most of the notebooks.
All notebooks do not run on travis or appveyor due to the excessive
amount of times it requires. They are being run a debian machine every week.
A `coverage page <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/all_notebooks_coverage.html>`_
reports on which ones run and the last time it was run.

Local Continuous Integration
----------------------------

Some of the tools used to modify and run all the notebooks
but they are not optional in most of the cases.

`7zip <http://www.7-zip.org/>`_,
`Chrome <https://www.google.fr/chrome/browser/desktop/>`_,
`CMake <https://cmake.org/>`_,
`Graphviz <http://www.graphviz.org/>`_,
`Git <https://git-scm.com/>`_,
`GitHub <https://desktop.github.com/>`_,
`Java 64 bit <https://www.java.com/fr/download/manual.jsp>`_ (for Spark),
`Jenkins <https://jenkins.io/>`_ (CI),
`Miktex Basic Installer 64 bit <https://miktex.org/download>`_ (formula in the documentation)
(check the option to silently install new packages),
`Pandoc <http://pandoc.org/>`_ (documentation),
`Python <https://www.python.org/>`_ 3.7, 64 bit
(do not add the interpreter on the default `PATH` on Windows),
`Scite <http://www.scintilla.org/SciTE.html>`_ (Windows),
`Visual Studio 2017 Community Edition <https://www.visualstudio.com/fr/vs/community/>`_ (Windows)
(check C++, C#, Python, CLang) (Cython).

A *Jenkins* server was installed on a *debian* machine
to run all the notebooks every week.
*Jenkins* requires a few extensions:
`Last Console Output <https://wiki.jenkins.io/display/JENKINS/Display+Console+Output+Plugin>`_,
`Next Executions <https://wiki.jenkins.io/display/JENKINS/Next+Executions>`_,
`Text File <https://wiki.jenkins-ci.org/display/JENKINS/Text+File+Operations+Plugin>`_.
Extension for `Jupyter <http://jupyter.org/>`_ notebooks
can be installed with the following instructions but this is
really optional.

::

    pip install widgetsnbextension
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

A local PyPi server needs to be installed:

::

    pypi-server.exe -u -p 8067 --disable-fallback ..\..\local_pypi\local_pypi_server

Some Python scripts and notebooks use
`keyring <https://pypi.python.org/pypi/keyring>`_
to retrieve passwords, usually to access private data.
You would have to set them to point to your own data.
The following command line tells how to automatically add
Jenkins jobs to a local Jenkins server:

::

    python setup.py local_jenkins --help
