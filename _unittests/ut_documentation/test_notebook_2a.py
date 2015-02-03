"""
@brief      test log(time=620s)
"""

import sys, os, unittest, re

try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

try :
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyquickhelper

try :
    import pyensae
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyensae", "src")))
    if path not in sys.path : sys.path.append (path)
    import pyensae

from pyquickhelper.ipythonhelper.notebook_helper import run_notebook
from pyquickhelper import get_temp_folder, fLOG



class TestNotebookRunner2a (unittest.TestCase):
    
    def begin(self, temp):
        docnote = os.path.join(temp, "..", "..", "..", "_doc", "notebooks", "td2a")
        notes = [ os.path.normpath(os.path.join(docnote, _)) for _ in os.listdir(docnote) ]

        addpath = [os.path.dirname(pyquickhelper.__file__), os.path.dirname(pyensae.__file__) ]
        addpath = [ os.path.normpath(os.path.join(_,"..")) for _ in addpath ]

        keepnote = [ ]
        for i,note in enumerate(notes):
            ext = os.path.splitext(note)[-1]
            if ext != ".ipynb" : continue
            if "td2a_correction_session_" not in note: continue
            if "td2a_correction_session_1." in note: continue
            keepnote.append(note)
        return addpath, keepnote
        
    def execute(self, addpath, temp, keepnote, fkeep):
        for i,note in enumerate(keepnote):
            if fkeep(i,note):
                fLOG("******",i,os.path.split(note)[-1])
                outfile = os.path.join(temp, "out_" + os.path.split(note)[-1])
                assert not os.path.exists(outfile)
                out = run_notebook(note, working_dir=temp, outfilename=outfile,
                        additional_path = addpath,
                        valid = lambda code: '%system' not in code)
                #fLOG(out)
                assert os.path.exists(outfile)

    def test_notebook_runner2a_2(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook2a_2")
        addpath, keepnote = self.begin(temp)
        self.execute(addpath, temp, keepnote, lambda i,n : "_2" in n and "_2B" not in n)

    def test_notebook_runner2a_4(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook2a_4")
        addpath, keepnote = self.begin(temp)
        self.execute(addpath, temp, keepnote, lambda i,n : "_4B" in n)

    def test_notebook_runner2a_5(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook2a_5")
        addpath, keepnote = self.begin(temp)
        self.execute(addpath, temp, keepnote, lambda i,n : "_5" in n)

    def test_notebook_runner2a_6(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_notebook2a_6")
        addpath, keepnote = self.begin(temp)
        self.execute(addpath, temp, keepnote, lambda i,n : "_6" in n)


if __name__ == "__main__"  :
    unittest.main ()