try:
    import pyquickhelper
except ImportError:
    import sys
    sys.path.append(r"../pyquickhelper/src")
    import pyquickhelper

import os
from pyquickhelper import run_doc_server

mappings = { }
fold = os.path.abspath( os.path.dirname(__file__))
fold = os.path.normpath( os.path.join( fold, "..") )
for project in os.listdir(fold):
    full = os.path.join(fold, project)
    if os.path.isdir(full):
        for i in ["", "2", "3"]:
            doc = os.path.join(full, "dist", "html" + i)
            if os.path.exists(doc):
                mappings [ project + i ] = doc
                print("add ", project + i, " --> ", doc )

print("running run_doc_server")
run_doc_server( "localhost",
                mappings = mappings,
                port = 8887)