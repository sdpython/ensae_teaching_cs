"""
@file
@brief Uses `pythonnet <https://github.com/sdpython/pythonnet>`_.
"""

import sys, platform

if sys.platform.startswith("win") :
    ver = sys.version_info
    arch = platform.architecture()[0]
    if ver[:2] == (3,3) :
        if arch == "amd64" :
            from .py33x64 import clr 
        elif arch == "32bit" :
            from .py33 import clr 
        else :
            raise ImportError("unable to import pythonnet for this architecture " + str(arch))
    elif ver[:2] == (3,4) :
        if arch == "amd64" :
            from .py34x64 import clr 
        elif arch == "32bit" :
            from .py34 import clr 
        else :
            raise ImportError("unable to import pythonnet for this architecture " + str(arch))        
    else :
        raise ImportError("unable to import pythonnet for this version of python " + str(ver))