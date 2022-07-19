# -*- coding: utf-8 -*-
"""
@file
@brief An example of a custom magic for IPython.
"""
from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML


@magics_class
class CustomMagics(Magics):

    @line_magic
    def ENSAEl(self, line):
        """
        This command can be activated by typing::

            %ENSAEl
        """
        if "site" in line:
            return HTML(
                '<a href="http://www.xavierdupre.fr/app/ensae_teaching_cs/'
                'helpsphinx/index.html">ENSAE TD</a>')
        if "blog" in line:
            return HTML(
                '<a href="http://www.xavierdupre.fr/blog/xd_blog_nojs.html">blog</a>')
        raise Exception("unknown command: " + line)

    @cell_magic
    def ENSAEb(self, line, cell):
        """
        This command can be activated by typing::

            %%ENSAEb
        """
        return [line, cell]

    @line_cell_magic
    def ENSAE(self, line, cell=None):
        """
        This command can be activated by typing::

            %ENSAE

        Or::

            %%ENSAE
        """
        if cell is None:
            line = line.strip()
            if line.startswith("download"):
                spl = line.split()
                if len(spl) == 2:
                    import pyensae.datasource
                    r = pyensae.datasource.download_data(spl[1])
                    return r
                raise Exception(f"unable to interpret: {line!r}")
            return self.ENSAEl(line)
        raise RuntimeError("Unable to interpret:\n" + cell)


def load_ipython_extension(ip):
    """
    Registers magics function, can be called from a notebook.
    """
    ip.register_magics(CustomMagics)
