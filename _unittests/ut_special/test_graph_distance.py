"""
@brief      test log(time=2s)

"""
import os
import sys
import unittest
import copy


try:
    import src
    import pyquickhelper as skip_
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
    import src
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.special.graph_distance import GraphDistance
from src.ensae_teaching_cs.helpers.graphviz_helper import draw_graph_graphviz


class TestGraphDistance(unittest.TestCase):

    def test_graph_load(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        this = os.path.abspath(os.path.dirname(__file__))
        graph = os.path.join(this, "data", "graph.gv")
        g = GraphDistance.load_from_file(graph, False)
        paths = list(g.enumerate_all_paths(True))
        assert len(paths) > 0

    def test_image_video_kohonen(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_graph_distance")

        graph1 = [("a", "b"), ("b", "c"), ("b", "d"), ("d", "e"),
                  ("e", "f"), ("b", "f"), ("b", "g"), ("f", "g"),
                  ("a", "g"), ("a", "g"), ("c", "d"), ("d", "g"),
                  ("d", "h"), ("aa", "h"), ("aa", "c"), ("f", "h"), ]
        graph2 = copy.deepcopy(graph1) + \
            [("h", "m"), ("m", "l"), ("l", "C"), ("C", "r"),
             ("a", "k"), ("k", "l"), ("k", "C"),
             ]

        graph1 = GraphDistance(graph1)
        graph2 = GraphDistance(graph2)

        graph2["C"].label = "c"
        store = {}
        if len(list(graph1.enumerate_all_paths(True))) != 17:
            raise Exception("expecting 17 here")
        if len(list(graph2.enumerate_all_paths(True))) != 19:
            raise Exception("expecting 19 here")

        distance, graph = graph1.distance_matching_graphs_paths(graph2,
                                                                use_min=False, store=store)

        if graph["h"].Label != "h":
            raise Exception("we expect this node to be merged in the process")

        if distance is None:
            raise Exception("expecting something different from None")

        outfile1 = os.path.join(temp, "unittest_GraphDistance4_sub1.png")
        outfile2 = os.path.join(temp, "unittest_GraphDistance4_sub2.png")
        outfilef = os.path.join(temp, "unittest_GraphDistance4_subf.png")

        vertices, edges = graph1.draw_vertices_edges()
        draw_graph_graphviz(vertices, edges, outfile1)

        vertices, edges = graph2.draw_vertices_edges()
        draw_graph_graphviz(vertices, edges, outfile2)
        assert os.path.exists(outfile2)

        vertices, edges = graph.draw_vertices_edges()
        draw_graph_graphviz(vertices, edges, outfilef)
        assert os.path.exists(outfilef)

    def test_unittest_GraphDistance2(self):
        graph1 = [("a", "b"), ("b", "c"), ("b", "X"), ("X", "c"),
                  ("c", "d"), ("d", "e"), ("0", "b")]
        graph2 = [("a", "b"), ("b", "c"), ("b", "X"), ("X", "c"),
                  ("c", "t"), ("t", "d"), ("d", "e"), ("d", "g")]
        graph1 = GraphDistance(graph1)
        graph2 = GraphDistance(graph2)
        store = {}
        distance, graph = graph1.distance_matching_graphs_paths(graph2,
                                                                use_min=False, store=store)
        if distance is None:
            raise TypeError("expecting something different from None")
        allPaths = list(graph.enumerate_all_paths(True))
        if len(allPaths) == 0:
            raise ValueError("the number of paths should not be null")
        if distance == 0:
            raise ValueError("expecting a distance > 0")
        vertices, edges = graph.draw_vertices_edges()
        #GV.drawGraphEdgesVertices (vertices,edges, "unittest_GraphDistance2.png")
        node = graph.vertices["X"]
        if None in node.pair:
            raise RuntimeError(
                "unexpected, this node should be part of the common set")

        if False:
            print("distance", distance)
            for k, v in store.items():
                print(k, len(v))
                for _ in v:
                    print("  ", _)

        vertices, edges = graph1.draw_vertices_edges()
        #GV.drawGraphEdgesVertices (vertices,edges, "unittest_GraphDistance2_sub1.png")
        vertices, edges = graph2.draw_vertices_edges()
        #GV.drawGraphEdgesVertices (vertices,edges, "unittest_GraphDistance2_sub2.png")


if __name__ == "__main__":
    unittest.main()
