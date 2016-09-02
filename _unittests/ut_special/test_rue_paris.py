"""
@brief      test log(time=25s)

"""
import os
import sys
import unittest

try:
    import src
    import pyquickhelper as skip_
    import pyensae as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from pyensae.datasource import download_data
from src.ensae_teaching_cs.special.rues_paris import get_data, bellman, kruskal, possible_edges, eulerien_extension, distance_paris, euler_path, connected_components, distance_haversine, graph_degree


class TestRueParis (unittest.TestCase):

    def test_get_data(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_rues")
        if not os.path.exists(folder):
            os.mkdir(folder)
        for ext in [".txt", ".zip"]:
            f = os.path.join(folder, "paris_54000" + ext)
            if os.path.exists(f):
                os.remove(f)
        try:
            data = get_data(whereTo=folder, fLOG=fLOG, timeout=60)
        except Exception as e:
            if "unable to retrieve data" in str(e):
                return
            else:
                raise Exception("*****" + str(e) + "*****") from e

        fLOG(len(data))
        assert len(data) > 0
        total = sum(_[-1] for _ in data)
        fLOG("total length", total)

    def test_algo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder, fLOG=fLOG)
        edges = edges[:1000]
        max_segment = max(e[-1] for e in edges)
        possibles = possible_edges(edges, max_segment / 8, fLOG=fLOG)
        init = bellman(edges, fLOG=fLOG, allow=lambda e: e in possibles)
        fLOG("---")
        init = bellman(
            edges,
            fLOG=fLOG,
            allow=lambda e: e in possibles,
            init=init)
        fLOG("---")
        added = kruskal(edges, init, fLOG=fLOG)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        fLOG("degrees", allow)
        allow = set(allow)
        fLOG("---")
        init = bellman(edges, fLOG=fLOG,
                       allow=lambda e: e in possibles or e[
                           0] in allow or e[1] in allow,
                       init=init)
        fLOG("---")
        added = kruskal(edges, init, fLOG=fLOG)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        fLOG("degrees", allow)

    def test_algo2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo2")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder, fLOG=fLOG)
        edges = edges[:1000]
        added = eulerien_extension(edges, fLOG=fLOG, alpha=1 / 8)
        assert len(added) > 0
        fLOG("nb added", len(added))

    def test_algo3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        return
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo3")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder, fLOG=fLOG)
        fLOG("start")
        added = eulerien_extension(edges, fLOG=fLOG, distance=distance_paris)
        assert len(added) > 0
        fLOG("nb added", len(added))
        with open(os.path.join(folder, "added.txt"), "w") as f:
            f.write(str(added))

    def test_euler(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_rues_euler")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder, fLOG=fLOG)

        data = download_data("added.zip", whereTo=folder, fLOG=fLOG)
        with open(data[0], "r") as f:
            text = f.read()
        added_edges = eval(text)
        path = euler_path(edges, added_edges)
        fLOG(len(path), len(edges) + len(added_edges))
        for p in path[:5]:
            fLOG(len(p), p)
        for p in path[-5:]:
            fLOG(len(p), p)

    def test_algo_euler4(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo_euler4")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder, fLOG=fLOG)
        edges = edges[:3]

        vertices = {}
        for e in edges:
            for i in range(0, 2):
                _ = e[i]
                p = e[i + 3]
                vertices[_] = p

        connex = connected_components(edges)
        v = [v for k, v in connex.items()]
        mi, ma = min(v), max(v)

        while mi != ma:
            edges.append((mi, ma, 2, vertices[mi], vertices[ma],
                          distance_haversine(* (vertices[mi] + vertices[ma]))))

            connex = connected_components(edges)
            v = [v for k, v in connex.items()]
            mi, ma = min(v), max(v)

        if __name__ == "__main__":
            import matplotlib.pyplot as plt
            import networkx as nx
            plt.figure()
            G = nx.Graph()
            for e in edges:
                a, b = e[:2]
                G.add_edge(a, b)
            pos = nx.spring_layout(G)
            nx.draw(G, pos, node_color='#A0CBE2')
            plt.savefig(os.path.join(folder, "graph1.png"))
            plt.close('all')

        added = eulerien_extension(edges, fLOG=lambda *l: None,
                                   distance=distance_paris)

        if __name__ == "__main__":
            for e in added:
                a, b = e[:2]
                G.add_edge(a, b)
            plt.figure()
            pos = nx.spring_layout(G)
            graph_degree(edges + added)
            #labels={ v:"{0}".format(deg[v]) for v in G.nodes() }
            nx.draw(G, pos, node_color='#A0CBE2'  # ,labels=labels
                    )
            plt.savefig(os.path.join(folder, "graph2.png"))
            plt.close('all')

        path = euler_path(edges, added)
        all = edges + added
        fLOG(len(all), len(path))
        #assert len(all) == len(path)


if __name__ == "__main__":
    unittest.main()
