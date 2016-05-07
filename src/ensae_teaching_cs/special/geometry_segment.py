"""
@file
@brief Defines a segment
"""

from .geometry_point import GeometryPoint, GeometryException


class GeometrySegment (object):
    """
    two points
    """
    __slots__ = ["_a", "_b"]

    def __init__(self, a, b):
        """
        constructor
        @param      a       first extremity
        @param      b       second extremity
        """
        if len(a) != len(b):
            raise GeometryException(
                "extremities don't share the same dimension")
        self._a = a
        self._b = b

    def __eq__(self, x):
        """
        equal
        """
        return (self._a == x._a and self._b == x._b) or \
               (self._b == x._a and self._a == x._b)

    def __neq__(self, x):
        """
        different
        """
        return not self.__eq__(x)

    def __len__(self):
        """
        dimension
        """
        return len(self._a)

    def __str__(self):
        """
        usual
        """
        return "%s --> %s" % (str(self._a), str(self._b))

    def __imul__(self, k):
        """
        multiplication
        """
        self._a *= k
        self._b *= k
        return self

    def vector(self):
        """
        @return the directional vector
        """
        return self._b - self._a

    def equation(self):
        """
        dimension 2 only

        @return a,b,c : ax + by +c
        """
        if len(self) != 2:
            raise GeometryException(
                "only able to define an equation in dimension 2")
        vec = self.vector()
        a = vec._x[1]
        b = -vec._x[0]
        c = - a * self._a._x[0] - b * self._a._x[1]
        return a, b, c

    def equation_eval(self, x):
        """
        @return the evaluation of the equation
        """
        a, b, c = self.equation()
        return x.scalar(GeometryPoint(a, b)) + c

    def norm2(self):
        """
        @return the norm2
        """
        v = self.vector()
        return v.scalar(v)

    def reverse(self):
        """
        switch extremities
        """
        x = self._a
        self._a = self._b
        self._b = x

    def topdown(self):
        """
        the vector only points in the same semi-plan
        """
        if self._a > self._b:
            self.reverse()
