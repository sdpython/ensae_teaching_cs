"""
@brief      test log(time=25s)
"""
import os
import unittest
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, ExtTestCase
from pyensae.datasource import download_data
from ensae_teaching_cs.special.rues_paris import (
    get_data, bellman, kruskal, possible_edges, distance_haversine,
    graph_degree)
from ensae_teaching_cs.special.rues_paris import (
    eulerien_extension, distance_paris, euler_path,
    connected_components)


class TestRueParis(ExtTestCase):

    def test_get_data(self):
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
            data = get_data(whereTo=folder, timeout=60)
        except Exception as e:
            if "unable to retrieve data" in str(e):
                return
            else:
                raise AssertionError("*****" + str(e) + "*****") from e

        assert len(data) > 0
        total = sum(_[-1] for _ in data)
        self.assertGreater(total, 0)

    def test_algo(self):
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder)
        edges = edges[:1000]
        max_segment = max(e[-1] for e in edges)
        possibles = possible_edges(edges, max_segment / 8)
        init = bellman(edges, allow=lambda e: e in possibles)
        init = bellman(
            edges,
            allow=lambda e: e in possibles,
            init=init)
        added = kruskal(edges, init)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        allow = set(allow)
        init = bellman(edges,
                       allow=lambda e: e in possibles or e[
                           0] in allow or e[1] in allow,
                       init=init)
        added = kruskal(edges, init)
        d = graph_degree(edges + added)
        allow = sorted([k for k, v in d.items() if v % 2 == 1])
        self.assertEmpty(list(allow))

    def test_algo2(self):
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo2")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder)
        edges = edges[:1000]
        added = eulerien_extension(edges, alpha=1 / 8)
        assert len(added) > 0

    def test_euler(self):
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_rues_euler")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder)

        data = download_data("added.zip", whereTo=folder)
        with open(data[0], "r") as f:
            text = f.read()
        added_edges = eval(text)
        path = euler_path(edges, added_edges)
        self.assertNotEmpty(path)

    def test_algo_euler4(self):
        folder = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)),
            "temp_algo_euler4")
        if not os.path.exists(folder):
            os.mkdir(folder)
        edges = get_data(whereTo=folder)
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

        fix_tkinter_issues_virtualenv()
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

        added = eulerien_extension(edges, fLOG=lambda *l_: None,
                                   distance=distance_paris)

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
        alls = edges + added
        self.assertEqual(len(alls), len(path))


if __name__ == "__main__":
    unittest.main(verbosity=2)
