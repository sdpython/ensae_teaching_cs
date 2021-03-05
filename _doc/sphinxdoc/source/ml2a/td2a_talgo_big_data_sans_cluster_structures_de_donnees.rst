
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-cluster-non-struct-2a:

Big data sans cluster, structures de données
++++++++++++++++++++++++++++++++++++++++++++

.. index:: itérateur

Beaucoup de jeux de données tiennent en mémoire mais les temps de calcul ou de chargement
même pour des choses simples sont parfois rédhibitoires. Parfois, on ne peut simplement pas
copier plus d'une fois le jeu de données sous peine de dépasser les capacités de la mémoire.
Face à ces obstacles, différentes stratégies sont possibles. Un échantillon aléatoire
conserve les propriétés statistiques mais réduit la taille mémoire. Les itérateurs
réduisent le temps le laps de temps entre le début de lecture des données et le début des
calculs. Ils ont aussi le mérité de n'utiliser que les données nécessaires lors des calculs :
les données défilent en mémoire. D'autres modules font en sorte qu'on puisse écrire des calculs
de la même manière alors que les données sont toujours sur le disque dur. D'autres compressent
les données et ne les décompressent que si besoin. Dans tous les cas, il s'agit de contourner
de façon intelligente la contrainte de volume. Et s'il n'y avait qu'une idée
à retenir, ce serait le concept d'ìtérateur <https://fr.wikipedia.org/wiki/It%C3%A9rateur>`_.

* `présentation données structurées <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_no_sql_exo
    ../notebooks/dataframe_matrix_speed
    ../notebooks/ml_huge_datasets
    ../notebooks/ml_table_mortalite

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_no_sql_twitter
    ../notebooks/_gs2a_big_in_memory

*Lectures*

- Propriétés des base de données : `ACID <http://fr.wikipedia.org/wiki/Propri%C3%A9t%C3%A9s_ACID>`_,
  `relationnelle <http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_relationnelle>`_,
  `transactionnelle <http://fr.wikipedia.org/wiki/Transaction_informatique>`_
- Best practices, index et `foreign key <http://en.wikipedia.org/wiki/Foreign_key>`_
  (importance des `random access <http://fr.wikipedia.org/wiki/Random_Access_Memories>`_ et `accès séquentiel <http://en.wikipedia.org/wiki/Sequential_access>`_)
- Limites des structures relationnelles
  (`données arborescentes <http://fr.wikipedia.org/wiki/Base_de_donn%C3%A9es_hi%C3%A9rarchique>`_,
  données hétérogènes)
- Base de données non relationnelles dont `NoSQL <http://fr.wikipedia.org/wiki/NoSQL>`_
- :ref:`l-td25asynthese`
- `Un tools d'itertour, ou l'inverse <http://sametmax.com/un-tools-ditertour-ou-linverse/>`_
- `Benchmark of Python JSON libraries <http://artem.krylysov.com/blog/2015/09/29/benchmark-python-json-libraries/>`_

*Bases de données no SQL*

* `MongoDB <https://www.mongodb.com/>`_
* `rethinkdb <https://rethinkdb.com/>`_ (python : `rethinkdb <https://pypi.python.org/pypi/rethinkdb/>`_)

*Modules*

* `dask <http://dask.pydata.org/en/latest/>`_
* `cytoolz <https://github.com/pytoolz/cytoolz>`_
