
.. |pyecopng| image:: ../_static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: ../_static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pystatpng|

.. _l-2a-cplusplus-para-serie:
.. _l-acc-code-llvm:

C++, Accélération de code
+++++++++++++++++++++++++

.. toctree::
    :maxdepth: 1

    ../notebooks/python_r
    ../notebooks/python_csharp
    ../notebooks/cffi_linear_regression

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_langages

*Lectures*

* :ref:`l-python_cplusplus`
* `sklearn-compiledtrees <https://github.com/ajtulloch/sklearn-compiledtrees/>`_ :
  création d'une implémentation C++ de la fonction de décision d'un arbre de décision entraîné avec
  scikit-learn
* `Just-in-time compilation <https://en.wikipedia.org/wiki/Just-in-time_compilation>`_

*Vidéos*

* `Making your code faster: Cython and parallel processing in the Jupyter Notebook <https://www.youtube.com/watch?v=MiHddLYZ6cQ>`_

*Modules*

* `cffi <https://cffi.readthedocs.io/en/latest/>`_
* `ctypes <https://docs.python.org/3/library/ctypes.html>`_
* `boost_python <http://www.boost.org/doc/libs/1_63_0/libs/python/doc/html/index.html>`_
* `pybind11 <https://github.com/pybind/pybind11/>`_
* `swig <http://www.swig.org/>`_
* `numba <https://numba.pydata.org/>`_ :
  JIT, compilation à la volée de certaines parties d'un code
* `nuitka <http://nuitka.net/>`_ :
  compilation d'un programme python ou d'un module
  (essaye de convertir un programe python en C)
* `pypy <https://pypy.org/>`_ :
  compilation d'un programme python ou d'un module
  (essaye de convertir un programe python en C)
* `cython <http://cython.org/>`_ :
  pseudo C (un mix entre C et Python), solution adoptée par scikit-learn

*Plus expérimental*

* `pythran <https://pythonhosted.org/pythran/>`_ : conversion de code python
  en C++ et compilation
* `pyston <https://github.com/dropbox/pyston>`_ (Python 2.7 seulement) :
  réécriture de l'interpréteur Python pour être plus rapide.
