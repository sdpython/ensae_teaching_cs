
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Array, Matrix
+++++++++++++

.. index:: array, matrix

Le langage :epkg:`Python` est trop lent pour écrire des algorithmes
d'optimisation seulement dans ce langage. Le compromis trouvé
par le langage fut de rendre accessibles en :epkg:`Python`
des librairies rapides et codées en :epkg:`C++`, voire en :epkg:`fortran`.
Une grande partie des algorithmes s'appuient sur le calcul
matriciel et ce que propose la librairies :epkg:`numpy`.
Pour que cela fonctionne, il faut transvaser
les données depuis le :epkg:`Python` dans un structure de données
propre à :epkg:`numpy` : ce sont les :epkg:`array`.
Le machine learning commence bien souvent par convertir les données
en :epkg:`array` et à les manipuler sous cette forme.
Pour simplifier, avec :epkg:`numpy`, le code
contient une boucle de moins.
L'addition de deux colonnes en :epkg:`Python` seul
s'écrirait de la sorte :

::

    mat = array(...)
    for i in range(0, mat.shape[0]):
        mat[i, 0] += mat[i, 1]

Mais il est beaucoup plus efficace de s'écrire comme ceci :

::

    mat = array(...)
    mat[:, 0] += mat[:, 1]

Les deux programmes sont équivalents d'un point
de vue algorithmique à ceci près que l'addition
dans le second exemple utilise un code écrit en :epkg:`C++`.
C'est un langage bas niveau, donc débarassé de tout ce que
le langage :epkg:`Python` ajoute pour simplifier
l'écriture des programmes. Etre bas niveau permet également d'utiliser
des accélérations offertes par les processeurs récents
comme celle offertes par la librairie
`Math Kernel Library <https://en.wikipedia.org/wiki/Math_Kernel_Library>`_
qui utilise les instructions processeur
`SIMD <https://en.wikipedia.org/wiki/SIMD>`_ et
`MIMD <https://en.wikipedia.org/wiki/MIMD>`_.

*Notebooks*

.. toctree::
    :maxdepth: 1

    ../notebooks/td2a_cenonce_session_2A
    ../notebooks/td2a_correction_session_2A

*Lectures*

* `NumPy tutorials <https://numpy.org/numpy-tutorials/>`_
* `From Python to Numpy <http://www.labri.fr/perso/nrougier/from-python-to-numpy/>`_
* :ref:`Pourquoi pandas et numpy, pourquoi pas seulement pandas ? <blog-pandas-numpy>`
* :ref:`cffilinearregressionrst`

*Modules*

* `numpy <http://www.numpy.org/>`_
* `scipy <https://www.scipy.org/>`_
