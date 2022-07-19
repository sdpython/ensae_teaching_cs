# -*- coding: utf-8 -*-
"""
@file
@brief Implements "homomorphic number".
"""
import random


class HomomorphicInt:
    """
    Implements an "homomorphic integer".
    See `Homomorphic encryption
    <https://en.wikipedia.org/wiki/Homomorphic_encryption>`_.
    """
    __slots__ = ['V', 'N', 'P', 'Q', 'E']

    @staticmethod
    def pgcd(a, b):
        """
        Computes the :epkg:`PGCD`.
        """
        while a != b:
            d = abs(a - b)
            c = min(a, b)
            a, b = d, c
        return a

    @staticmethod
    def lcm(a, b):
        """
        Computes the least common multiple
        (:epkg:`PPCM`).
        """
        p = HomomorphicInt.pgcd(a, b)
        return a * b // p

    @staticmethod
    def find_e(p, q):
        """
        Finds one exposant for the :epkg:`RSA` encryption.
        """
        c = HomomorphicInt.pgcd(p - 1, q - 1)
        qn = (p - 1) * (q - 1) // c
        i = 0
        while True:
            h = random.randint(2, qn - 1)
            pg = HomomorphicInt.pgcd(h, qn)
            if pg == 1:
                e = HomomorphicInt(h, (p - 1) // c, q - 1, (h, h))
                try:
                    ei = e.inv().V
                except ZeroDivisionError:
                    i += 1
                    continue
                h2 = random.randint(2, p * q - 1)
                e2 = HomomorphicInt(h2, p, q, (h2, h2))
                try:
                    ei2 = e2.inv().V
                except ZeroDivisionError:
                    i += 1
                    continue
                return (h, ei, h2, ei2)
            i += 1
            if i > 100:
                raise ValueError(
                    "Unable to find a number prime with (p-1)(q-1).")

    def __init__(self, value, p=673, q=821, e=None):
        """
        @param  value   initial value
        @param  p       p for RSA
        @param  q       q for RSA
        @param  e       e for RSA (e, and inverse e)

        Other prime numbers can be found at
        `The First 100,008 Primes <https://primes.utm.edu/lists/small/100000.txt>`_.
        """
        self.N = p * q
        self.P = p
        self.Q = q
        if self.N <= 2:
            raise ValueError("p*q must be > 2")
        self.V = value % self.N
        if e is None:
            self.E = HomomorphicInt.find_e(self.P, self.Q)
        elif not isinstance(e, tuple):
            raise TypeError("e must a tuple.")
        else:
            self.E = e

    def new_int(self, v):
        """
        Returns a @see cl HomomorphicInt with the same encrypted parameters.
        """
        return HomomorphicInt(v, self.P, self.Q, self.E)

    def __repr__(self):
        """
        Usual
        """
        return f'HomomorphicInt({self.V},{self.P},{self.Q},{self.E})'.replace(" ", "")

    def __pow__(self, n):
        """
        Power operator.
        """
        if n == 0:
            return HomomorphicInt(1, self.P, self.Q, self.E)
        s = self.V
        while n > 1:
            s *= self.V
            s %= self.N
            n -= 1
        return HomomorphicInt(s, self.P, self.Q, self.E)

    def __add__(self, o):
        """
        Addition.
        """
        if self.N != o.N:
            raise ValueError(f"{self.N} != {o.N}")
        return HomomorphicInt(self.V + o.V, self.P, self.Q, self.E)

    def __sub__(self, o):
        """
        Soustraction.
        """
        if self.N != o.N:
            raise ValueError(f"{self.N} != {o.N}")
        return HomomorphicInt(self.V - o.V, self.P, self.Q, self.E)

    def __mul__(self, o):
        """
        Multiplication.
        """
        if self.N != o.N:
            raise ValueError(f"{self.N} != {o.N}")
        return HomomorphicInt(self.V * o.V, self.P, self.Q, self.E)

    def inv(self):
        """
        Inversion. This only works in all cases if *n* is a prime number.
        We use :math:`a^{-1} \\equiv a^{n-2} \\mod n`.
        The implementation can be improved (use binary decomposition) and cached.
        """
        s = self.V
        for i in range(1, self.N - 2):
            s *= self.V
            s %= self.N
            if ((self.V * i) % self.N) == 1:
                return HomomorphicInt(i, self.P, self.Q, self.E)
        if ((s * self.V) % self.N) != 1:
            raise ZeroDivisionError(
                f"Inverse of {self.V} does not exist.")
        return HomomorphicInt(s, self.P, self.Q, self.E)

    def __div__(self, o):
        """
        Division, implies to find the inverse (so very costly).
        """
        if self.N != o.N:
            raise ValueError(f"{self.N} != {o.N}")
        i = o.inv()
        return HomomorphicInt(self.V * i.V, self.P, self.Q, self.E)

    def crypt_mult(self):
        """
        Crypt a number and preserve multiplication.
        We use `RSA <https://fr.wikipedia.org/wiki/Chiffrement_RSA>`_.
        """
        return self ** self.E[0]

    def decrypt_mult(self):
        """
        Decrypt a number and preserve multiplication.
        """
        return self ** self.E[1]

    def crypt_add(self):
        """
        Simple permutation.
        """
        return HomomorphicInt(self.V * self.E[2], self.P, self.Q, self.E)

    def decrypt_add(self):
        """
        Decrypt a number and preserve multiplication.
        """
        return HomomorphicInt(self.V * self.E[3], self.P, self.Q, self.E)
