"""
@file
@brief clean all files .pyd and .so compiled by the library.
"""
import os
for root, dirs, files in os.walk("."):
    for f in files : 
        if (".pyd" in f or ".so" in f or ".o" in f or ".def" in f) and "_externals" not in root and "exe.win" not in root :
            filename = os.path.join(root,f)
            print ("removing ", filename)
            os.remove(filename)
            