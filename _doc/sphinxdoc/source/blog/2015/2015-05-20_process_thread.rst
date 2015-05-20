
.. blogpost::
    :title: Utilisation des threads et des process
    :keywords: thread, process, parallelized, parallel cmoputing
    :date: 2015-05-20
    :categories: distributed
    
    Le langage Python n'offre qu'un seul fil d'exécution.
    et il n'est pas possible d'utiliser tous les coeurs d'un processeur
    avec juste des threads. Il faut donc passer pas des processus.
    Seulement, comme les processus ne partagent pas la mémoire,
    il est plus compliqué d'échanger des informations entre eux,
    en particulier la sortie standard. Le programme suivant 
    n'affiche rien malgré le ``print``. ::
    
        from multiprocessing import Process
        def f(name):
            print('hello', name)

        p = Process(target=f, args=('bob',))
        p.start()
        p.join()
        
    Pour communiquer entre deux processus, il faut utiliser 
    un objet 
    `Queue <https://docs.python.org/3.4/library/multiprocessing.html#exchanging-objects-between-processes>`_
    comme ceci par exemple ::

        from multiprocessing import Process, Queue
        import sys

        def f(name, q):
            q.put([name])

        if __name__ == '__main__':
            q = Queue()
            p = Process(target=f, args=('bob',q))
            p.start()
            p.join()   
            print(q.get())  # affiche ['bob']
            
            
    On voudrait pouvoir échanger tout et n'importe quoi de cette façon.
    Là encore, tout n'est pas possible, c'est pourquoi on peut 
    tomber sur l'exception ::

        Traceback (most recent call last):
          File "u.py", line 10, in <module>
            p.start()
          File "C:\Python34_x64\lib\multiprocessing\process.py", line 105, in start
            self._popen = self._Popen(self)
          File "C:\Python34_x64\lib\multiprocessing\context.py", line 212, in _Popen
            return _default_context.get_context().Process._Popen(process_obj)
          File "C:\Python34_x64\lib\multiprocessing\context.py", line 313, in _Popen
            return Popen(process_obj)
          File "C:\Python34_x64\lib\multiprocessing\popen_spawn_win32.py", line 66, in __init__
            reduction.dump(process_obj, to_child)
          File "C:\Python34_x64\lib\multiprocessing\reduction.py", line 59, in dump
            ForkingPickler(file, protocol).dump(obj)
        TypeError: cannot serialize '_io.TextIOWrapper' object
        
    .. index:: sérialisation, sérialisable
        
    Cela dit qu'une information n'est pas *sérialisable* : comme les processsus ne partage pas
    la mémoire, les informations sont recopiées. Il faut donc pouvoir convertir un objet
    en une séquence contiguë d'octets. Le processus recevant l'information
    fera la conversion inverse. C'est la sérialisation.
    Elle est implicite pour tous les types standards (ou une composition de ceux-ci).
    C'est le module `pickle <https://docs.python.org/3.4/library/pickle.html#module-pickle>`_ qui
    s'en occupe.
    Quand elle ne fonctionne pas (typiquement si un objet contient un `stream
    <https://docs.python.org/3/glossary.html#term-file-object>`_),
    il faut la définir soi-même au travers 
    de `__getstate__ <https://docs.python.org/3.4/library/pickle.html#object.__getstate__>`_
    et `__setstate__ <https://docs.python.org/3.4/library/pickle.html#object.__setstate__>`_.
    
    Voir également :
    
    * `An introduction to parallel programming <http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html>`_
    * `joblib <http://pythonhosted.org/joblib/>`_
    * `Using IPython for parallel computing <http://ipython.org/ipython-doc/dev/parallel/>`_
    