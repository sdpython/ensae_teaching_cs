"""
@brief      test log(time=10s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from ensae_teaching_cs.special.geometry_point import GeometryPoint
from ensae_teaching_cs.special.geometry_segment import GeometrySegment
from ensae_teaching_cs.special.geometry_polygone import GeometryPolygone


class TestGeometry(ExtTestCase):

    def test_geometry_point(self):
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
        middle = GeometryPoint(GeometryPoint(0.5, 0.1))
        poly = GeometryPolygone([GeometryPoint(0, 0), GeometryPoint(1, 0),
                                 GeometryPoint(1, 1), GeometryPoint(0, 1)])
        r = poly.in_convex(middle)
        self.assertNotEmpty(r)
        out = GeometryPoint(0.5, -0.1)
        r = poly.in_convex(out)
        self.assertFalse(r)

    def test_geometry_polygone2(self):
        poly = GeometryPolygone([GeometryPoint(0, 0), GeometryPoint(0, 1),
                                 GeometryPoint(1, 1), GeometryPoint(1, 0)])
        convex = poly.convex()
        self.assertEqual(len(convex), len(poly))
        r = [GeometryPoint(0, 1), GeometryPoint(0, 0),
             GeometryPoint(1, 0), GeometryPoint(1, 1)]
        for p, e in zip(convex, r):
            self.assertEqual(p, e)


if __name__ == "__main__":
    unittest.main()
