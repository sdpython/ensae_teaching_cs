# -*- coding: utf-8 -*-
"""
@file
@brief Cython helpers

"""

import os
import sys
import warnings

from pyquickhelper.loghelper import run_cmd, noLOG


class CustomCythonError(Exception):
    """
    raised by function @see fn compile_cython_single_script
    when a script cannot be compiled with Cython
    """
    pass


def compile_cython_single_script(script, skip_warn=True, fLOG=noLOG):
    """
    This function considers a script ``.pyx``, writes
    the proper setup file, and compiles it.

    @param      script      filename
    @param      skip_warn   skip warnings
    @param      fLOG        logging function

    The function applies the steps described in the basic tutorial
    :epkg:`The Basics of Cython`.
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
        :epkg:`The Basics of Cython`
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

    name = os.path.split(script)[-1]
    namen = os.path.splitext(name)[0]
    setup_script = """
        from distutils.core import setup
        from Cython.Build import cythonize
        setup(
            name='{1}',
            ext_modules=cythonize("{0}",
                                  compiler_directives={{'language_level': {2}}})
        )
        """.replace("        ", "").format(name, namen, sys.version_info[0])

    current, name = os.path.split(script)
    filename = os.path.join(os.path.dirname(script), name + ".setup.py")
    with open(filename, "w") as f:
        f.write(setup_script)

    cmd = sys.executable + f" -u {filename} build_ext --inplace"

    out, err = run_cmd(cmd, wait=True, fLOG=fLOG, change_path=current)
    if len(err) > 0:
        if skip_warn:
            do_raise = False
            lines = err.split("\n")
            for line in lines:
                if len(line) > 0 and not line.startswith(" "):
                    if "UserWarning" not in line:
                        do_raise = True
                        break
        else:
            do_raise = True
        if do_raise:
            with open(script, "r", encoding="utf-8") as f:
                content = f.read()
            raise CustomCythonError(
                f"CMD:\n{cmd}\nOUT:\n{out}ERR:\n{err}\nSCRIPT:\n{content}")
        else:
            warnings.warn(
                f"[compile_cython_single_script] CMD:\n{cmd}\nOUT:\n{out}ERR:\n{err}")
    return out
