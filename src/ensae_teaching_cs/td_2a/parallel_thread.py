#-*- coding: utf-8 -*-
"""
Ce fichier contient un exemple qui permet d'exécuter plusieurs threads.
"""

import threading
import time


class ParallelThread (threading.Thread):

    """
    Cette classe implémente un thread qui exécute en boucle une fonction
    sur tous les éléments d'une liste.
    """

    def __init__(self, f, list_of_params):
        """
        Constructeur

        @param      f                   fonction à exécuter
        @param      list_of_params      liste des paramètres à exécuter
        """
        threading.Thread.__init__(self)
        self.f2run = f
        self.results = None
        self.list_of_params = list_of_params

    def run(self):
        """
        Appelle une fonction plusieurs sur tous les paramètres dans une liste.
        """
        self.results = []
        for params in self.list_of_params:
            l, p = (params, {}) if len(params) else params
            self.results.append(self.f2run(*l, **p))

    @staticmethod
    def parallel(f,
                 list_of_params,
                 nbthread=2,
                 wait=True,
                 daemon=True,
                 delay_sec=1):
        """
        Parallélise l'appel à la fonction ``f``
        sur une liste de paramètres.

        @param      f                   fonction à appeler sur chacun des paramètres de la liste
        @param      list_of_params      liste des paramètres
        @param      nbthread            nombre de threads
        @param      wait                attendre pour la fin
        @param      daemon              voir `daemon <https://docs.python.org/3.4/library/threading.html#threading.Thread.daemon>`_
        @param      delay_sec           la fonction inclut une boucle qui attend les threads, elle vérifie cela toutes ``delay_sec`` secondes
        """
        th = []
        split = [list_of_params[i::nbthread] for i in range(nbthread)]
        for spl in split:
            t = ParallelThread(f, spl)
            t.daemon = daemon
            th.append(t)
            t.start()

        if wait:
            waits = th.copy()
            nb = len(waits)
            while len(waits) > 0:
                waits = [t for t in th if t.is_alive()]
                if len(waits) > 0:
                    time.sleep(delay_sec)
            final = [None for i in range(len(list_of_params))]
            for i in range(nbthread):
                final[i::nbthread] = th[i].results
            return final
        else:
            return th

if __name__ == "__main__":
    import numpy

    def inv(m):
        return numpy.linalg.inv(m)

    nps = [[numpy.random.random((5, 5))] for i in range(0, 1000)]
    mm = ParallelThread.parallel(inv, nps, 10)
    print(len(mm))
