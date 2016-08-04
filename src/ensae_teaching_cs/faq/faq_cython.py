# -*- coding: utf-8 -*-
"""
@file
@brief Cython helpers

"""

import os
import sys

from pyquickhelper.loghelper import run_cmd, noLOG


class CustomCythonError:
    """
    raised by function @see fn compile_cython_single_script
    when a script cannot be compiled with Cython
    """
    pass


def compile_cython_single_script(script, fLOG=noLOG):
    """
    This function considers a script ``.pyx``, writes
    a the proper setup file, and compiles it.

    @param      script      filename
    @param      fLOG        logging function

    The function applies the steps described in the basic tutorial
    `The Basics of Cython <http://docs.cython.org/src/tutorial/cython_tutorial.html>`_.
    The function creates a ``setup.py``
    in the same location and compiles it.

    The compilation requires a compiler
    (not `MinGW <http://www.mingw.org/>`_ or
    `Visual Studio (Community Edition) <https://www.microsoft.com/france/visual-studio/produits/community/Default.aspx>`_).
    If none was found, Python usually displays an error message like::

        Unable to find vcvarsall.bat

    You can also read this old blog post:
    `Build a Python 64 bit extension on Windows <http://www.xavierdupre.fr/blog/2013-07-07_nojs.html>`_
    about this file:: ``C:\\Python35_x64\\lib\\distutils\\msvc9compiler.py``.

    .. faqref::
        :tag: cython
        :title: Compiler une function Cython ?

        Cette fonction compile un script
        `Cython <http://cython.org/>`_.
        Cette extension permet d'implémenter des fonctions Python dans un
        pseudo-langage proche du `C <https://en.wikipedia.org/wiki/C_(programming_language)>`_.
        Il faut suivre les instructions décrite dans le tutorial
        `The Basics of Cython <http://docs.cython.org/src/tutorial/cython_tutorial.html>`_
        pour réussir à utiliser une fonction codée en Cython.
        C'est ce que fait la fonction :func:`compile_cython_single_script`.

        Etant donné que la partie en pseudo C est compilée afin de la rendre beaucoup
        plus rapide, la partie la plus difficile est généralement celle qui consiste à faire
        en sorte que l'interpréteur Python trouve le <b>bon</b> compilateur.
        Ce compilateur est nécessairement le même que celui utilisé pour compiler
        Python et celui-ci change à chaque version.
        Voir
        `Compiling Python on Windows <https://docs.python.org/3/using/windows.html?highlight=visual%20studio#compiling-python-on-windows>`_
        et faire attention à la version de Python que vous utilisez.
    """
    ext = os.path.splitext(script)[-1]
    if ext != ".pyx":
        raise ValueError("no extension .pyx: " + script)
    if not os.path.exists(script):
        raise FileNotFoundError(script)

    setup_script = """
        from distutils.core import setup
        from Cython.Build import cythonize
        setup(
            ext_modules = cythonize("{0}")
        )
        """.replace("        ", "").format(os.path.split(script)[-1])

    current, name = os.path.split(script)
    filename = os.path.join(os.path.dirname(script), name + ".setup.py")
    with open(filename, "w") as f:
        f.write(setup_script)

    cmd = sys.executable + " -u {0} build_ext --inplace".format(filename)

    out, err = run_cmd(cmd, wait=True, fLOG=fLOG, change_path=current)
    if len(err) > 0:
        raise CustomCythonError(
            "CMD:\n{0}\nOUT:\n{1}ERR:\n{2}".format(cmd, out, err))

    return out
