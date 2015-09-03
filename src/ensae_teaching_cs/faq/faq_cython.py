# -*- coding: utf-8 -*-
"""
@file
@brief Cython helpers

"""

import os
import sys

from pyquickhelper import run_cmd, noLOG


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

    @FAQ(Cython___Compiler une function Cython?)

    Cette fonction compile un script
    `Cython <http://cython.org/>`_.
    Cette extension permet d'implémenter des fonctions Python dans un
    pseudo-langage proche du `C <https://en.wikipedia.org/wiki/C_(programming_language)>`_.
    Il faut suivre les instructions décrite dans le tutorial
    `The Basics of Cython <http://docs.cython.org/src/tutorial/cython_tutorial.html>`_
    pour réussir à utiliser une fonction codée en Cython.
    C'est ce que fait la fonction :func:`compile_cython_single_script`.


    @endFAQ
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
