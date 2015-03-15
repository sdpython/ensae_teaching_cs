
.. _l-proj_data:

Data en folie
=============

Il est difficile de résumer les sujets de cette rubrique.
Il s'agit toujours de triturer des données de différentes façons,
machine learning, datamining, recherche opérationnelle, texte mining...

.. _l-data-velib:


Inférer les trajectoirs de vélo vélib
-------------------------------------

C'était le sujet de la première coding party que personne
n'est vraiment arrivé à conclure. Avec un peu plus de temps, qui sait ?

:ref:`l-codingparty1`

.. _l-data-nuage:

Nuages de mots, extraction de concepts
--------------------------------------


Les nuages de mots sont apparus récemment pour représenter les mots-clés les plus importants sur une page, 
un ensemble de pages internet : `Tag Cloud <http://en.wikipedia.org/wiki/Tag_cloud>`_.

.. image:: nuage.png

L'objectif est de construire ces nuages de points pour les discours du premier ministre et 
du président de la République. Le rendu graphique peut être réalisé simplement 
à partir du langage HTML (voir l'`exemple suivant <http://www.xavierdupre.fr/enseignement/projet_data/tag_cloud.html>`_) 
ou en utilisant des représentations dynamiques 
(voir `More about interactive graphs using Python, d3.js, R, shiny, IPython, vincent, d3py, python-nvd3 <http://www.xavierdupre.fr/blog/2013-11-30_nojs.html>`_).
Pour déterminer l'importance des termes, les premiers essais pourront être faits en fonction 
de la fréquence de chaque mot bien que cette méthode a tendance à favoriser les petits mots. 
On pourra ensuite utiliser des critères plus complexes comme celles suggérées sur la page 
`Tag Cloud <http://en.wikipedia.org/wiki/Tag_cloud>`_.

Quelques références bibliographiques :

- `BM25 <http://en.wikipedia.org/wiki/Okapi_BM25>`_ : c'est une des variables utilisées par les moteurs de recherches
- `TF-IDF <http://fr.wikipedia.org/wiki/TF-IDF>`_
- `Représentations du texte pour la classification arborée <http://www.xavierdupre.fr/enseignement/projet_data/texte_n187r1340_mellet_co.pdf>`_
- `Tag Clusters as Information Retrieval Interfaces <http://www.xavierdupre.fr/enseignement/projet_data/texte_tag_cloud_Knautz_Soubusta_Stock.pdf>`_
- `Sur la topologie d'un arbre phylogénétique... <http://www.xavierdupre.fr/enseignement/projet_data/texte_topo_MSH_1987__100__57_0.pdf>`_

Pour la partie extraction de concepts, on pourra s'inspirer de :

- `Interactive Retrieval Based on Wikipedia Concepts <http://arxiv.org/abs/1412.8281>`_, Lanbo Zhang

Deux blogs qui pourront vous donner d'autres idées comme calculer la richesse d'un vocabulaire :

- `Pascal Marchand, richesse lexicale <http://pascal-marchand.fr/spip.php?article13>`_
- `Corpus - La distance intertextuelle <http://corpus.revues.org/index52.html>`_

Si besoin, voici d'autres données sur un autre blog :

- `Veronis/Discours 2007 <http://sites.univ-provence.fr/veronis/Discours2007/>`_
- `Veronis Premiers Ministres <http://sites.univ-provence.fr/veronis/Premiers/>`_

.. _l-data-twitter:

Twitter
-------

On peut faire beaucoup de choses avec `Twitter <https://twitter.com/>`_. La première étape consiste à récupérer des données
avec des modules tels que :

- `tweepy <http://www.tweepy.org/>`_
- `twitter <https://pypi.python.org/pypi/twitter>`_
- `python-twitter <https://pypi.python.org/pypi/python-twitter>`_


Ensuite, l'exploitation des données peut varier. A partir de données historiques qu'on collectera tout au long du projet,
on peut chercher à prédire un événément, la météo, des opinions...

Quelques références :

- `Competing Opinions and Stubborness: Connecting Models to Data <http://arxiv.org/pdf/1411.7415v1.pdf>`_
- `Home Location Identification of Twitter Users <http://arxiv.org/ftp/arxiv/papers/1403/1403.2345.pdf>`_
- `Opinion control in complex networks <http://arxiv.org/pdf/1412.2170v1.pdf>`_


.. _l-data-whoosh:

Recherche de texte dans n'importe quelle base de données avec Whoosh
--------------------------------------------------------------------

`Whoosh <http://pythonhosted.org//Whoosh/index.html>`_ est un module Python qui permet 
de faire de la recherche dans une base de données de textes. Il faudra d'abord
constituer un corpus de texte (discours politiques, 
pages `wikipedia dumps <http://dumps.wikimedia.org/>`_, Twitter, blogs, ...)

Evaluer un moteur de recherche n'est pas chose facile, cela dépend
de la tâche, du corpus...
Une métrique possible est le `DCG <http://en.wikipedia.org/wiki/Discounted_cumulative_gain>`_.
Le projet se déroulera en plusieurs étapes :

* constitution du corpus de texte
* premiers exemples avec Whoosh
* définition de l'objectif de recherche
* évaluation
* possible extensions
    * `query rewriting <http://hughewilliams.com/2012/03/19/query-rewriting-in-search-engines/>`_
    * `Rewriting Queries <https://developers.google.com/custom-search/docs/queries>`_
    * `Online Expansion of Rare Queries for Sponsored Search <https://classes.soe.ucsc.edu/ism293/Spring09/material/papers/lec6/quartz.pdf>`_
    
    
Source de textes
----------------

* `wikipedia dumps <http://dumps.wikimedia.org/>`_
* :ref:`f-discourspolitique` (pour récupérer les discours politiques de l'Elysées)

