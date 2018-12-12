
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-categories:

Variables catégorielles
+++++++++++++++++++++++

Les variables catégorielles sont plus ou moins difficiles
selon que le nombre de catégories est grand ou pas.
S'il est petit, les transformations classiques
type `OneHotEncoder <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html>`_
sont suffisamment performantes. Lorsque le nombre n'est pas
très grand, il faut nécessairement réduire le nombre
de catégorie en utilisant un
`BaseNEncoder <http://contrib.scikit-learn.org/categorical-encoding/basen.html>`_
ou un
`HashingEncoder <http://contrib.scikit-learn.org/categorical-encoding/hashing.html>`_.
Si le nombre est très grand, il peut arriver que ce soit ce qui
est attendu comme l'ensemble des produits d'un site de vente en ligne
ou un grand nombre quelque peu surfaits et dû en grande partie
à erreurs de saisie. Par exemple pour une colonne qui contient
le nom d'une ville, *Charleville* et *Charleville-Mézières*
désignent la même ville et devraient être rangés dans
la même catégorie. Néanmoins, le fait de faire la différence
est peut-être intéressant, cela veut peut-être dire que la personne
vit à Mézières plutôt qu'à Charleville. Pour tenir compte
des ces similarités au niveau caractères,
le module :epkg:`dirty-cat` propose le
`SimilarityEncoder <https://dirty-cat.github.io/stable/generated/dirty_cat.SimilarityEncoder.html#dirty_cat.SimilarityEncoder>`_
qui est particulièrement efficace pour gérer ces erreurs
ennuyeuses mais contenant de l'information.

(à venir)

* Corrélation entre des variables catégorielles
* `SimilarityEncoder <https://dirty-cat.github.io/stable/generated/dirty_cat.SimilarityEncoder.html#dirty_cat.SimilarityEncoder>`_.

*Notebooks*

* `Hashing et catégories <http://www.xavierdupre.fr/app/papierstat/helpsphinx/notebooks/artificiel_category_hash.html>`_
* :ref:`td2asentimentanalysisrst` (:ref:`correction <td2asentimentanalysiscorrectionrst>`)

*Lectures*

* :ref:`Tranformer les variables catégorielles et contrastes <encoding-categorie-id>`
* :ref:`blog-dirty-cat`
* `Corrélations entre des variables catégorielles <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/notebooks/correlation_non_lineaire.html>`_
* `Exemple de traitement d'une variable catégorielle <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/notebooks/solution_2017.html#solution2017rst>`_
* `Enoncé d'examan autour des variables catégorielles <http://www.xavierdupre.fr/site2013/enseignements/tdnoteseul/td_note_2017.pdf>`_
  et sa :ref:`corection <tdnote2017rst>`
* `Visiting: Categorical Features and Encoding in Decision Trees <https://medium.com/data-design/visiting-categorical-features-and-encoding-in-decision-trees-53400fa65931>`_
* `Similarity encoding for learning with dirty categorical variables <https://hal.inria.fr/hal-01806175>`_
* `CatBoost vs. Light GBM vs. XGBoost <https://towardsdatascience.com/catboost-vs-light-gbm-vs-xgboost-5f93620723db>`_
* `Similarity encoding for learning with dirty categorical variables <https://arxiv.org/pdf/1806.00979.pdf>`_

*Modules*

* `scikit-learn <http://scikit-learn.org/stable/>`_
* `category_encoders <http://contrib.scikit-learn.org/categorical-encoding/>`_
* `catboost <https://github.com/catboost/catboost>`_
* :epkg:`dirty-cat`
