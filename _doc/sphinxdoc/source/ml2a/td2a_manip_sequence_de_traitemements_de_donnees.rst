
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Séquence de traitemements de données
++++++++++++++++++++++++++++++++++++

Il est très rare qu'un modèle de machine learning puisse
être appliqué sur des données brutes. Il y a toujours
une étape de nettoyages, de traitements des valeurs manquantes.
Ce sont souvent des étapes qu'on effectue dans plusieurs cellules
distinctes d'un notebook et qu'on exécute à chaque fois
que les données sont rafraîchies. On peut néanmoins vouloir
les assembler en un seul objet afin de simplifier le code,
on peut aussi souhaiter optimiser certains paramètres, un
traitement particulier au sein d'une séquence de traitements.
C'est ainsi que la notion de *pipeline*, c'est un objet
qui conserve la mémoire d'une séquence de traitements
tout en lui donnant l'apparence d'un seul.

(*à venir*)

*Lecture*

* `Pipeline <http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline>`_
* `FeatureUnion <http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.FeatureUnion.html#sklearn.pipeline.FeatureUnion>`_
* `FunctionTransformer <http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.FunctionTransformer.html#sklearn.preprocessing.FunctionTransformer>`_
* `ItemSelector <http://scikit-learn.org/stable/auto_examples/hetero_feature_union.html>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/>`_
