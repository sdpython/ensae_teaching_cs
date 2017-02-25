
.. _l-page-idees:

=================
La page des idées
=================

Le problème quand on commence, c'est qu'il n'y jamais de fin.
Quelques idées non traitées qui pourront peut-être intéresser quelques contributeurs.
D'autres sont recensées sur
`GitHub/issues <https://github.com/sdpython/ensae_teaching_cs/issues>`_
(ou `Waffle <https://waffle.io/sdpython/ensae_teaching_cs>`_).

.. contents::
    :local:

Algorithmes (1A)
================

.. todoext::
    :title: Ajouter un exercice sur le templating (jinja2, mako)
    :issue:
    :tag: plus

    Le templating fonction comme la fonction ``format`` et permet
    en plus de faire des répétitions. C'est très utiliser
    dans le domaine du web, notamment par `django <https://www.djangoproject.com/>`_.

.. todoext::
    :title: ajouter un notebook sur flexx
    :issue: 13
    :tag: plus

    Voir blog post sur :ref:`Flexx <blog-post-flexx>`.

.. todoext::
    :title: Estimer le n pourcentile d'une variable aléatoire
    :tag: plus

    Intéressant pour une séance de travaux pratiques.
    `Estimating the n percentile of a set <http://matthewfl.com/2018/programming/algorithms/estimating-the-n-percentile-of-a-set>`_

.. todoext::
    :title: Simuler différentes systèmes de votes
    :tag: plus

    Intéressant pour une séance de travaux pratiques.
    `Theoretical online voting system <http://matthewfl.com/2094/programming/algorithms/theoretical-online-voting-system>`_,
    `Survey of Fully Verifiable Voting Cryptoschemes <https://courses.csail.mit.edu/6.857/2016/files/2.pdf>`_.

Data Science (2A)
=================

Programmation
-------------

.. todoext::
    :title: techniques de webscrapping
    :tag: plus

    * beautifulsoup, ghost.py, scrappy
    * `Python's Web Framework Benchmarks <http://klen.github.io/py-frameworks-bench/>`_

.. todoext::
    :title: aborder les formats de données sparses (CRS, ...)
    :tag: plus

    See `Compressed Sparse Row Format (CSR) <http://www.scipy-lectures.org/advanced/scipy_sparse/csr_matrix.html>`_.

.. todoext::
    :title: ajouter un notebook sur joblib
    :tag: plus

    joblib est utilisé par scikit-learn pour
    paralléliser les calculs

.. todoext::
    :title: Retravailler la partie visualisation de Python pour un data scientist
    :tag: plus

    Il manque un notebooks sur les visualisations les plus utilisées en machine learning,
    ROC, régression, visualisation d'arbres de décision avec ete3, les cartes.
    Insister sur l'interactivité.
    Voir `TD 4B : Visualisation <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_enonce.html#seance6graphesenoncerst>`_
    (`correction <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/seance6_graphes_correction.html#seance6graphescorrectionrst>`_),
    ce notebook présente un moyen de faire une carte géographique, des graphes zoomables.

.. todoext::
    :title: ajouter ctypes
    :tag: plus

    utilisation du module ctypes pour les import C++
    + un exemple de `sklearn-compiledtrees <https://github.com/ajtulloch/sklearn-compiledtrees/>`_

Programmation avancée
---------------------

.. todoext::
    :title: aborder d'autres librairies
    :tag: plus

    py-earth, pytorch, boruta, wendelin.core, zodb,
    (requires transaction, zc.lockfile, zodbpickle, ZODB, zdaemon, ZEO, ZODB3, wendelin.core),
    ghost.py (scrapping)
    h5py, PyTables, lda
    See `Related Projects <http://scikit-learn.org/stable/related_projects.html>`_,
    `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_

.. todoext::
    :title: ajouter un notebook sur numba, llvmlite
    :tag: plus

    Il n'y pas que CPython pour ooptimiser les calculs.
    Aborder les notions de JIT.

.. todoext::
    :title: ajouter MILP
    :tag: plus

    avec des modules tels que `pyomo <http://www.pyomo.org/>`_,
    lire `Mixed integer programming for machine learning <http://www.litislab.fr/wp-content/uploads/2015/12/Canu-S.pdf>`_,
    `GLPK/Python <https://en.wikibooks.org/wiki/GLPK/Python#Python-GLPK>`_,
    `optlang <http://optlang.readthedocs.io/en/latest/>`_

Théorie
-------

.. todoext::
    :title: multi-label, coverage_error
    :tag: plus

    fonction `coverage-error <http://scikit-learn.org/stable/modules/model_evaluation.html#coverage-error>`_,
    lire `Mining Multi-label Data <http://lpis.csd.auth.gr/publications/tsoumakas09-dmkdh.pdf>`_

.. todoext::
    :title: ajouter projections
    :tag: plus

    parler plus précisément des projections, de la réduction des dimensions

.. todoext::
    :title: HMM
    :tag: plus

    parler de Modèles de Markov cachés HMM avec des mélanges de gaussiennes
    pour analyser les séries temporelles
    `hmmlearn <https://github.com/hmmlearn/hmmlearn/blob/master/>`_,
    `seqlearn <https://github.com/larsmans/seqlearn>`_,
    `pomegranate <https://github.com/jmschrei/pomegranate>`_

.. todoext::
    :title: modules, framework à regarder
    :tag: plus

    * `REP <https://github.com/yandex/rep>`_
    * `TPOT <https://github.com/rhiever/tpot>`_
    * `auto-sklearn <https://github.com/automl/auto-sklearn/>`_

    * `msmbuilder <http://msmbuilder.org/3.6.0/decomposition.html>`_
    * `sparkit-learn <https://github.com/lensacom/sparkit-learn>`_
    * `kmodes <https://github.com/nicodv/kmodes>`_
    * `hdbscan <https://github.com/scikit-learn-contrib/hdbscan>`_
    * `sacred <https://github.com/IDSIA/Sacred>`_

GPU
---

.. todoext::
    :title: Aborder theano, keras, GPU et les types de deep strucures
    :tag: done
    :hidden:

    Et les autres caffee, tensorflow, cntk, torch, h2o
    (voir `libraries <http://www.teglor.com/b/deep-learning-libraries-language-cm569/>`_,
    `librairies 1 <http://machinelearningmastery.com/popular-deep-learning-libraries/>`_,
    `librairies 2 <http://www.datasciencecentral.com/profiles/blogs/here-are-15-libraries-in-various-languages-to-help-implement-your>`_,
    `comparison <https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software>`_
    et différents types de structures DNN, CNN
    `deep learning <https://en.wikipedia.org/wiki/Deep_learning>`_

NLP
---

.. todoext::
    :title: rédiger un ou deux notebook sur le traitement du langage
    :tag: done

    Aborder la distance d'édition, n-grams, NLTK, gensim,
    word2vec, LDA (Latent Dirichlet Application), traduction statistique,
    td-idf, coocurrence, analyse de sentiment, stemming
    `SMT <https://en.wikipedia.org/wiki/Statistical_machine_translation>`_,
    alignement,
    `moses <http://www.statmt.org/moses/>`_
