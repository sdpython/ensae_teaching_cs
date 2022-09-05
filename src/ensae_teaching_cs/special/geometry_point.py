"""
@file
@brief  Defines a point in N-dimension
"""

import math


class GeometryException(Exception):
    """
    raises when an issue arises with class GeometryPoint
    """
    pass


class GeometryPoint:
    """
    one point
    """
    __slots__ = ["_x"]

    def __init__(self, *x):
        """
        @param      x       is a vector
        """
        if isinstance(x, (tuple, list)):
            if len(x) == 0:
                raise ValueError("empty dimension")
            if isinstance(x[0], GeometryPoint) and len(x) == 1:
                self._x = x[0]._x
            else:
                self._x = tuple(x)
        else:
            raise TypeError(f"Unexpected type {type(x)!r}.")

    def __eq__(self, x):
        """
        is equal
        """
        return self._x == x

    def __neq__(self, x):
        """
        is different
        """
        return not self.__eq__(x)

    def __len__(self):
        """
        returns the dimension
        """
        return len(self._x)

    def __str__(self):
        """
        converts into string
        """
        if len(self) == 2:
            s = "({0},{1})".format(*self._x)
            return s.replace(".000000", "")

        format = ", ".join(["{}" for _ in self._x])
        t = format.format(*self._x)
        s = f"({t})"
        return s.replace(".000000", "")

    def __repr__(self):
        """
        ``eval(__repr__)`` should return the same object
        """
        return f"GeometryPoint({', '.join(str(_) for _ in self._x)})"

    def __iadd__(self, x):
        """
        addition
        """
        if len(self) != len(x):
            raise GeometryException(
                f"dimension problem {len(self)} != {len(x)}")
        if len(self) == 2:
            self._x = (self._x[0] + x._x[0], self._x[1] + x._x[1])
        else:
            self._x = tuple(a + b for a, b in zip(self._x, x._x))
        return self

    def __add__(self, x):
        """
        addition
        """
        if len(self) != len(x):
            raise GeometryException(
                f"dimension problem {len(self)} != {len(x)}")
        if len(self) == 2:
            return GeometryPoint(self._x[0] + x._x[0], self._x[1] + x._x[1])
        else:
            return GeometryPoint(a + b for a, b in zip(self._x, x._x))

    def __sub__(self, x):
        """
        substraction
        """
        if len(self) != len(x):
            raise GeometryException(
                f"dimension problem {len(self)} != {len(x)}")
        if len(self) == 2:
            return GeometryPoint(self._x[0] - x._x[0], self._x[1] - x._x[1])
        return GeometryPoint(a - b for a, b in zip(self._x, x._x))

    def __imul__(self, k):
        """
        multiplication by a scalar
        """
        if len(self) == 2:
            self._x = (self._x[0] * k, self._x[1] * k)
        else:
            self._x = tuple(_ * k for _ in self._x)
        return self

    def __mul__(self, k):
        """
        multiplication by a scalar
        """
        if len(self) == 2:
            return GeometryPoint(self._x[0] * k, self._x[1] * k)
        else:
            return GeometryPoint(_ * k for _ in self._x)

    def scalar(self, x):
        """
        scalar product
        """
        if len(self) != len(x):
            raise GeometryException("dimension problem %d != %d\n%s ? %s" % (len(self), len(x),
                                                                             str(self), str(x)))
        r = 0.
        for a, b in zip(self._x, x._x):
            r += a * b
        return r

    def __cmp__(self, x):
        """
        comparison
        """
        if len(self) != len(x):
            raise GeometryException(
                f"dimension problem {len(self)} != {len(x)}")
        for a, b in zip(self._x, x._x):
            t = -1 if a < b else (0 if a == b else 1)
            if t != 0:
                return t
        return 0

    def __lt__(self, x):
        """
        inferior
        """
        return self.__cmp__(x) == -1

    def product(self, x):
        """
        vectoriel product, dimension 2 only
        """
        if len(self) != 2:
            raise GeometryException(
                "this function only exists if len(self) == 2")

        return self._x[1] * x._x[0] - self._x[0] * x._x[1]

    def cossin(self):
        """
        return the cos, sin of a vector (dimension 2 only)
        """
        n = self.norm2()
        if n == 0.:
            return 1., 0.
        n = n ** 0.5
        p = GeometryPoint(1., 0.)
        cos = self.scalar(p) / n
        sin = self.product(p) / n
        return cos, sin

    def norm2(self):
        """
        return the norm
        """
        return self.scalar(self)

    def angle(self):
        """
        return the angle
        """
        cos, sin = self.cossin()
        if cos == 0:
            if sin == 0:
                return 0
            elif sin > 0:
                return math.pi / 2
            else:
                return -math.pi / 2
        else:
            t = sin / cos
            a = math.atan(t)
            if cos < 0:
                return a - math.pi
            else:
                return a
