#-*- coding: utf-8 -*-
"""
@file
@brief An example of a custom magic for IPython.
"""

from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
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
            return HTML('<a href="http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html">ENSAE TD</a>')
        elif "blog" in line :
            return HTML('<a href="http://www.xavierdupre.fr/blog/xd_blog_nojs.html">blog</a>')
        else: 
            raise Exception("unknown command: " + line)
        
        #print("Full access to the main IPython object:", self.shell)
        #print("Variables in the user namespace:", list(self.shell.user_ns.keys()))

    @cell_magic
    def ENSAEb(self, line, cell):
        """
        This command can be activated by typing::
        
            %%ENSAEb
            
        """
        return line, cell

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
                if len(spl)==2:
                    import pyensae
                    r = pyensae.download_data(spl[1])
                    return r
                else :
                    raise Exception("unable to interpret: " + line)
            else :
                return self.ENSAEl(line)
        else:
            raise Exception("unable to interpret:\n" + cell)

def register_magics():
    ip = get_ipython()
    ip.register_magics(CustomMagics)
    