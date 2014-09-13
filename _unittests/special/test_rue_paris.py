"""
@brief      test log(time=17s)

"""
import os,sys,unittest

try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyensae", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper
    import pyensae

from pyquickhelper import fLOG
from src.ensae_teaching_cs.special.rues_paris import get_data, bellman, kruskall, possible_edges, degre, eulerien_extension, distance_paris, euler_path

class TestRueParis (unittest.TestCase):
    
    def _test_get_data(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"temp_rues")
        if not os.path.exists(folder) : os.mkdir(folder)
        for ext in [".txt",".zip"]:
            f = os.path.join(folder, "paris_54000" + ext)
            if os.path.exists(f): os.remove(f)
        data = get_data(whereTo=folder)
        fLOG(len(data))
        assert len(data)>0
        total = sum( _[-1] for _ in data )
        fLOG("total length", total)
        
    def _test_algo(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"temp_rues2")
        if not os.path.exists(folder) : os.mkdir(folder)
        edges = get_data(whereTo=folder)
        edges = edges[:1000]
        max_segment = max ( e[-1] for e in edges )
        possibles = possible_edges(edges, max_segment/8, fLOG = fLOG)
        init = bellman(edges, fLOG = fLOG, allow = lambda e : e in possibles)
        fLOG("---")
        init = bellman(edges, fLOG = fLOG, allow = lambda e : e in possibles, init = init)
        fLOG("---")
        added = kruskall(edges, init, fLOG = fLOG)
        d = degre(edges + added)
        allow = sorted([ k for k,v in d.items() if v%2 == 1 ])
        fLOG("degrees", allow)
        allow = set(allow)
        fLOG("---")
        init = bellman(edges, fLOG = fLOG, 
                allow = lambda e : e in possibles or e[0] in allow or e[1] in allow, 
                init = init)
        fLOG("---")
        added = kruskall(edges, init, fLOG = fLOG)
        d = degre(edges + added)
        allow = sorted([ k for k,v in d.items() if v%2 == 1 ])
        fLOG("degrees", allow)
        
    def _test_algo2(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"temp_rues2")
        if not os.path.exists(folder) : os.mkdir(folder)
        edges = get_data(whereTo=folder)
        edges = edges[:1000]
        added = eulerien_extension(edges, fLOG = fLOG, alpha = 1/8)
        assert len(added)>0
        fLOG ("nb added",len(added))

    def test_algo3(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        return
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"temp_rues2")
        if not os.path.exists(folder) : os.mkdir(folder)
        edges = get_data(whereTo=folder)
        fLOG("start")
        added = eulerien_extension(edges, fLOG=fLOG, distance = distance_paris)
        assert len(added)>0
        fLOG ("nb added",len(added))
        with open(os.path.join(folder,"added.txt"),"w") as f : 
            f.write(str(added))
            
    def test_euler(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        folder = os.path.join(os.path.abspath(os.path.dirname(__file__)),"temp_rues_euler")
        if not os.path.exists(folder) : os.mkdir(folder)
        edges = get_data(whereTo=folder)
        
        data = pyensae.download_data("added.zip", whereTo=folder)
        with open(data[0],"r") as f : text = f.read()
        added_edges = eval(text)        
        path = euler_path(edges, added_edges)
        fLOG(len(path))
        fLOG(path[:5])
        fLOG(path[-5:])

if __name__ == "__main__"  :
    unittest.main ()    
