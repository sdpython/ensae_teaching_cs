
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-reddim:

Projections, Réduction des dimensions
+++++++++++++++++++++++++++++++++++++

(à venir)

* PCA, Sparse PCA, Kernel PCA
* SOM
* LSH

*Lectures*

* `PCA <http://scikit-learn.org/stable/modules/decomposition.html>`_
* `Johnson–Lindenstrauss lemma <https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma>`_,
  `Random projection <http://scikit-learn.org/stable/modules/random_projection.html>`_,
  `Concentration of measure <https://en.wikipedia.org/wiki/Concentration_of_measure>`_,
  `Experiments with Random Projection <http://cseweb.ucsd.edu/~dasgupta/papers/randomf.pdf>`_
* `Compressed sensing and single-pixel cameras <https://terrytao.wordpress.com/2007/04/13/compressed-sensing-and-single-pixel-cameras/>`_
  (wikipedia : `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_)
* `Locality-sensitive hashing <https://en.wikipedia.org/wiki/Locality-sensitive_hashing>`_,
  `LSH Forest: Self-Tuning Indexes for Similarity Search <http://infolab.stanford.edu/~bawa/Pub/similarity.pdf>`_
* `Manifold learning <http://scikit-learn.org/stable/modules/manifold.html>`_
* `Cartes de Kohonen <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_clus/kohonen.html>`_
* `Dynamic Self-Organising Map <http://www.labri.fr/perso/nrougier/coding/article/article.html>`_
* `Fast Randomized SVD <https://research.fb.com/fast-randomized-svd/>`_
* `Neural Autoregressive Distribution Estimation <http://www.jmlr.org/papers/volume17/16-272/16-272.pdf>`_
* `How to Use t-SNE Effectively <http://distill.pub/2016/misread-tsne/>`_
* `Practical and Optimal LSH for Angular Distance <https://arxiv.org/abs/1509.02897>`_
* `Optimal Data-Dependent Hashing for Approximate Near Neighbors <https://arxiv.org/abs/1501.01062>`_
* `mQAPViz: A divide-and-conquer multi-objective optimization algorithm to compute large data visualizations <https://arxiv.org/abs/1804.00656>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `fbpca <http://fbpca.readthedocs.io/en/latest/>`_ : ACP
* `prince <https://github.com/MaxHalford/Prince>`_ : ACM
* `Parametric-t-SNE <https://github.com/kylemcdonald/Parametric-t-SNE/blob/master/Parametric%20t-SNE%20(Keras).ipynb>`_
* `openTSNE <https://github.com/pavlin-policar/openTSNE>`_
* `datasketch <https://github.com/ekzhu/datasketch>`_ (LSH),
  le module `minhashcuda <https://github.com/src-d/minhashcuda>`_
  implémente l'algorithme `MinHash <https://en.wikipedia.org/wiki/MinHash>`_ sur GPU
* `NearPy <https://github.com/pixelogik/NearPy>`_ (LSH)

*Animations*

* `How to Use t-SNE Effectively <http://distill.pub/2016/misread-tsne/>`_
