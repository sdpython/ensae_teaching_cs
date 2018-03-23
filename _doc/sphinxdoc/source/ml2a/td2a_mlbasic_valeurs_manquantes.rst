
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Valeurs manquantes
++++++++++++++++++

.. index:: valeurs manquantes

Les valeurs manquantes sont rarement l'objectif final
d'un système de prédiction mais elles sont souvent sur le chemin.
Pourquoi leur consacrer un chapitre alors qu'il paraît si facile
de les remplacer par la moyenne ? Pourquoi ne pas chercher à
les prédire puisqu'il s'agit d'utiliser une valeur appropriée à la
place de quelque chose qu'on ne connaît ? Les mots-clés importants :
*imputation*, *MICE*, *Amelia*.

*(à venir)*

*Lectures*

* `Missing Data <https://en.wikipedia.org/wiki/Missing_data>`_
* `Imputation de données manquantes <https://www.math.univ-toulouse.fr/~besse/Wikistat/pdf/st-m-app-idm.pdf>`_
* `Missing Data & How to Deal: An overview of missing data <https://liberalarts.utexas.edu/prc/_files/cs/Missing-Data.pdf>`_
* `Additive Non-negative Matrix Factorization for Missing Data <https://arxiv.org/abs/1007.0380>`
* `Scalable Tensor Factorizations for Incomplete Data <https://arxiv.org/pdf/1005.2197.pdf>`_
* `Missing-data imputation <http://www.stat.columbia.edu/~gelman/arm/missing.pdf>`_
* `Check your missing-data imputations using cross-validation <http://andrewgelman.com/2012/03/18/check-your-missing-data-imputations-using-cross-validation/>`_
* `Multiple Imputation for Continuous and Categorical Data: Comparing Joint and Conditional Approaches <http://www.stat.columbia.edu/~gelman/research/published/MI_manuscript_RR.pdf>`_
* `Multiple Imputation by Chained Equations: What is it and how does it work? <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/>`_
* `Much ado about nothing: A comparison of missing data methods and software to fit incomplete data regression models <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1839993/>`_

*Librairies*

* `fancyimpute <https://github.com/hammerlab/fancyimpute>`_
* `knnimpute <https://github.com/hammerlab/knnimpute>`_
