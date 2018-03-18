
.. |pyecopng| image:: _static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pystatpng|

Streaming algorithms
++++++++++++++++++++

Les algorithmes *streaming* que Wikipédia traduit par
`Algorithme de fouille de flots de données <https://fr.wikipedia.org/wiki/Algorithme_de_fouille_de_flots_de_donn%C3%A9es>`_
sont des algorithmes qui s'exécutent sans avoir connaissance de l'ensemble des données
ni même combien il y en a. Cela signifie que l'algorithme peut s'arrêter à tout moment
et qu'il est capable de retourner un résultat valide sur l'ensemble des données qu'il
a traités jusqu'à présent. L'algorithme le plus connu est sans aucun doute
`Reservoir Sampling <https://en.wikipedia.org/wiki/Reservoir_sampling>`_
qui permet de tirer un échantillon aléatoire dans un jeu de données dont la taille
est inconnue à l'avance.

* `Répartir train / test en streaming <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/split_train_test.html#streaming-splitting>`_

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_streaming

*Lectures*

* Algorithme BJKST `Counting distinct elements in a data stream <https://pdfs.semanticscholar.org/e349/7952347101a3535434bc35d378224cf87bcc.pdf>`_
* `Streaming Algorithms <http://resources.mpi-inf.mpg.de/departments/d1/teaching/ss14/gitcs/notes3.pdf>`_
* `Optimal streaming histograms <https://amplitude.com/blog/2014/08/06/optimal-streaming-histograms/>`_
* `Density Estimation Over Data Stream <http://alumni.cs.ucr.edu/~wli/publications/deosd.pdf>`_
* `Confidence Decision Trees via Online and Active Learning for Streaming (BIG) Data <https://arxiv.org/pdf/1604.03278.pdf>`_
* `Approximation and Streaming Algorithms for Histogram Construction Problems <http://www.mathcs.emory.edu/~cheung/papers/StreamDB/Histogram/2005-Guha-Histogram.pdf>`_
* `State-of-the-art on clustering data streams <https://bdataanalytics.biomedcentral.com/articles/10.1186/s41044-016-0011-3>`_
* `Parallel Computing of Kernel Density Estimates with MPI <http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.102.5195&rep=rep1&type=pdf>`_
* `Density Estimation with Adaptive Sparse Grids for Large Data Sets <http://web.mit.edu/pehersto/www/preprints/sgde_siam.pdf>`_
* `Sliding HyperLogLog: Estimating cardinality in a data stream <https://hal.archives-ouvertes.fr/file/index/docid/465313/filename/sliding_HyperLogLog.pdf>`_
* `Data Streaming Algorithms 2009 <http://www.cs.dartmouth.edu/~ac/Teach/CS85-Fall09/Notes/lecnotes.pdf>`_,
  `Data Streaming Algorithms 2011 <http://www.cs.dartmouth.edu/~ac/Teach/CS49-Fall11/Notes/lecnotes.pdf>`_
* `Data Stream Management <http://web.cs.ucla.edu/classes/winter17/cs240B/notes/DataStreamMg.pdf>`_
  (collection d'articles)

*Modules*

* `StreamLib <https://github.com/jiecchen/StreamLib>`_
* `pandas_streaming <https://github.com/sdpython/pandas_streaming/>`_
* `streamparse <https://github.com/Parsely/streamparse>`_
