"""
@brief      test log(time=10s)
"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from ensae_teaching_cs.special.geometry_point import GeometryPoint
from ensae_teaching_cs.special.geometry_segment import GeometrySegment
from ensae_teaching_cs.special.geometry_polygone import GeometryPolygone


class TestGeometry(unittest.TestCase):

    def test_geometry_point(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        p = GeometryPoint(4, 5)
        p += p
        self.assertEqual(p, (8, 10))
        p -= p
        self.assertEqual(p, (0, 0))
        p2 = GeometryPoint(4, 5) + GeometryPoint(1, 1)
        self.assertEqual(p2, (5, 6))
        norm = p2.norm2()
        seg = GeometrySegment(p, p2)
        norms = seg.norm2()
        self.assertEqual(norms, norm)

    def test_geometry_polygone(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        middle = GeometryPoint(GeometryPoint(0.5, 0.1))

        poly = GeometryPolygone([GeometryPoint(0, 0), GeometryPoint(1, 0),
                                 GeometryPoint(1, 1), GeometryPoint(0, 1)])
        r = poly.in_convex(middle)
        assert r
        out = GeometryPoint(0.5, -0.1)
        r = poly.in_convex(out)
        assert not r

    def test_geometry_polygone2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        poly = GeometryPolygone([GeometryPoint(0, 0), GeometryPoint(0, 1),
                                 GeometryPoint(1, 1), GeometryPoint(1, 0)])
        convex = poly.convex()
        fLOG(convex)
        self.assertEqual(len(convex), len(poly))
        r = [GeometryPoint(0, 1), GeometryPoint(
            0, 0), GeometryPoint(1, 0), GeometryPoint(1, 1)]
        for p, e in zip(convex, r):
            self.assertEqual(p, e)


if __name__ == "__main__":
    unittest.main()
