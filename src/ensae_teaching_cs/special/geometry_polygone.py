"""
@file
@brief defines a polyline
"""

import copy
from .geometry_point import GeometryException
from .geometry_segment import GeometrySegment


class GeometryPolygone (list):
    """
    A sequence of point, the last one is connected to the first one.
    """

    def barycentre(self):
        """
        @return the barycentre
        """
        if len(self) == 0:
            raise GeometryException("no point")
        r = copy.copy(self[0])
        for i in range(1, len(self)):
            r += self[i]
        return r * (1. / float(len(self)))

    def circle(self):
        """
        @return a list of points ordered by angle taken to the barycenter (works only dimension 2)
        """
        bary = self.barycentre()
        prod = [((p - bary).angle(), p) for p in self]
        prod.sort()
        return GeometryPolygone([p[1] for p in prod])

    def convex(self):
        """
        @return the convex envelop

        only in 2 dimensions right now
        """
        cir = self.circle()
        mod = True
        while mod:
            mod = False
            r = None
            n = len(cir)
            for i in range(2, n):
                a = cir[i - 1] - cir[i - 2]
                b = cir[i] - cir[i - 1]
                s = a.product(b)
                if s > 0:
                    r = i - 1
                    mod = True
                    break

            if not mod:
                for i in range(n, n + 2):
                    a = cir[(i - 1) % n] - cir[(i - 2) % n]
                    b = cir[i % n] - cir[(i - 1) % n]
                    s = a.product(b)
                    if s > 0:
                        mod = True
                        r = (i - 1) % len(n)
                        break

            if mod:
                del cir[r]

        return cir

    def in_convex(self, p):
        """
        we assume the polygone is convex and the result of function convex (points sorted by angle
        we check then if a point p belongs to the envelop (only 2-dimension)

        @param      p       point
        @return             boolean
        """
        res = None
        for i in range(1, len(self)):
            s = GeometrySegment(self[i - 1], self[i])
            t = s.equation_eval(p)
            if t == 0:
                continue
            r = 1 if t > 0 else -1
            if res is None:
                res = r
            elif res != r:
                return False
        return True
