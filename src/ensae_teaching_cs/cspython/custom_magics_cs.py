# -*- coding: utf-8 -*-
"""
@file
@brief An example of a custom magic for IPython.
"""
import sys

from IPython.core.magic import Magics, magics_class, cell_magic


@magics_class
class CustomMagicsCs(Magics):

    @cell_magic
    def SPEAK(self, line, cell):
        """
        If the OS is Windows, the magic command will tell the text.

        The function defines ``%%SPEAK``.

        """
        if not sys.platform.startswith("win"):
            raise Exception("Works only on Windows.")

        from ..cspython import vocal_synthesis
        if line is not None:
            spl = line.strip().split(" ")
            lang = spl[0]
            filename = " ".join(spl[1:]) if len(spl) > 1 else ""

        if lang == "-h":
            print("Usage: "
                  "   %%SPEAK fr-FR [filename]"
                  "   speech")
        else:
            vocal_synthesis(cell, lang, filename)


def load_ipython_extension(ip):
    """
    Register magics function, can be called from a notebook.
    """
    ip.register_magics(CustomMagicsCs)
