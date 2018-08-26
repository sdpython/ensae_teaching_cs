
.. _l-python_cplusplus:

Python et C++, stratégies
=========================

On n'utilise le `C/C++ <https://fr.wikipedia.org/wiki/C%2B%2B>`_ que dans le but
d'accélérer un programme Python. Il existe plusieurs façons de mélanger les deux
langages.

.. contents::
    :local:

CPython
+++++++

L'interpréteur `Python <https://github.com/python/cpython>`_ a toujours été écrit en C.
`CPython <https://fr.wikipedia.org/wiki/CPython>`_ est l'implémentation en C des modules standards autrefois écrits en Python.
CPython est aussi une machine virtuelle comme l'est Java. Les programmes Python sont compilés sous
forme `bytecode <https://docs.python.org/3/library/dis.html#dis.Bytecode>`_ (qu'il est possible d'analyser avec le module
`dis <https://docs.python.org/3/library/dis.html>`_) puis exécutés.

.. index:: ctypes

C++ et Python séparés avec ctypes
+++++++++++++++++++++++++++++++++

Le module `ctypes <https://docs.python.org/3.5/library/ctypes.html>`_ permet
d'utiliser une `librairie <https://en.wikipedia.org/wiki/Library_(computing)>`_
compilée séparément (`DLL <https://fr.wikipedia.org/wiki/Dynamic_Link_Library>`_ sous Windows).
Le programme Python déclare les fonctions
qu'il souhaite utiliser. Les interfaces sont souvent écrites en C.
C'est l'option choisie par la librairie
`XGBoost <https://github.com/dmlc/xgboost>`_.

La librairie C++ est compilée et expose des fonctions via une API C :
`c_api.h <https://github.com/dmlc/xgboost/blob/master/include/xgboost/c_api.h>`_.
Une fois la compilation terminée, il faut recopier la librairie
compilée (`instructions <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2016/2016-08-09_xgboost_again.html>`_).
Cette librairie est incluse dans le fichier
`setup.py <https://github.com/dmlc/xgboost/blob/master/python-package/setup.py>`_
lorsque celui-ci est *buildé*. Dans le code du package, la librairie
est chargé via la fonction `_load_lib <https://github.com/dmlc/xgboost/blob/master/python-package/xgboost/core.py#L101>`_.
Les méthodes de la DLL sont appelées comme elles le seraient dans un programme python.
Exemple avec la fonction `XGDMatrixCreateFromFile <https://github.com/dmlc/xgboost/blob/master/python-package/xgboost/core.py#L260>`_.

Il est préférable de connaître le C/C++ pour comprendre pourquoi les types Python et C sont
différentes ou encore ce que veut `ctypes.byref <https://docs.python.org/3.5/library/ctypes.html#ctypes.byref>`_.

.. inde:: cython

C++ avec Cython
+++++++++++++++

C'est l'option choisie par beaucoup de modules
tels que `scikit-learn <http://scikit-learn.org/stable/>`_.
C'est aussi la moins verbeuse et la plus accessible surtout
qu'il possible de s'interface facilement avec `numpy <http://scikit-learn.org/stable/>`_.

Les fichiers d'extension *pyd* déclarent les fonctions qui seront implémentées en Cythno.
Ils sont optionnels. Les fichiers d'extensions *pyx* implémentent des fonctions en Cython.
Exemple : `_utils.pyd <https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_utils.pxd>`_
et `_utils.pyx <https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/_utils.pyx>`_.
Ces fichiers sont toujours accompagnés d'instructions de compilation :
`tree/setup.py <https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/tree/setup.py>`_
et `setup.py <https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/setup.py>`_.

* `tutoriel <http://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html>`_
* `Cython et Numpy <http://cython.readthedocs.io/en/latest/src/tutorial/numpy.html>`_

Cython permet aussi d'écrire du code en allégeant la contrainte sur le
`GIL <https://en.wikipedia.org/wiki/Global_interpreter_lock>`_ ou *Global Interpreter Lock*.
Celui-ci impose l'exécution du langage sur un seul thread. Il faut savoir ce qu'on fait
quand on relâche cette contrainte mais c'est le seul moyen d'écrire un programme vraiment parallèle.

* `cython.parallel <http://cython.readthedocs.io/en/latest/src/userguide/parallelism.html?highlight=nogil>`_

Le langage Python effectue constamment plein de vérifications comme le fait qu'un indice soit en dehors d'une liste.
Cython permet d'écrire un code plus rapide mais moins sûr en esquivant ces contraintes :

* `directives de compilation <http://cython.readthedocs.io/en/latest/src/reference/compilation.html?highlight=boundscheck#compiler-directives>`_

Le plus simple pour commencer à se familiariser est d'utiliser la commande
magique `%%cython <http://cython.readthedocs.io/en/latest/src/quickstart/build.html#using-the-ipython-notebook>`_
qui effectue les opérations de compilation pour le programmeur.

.. index:: pybind11, boost_python, SWIG

Modules Python écrits en C
++++++++++++++++++++++++++

Il faut lire le tutoriel
`Extending Python with C or C++ <https://docs.python.org/3/extending/extending.html>_.
C'est la solution qui produit le code le plus efficace mais il faut constamment convertir des
données depuis Python vers C et réciproquement. Il faut aussi gérer soi-même le
`comptage des références <https://docs.python.org/3.6/c-api/refcounting.html?highlight=py_incref#reference-counting>`_
afin que le `garbage collector <https://fr.wikipedia.org/wiki/Ramasse-miettes_(informatique)>`_
garde la trace des objets créés et détruits.

Cette option est devenue moins intéressente avec les récents développement de Python.
Il faut citer deux outils qui permettent de faciliter l'habillage d'une librairie C en Python :

* `SWIG <http://www.swig.org/>`_
* `Boost Python <http://www.boost.org/doc/libs/1_62_0/libs/python/doc/html/index.html>`_
* `pybind11 <https://github.com/pybind/pybind11>`_

Compiler le langage Python
++++++++++++++++++++++++++

Le langage Python n'est pas compilable mais certains outils tentent de convertir un code
existant en C/C++ pour le compiler ensuite. Un des problèmes rencontrés est
l'`inférence de type <https://fr.wikipedia.org/wiki/Inf%C3%A9rence_de_types>`_ : la compilateur requiert
la connaissance du type d'une variable et celui n'est connu qu'à l'exécution.
Quelques outils :

* `llvmlite <https://llvmlite.readthedocs.io/en/latest/>`_
* `Nuitka <http://nuitka.net/>`_
* `Numba <http://numba.pydata.org/>`_
* `PyPy <http://pypy.org/>`_
* `Pyston <https://github.com/dropbox/pyston>`_

Tous repose sur un mécanisme appelé `JIT <https://fr.wikipedia.org/wiki/Compilation_%C3%A0_la_vol%C3%A9e>`_
ou *compilation à la volée*.

.. index:: cpyquickhelper

Un exemple
++++++++++

Le module `cpyquickhelper <https://github.com/sdpython/cpyquickhelper/>`_
implémente quelques façons de mettre du C
dans un module :epkg:`Python` et contient
toutes les instructions pour en faire un module
compilé et prêt à l'emploi.
