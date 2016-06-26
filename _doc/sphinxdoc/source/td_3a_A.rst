
Découverte de Hadoop et premier job Map/Reduce (PIG)
====================================================

Séances dirigées
++++++++++++++++

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs3a_hadoop_decouverte
    

Exercices et lectures recommandées
++++++++++++++++++++++++++++++++++

* manipulation de fichiers avec `HDFS <http://hadoop.apache.org/docs/r1.2.1/hdfs_design.html>`_
* premier job avec `PIG-latin <https://pig.apache.org/docs/r0.7.0/piglatin_ref2.html>`_ [#fp2]_
* parallèle entre la syntaxe `PIG <http://pig.apache.org/docs/r0.12.1/basic.html>`_ et `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_
* `ENSAE 3A - Map/Reduce en pratique <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_3A/index.html>`_
* `SQL Magic Commands with SQLite in a Notebook <http://www.xavierdupre.fr/app/pyensae/helpsphinx/notebooks/pyensae_sql_magic.html>`_

.. [#fp2] Les exercices des notebooks s'appuient sur le langage `PIG-latin <http://en.wikipedia.org/wiki/Pig_Latin>`_ qui est un langage
          haut niveau permettant d'écrire des tâches Map Reduce complexes. Le script est ensuite converti en un ensemble de 
          `mapper / reducer <http://hadooptutorial.wikispaces.com/MapReduce>`_. 
          Ce langage suffit dans la plupart des cas
          et le temps de développement est très réduit par rapport à un langage plus bas niveau.
          L'autre langage haut niveau est `Hive <https://hive.apache.org/>`_. Sa syntaxe est très proche de celle
          du `SQL <http://fr.wikipedia.org/wiki/Structured_Query_Language>`_. 
          `PIG <http://en.wikipedia.org/wiki/Pig_Latin>`_ a été choisi
          car `Hive <https://hive.apache.org/>`_ est plus un moyen de lancer rapidement de petites
          tâches, PIG permet des tâches plus conséquentes pour un coût d'apprentissage
          très raisonnable.