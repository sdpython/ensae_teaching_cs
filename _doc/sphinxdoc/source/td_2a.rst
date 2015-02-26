

.. issue.

.. _l-td2a:

.. index:: 2A


2A
==

`Python Avancé Données, Machine Learning et Programmation <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/2me-anne-formationsdiplome-95.html?id=101352>`_

Cours animé par :

* Antoine Thabault
* Nicolas Rousset
* Jérémie Jakubowicz
* Xavier Dupré


Ce cours s'étale sur 6 séances de cours/TD d'une durée de 4h.
Les outils proposés sont en langage `Python <https://www.python.org/>`_. 
Ils sont tous `open source <http://fr.wikipedia.org/wiki/Open_source>`_,
pour la plupart disponibles sur `GitHub <https://github.com/>`_ et en développement actif.
Python est récemment devenu une alternative plus que probante 
pour les scientifiques et comme c'est un langage générique, il est 
possible de gérer l'ensemble des traitements appliqués aux données, depuis
le traitements des sources de données jusqu'à leur visualisation sans changer de langage.

La présentation 
`ENSAE 2A - Données, Machine Learning et Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_
donne un aperçu des thèmes abordés. La page :ref:`Python pour Data Scientist <l-data2a>` 
liste les différents modules proposés lors de ce cours.

DataFrame, calcul matriciel, calcul distribué, Python et autres langages sont les thèmes abordés durant les deux premières séances.

.. index:: sérialisation, index, dataframe

    
TD
++

- **TD 1 : DataFrame** 
    - :ref:`TD 1 : Données et Graphes <td2acenoncesession1rst>` (:ref:`correction <td2acorrectionsession1rst>`)
        - import/export de données dans un DataFrame
        - manipulation selon une logique SQL
        - utilité des index
        - lambda function
        - premiers graphiques
- **TD 2 : calcul matriciel et astuces**
    - :ref:`TD 2A : Calcul Matriciel, Optimisation <td2acenoncesession2arst>` (:ref:`correction <td2acorrectionsession2arst>`)
    - :ref:`TD 2B : Python autres langages <td2acenoncesession2brst>` (:ref:`correction <td2acorrectionsession2brst>`)
    - :ref:`TD 2C : IPython et commandes magiques <td2acenoncesession2crst>` (:ref:`correction <td2acorrectionsession2crst>`)
    - :ref:`TD 2D : IPython et calcul distribué <td2acenoncesession2drst>` (:ref:`correction <td2acorrectionsession2drst>`)
    - :ref:`TD 2E : Sérialisation <td2acenoncesession2erst>` (:ref:`correction <td2acorrectionsession2erst>`) (avec le module `pickle <https://docs.python.org/3.4/library/pickle.html>`_)
- **TD 3 : machine learning**
    - :ref:`TD 3A : Statistiques descriptives <td2acenoncesession3arst>` (:ref:`correction <td2acorrectionsession3arst>`)
    - Présentation de `Gaël Varoquaux <http://gael-varoquaux.info/>`_ : machine learning et `scikit-learn <http://scikit-learn.org/stable/>`_
      (tutoriels sur scikit-learn <http://nbviewer.ipython.org/github/GaelVaroquaux/sklearn_pandas_tutorial/tree/master/rendered_notebooks/>`_),
      quelques extraits :
        - Par définition les plus proches voisins ne font pas d'erreur sur la base d'apprentissage, l'apprentissage consiste à forcer le modèle à faire des erreurs.
        - `Overfitting <http://en.wikipedia.org/wiki/Overfitting>`_ et `régularisation <http://en.wikipedia.org/wiki/Regularization_(mathematics)>`_
        - Erreur `L2 <http://en.wikipedia.org/wiki/Lp_space>`_ et pénalisation `L1 <http://fr.wikipedia.org/wiki/Espace_L1>`_
        - `RandomizedPCA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.RandomizedPCA.html>`_, `GridSearch <http://scikit-learn.org/stable/modules/grid_search.html>`_, `LassoCV <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html>`_
        - `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_
    - :ref:`TD 3B : Arbres de décision et Random Forests <td2acenoncesession3brst>`  (:ref:`correction <td2acorrectionsession3brst>`)    
- **TD 4 : machine learning et algorithme**
    - :ref:`TD 4A : Machine Learning et Marketting <td2acenoncesession4arst>` (:ref:`correction <td2acorrectionsession4arst>`)
        - machine learning
        - `d3.js <http://d3js.org/>`_
    - :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
    - :ref:`TD 4B : Culture algorithmique <td2acenoncesession4brst>` (:ref:`correction <td2acorrectionsession4brst>`)
        - présentation `Eléments d'Algorithmique <http://www.xavierdupre.fr/enseignement/complements/Seance4_algorithme.pdf>`_
        - `Machine learning et algorithme <http://www.xavierdupre.fr/blog/2014-10-11_nojs.html>`_
        - :ref:`exerciceplusgrandesommerst`
- **TD 5 : modèle de données**
    - `présentation <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_
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
    - :ref:`TD 5 : Modèles de données <td2acenoncesession5rst>` (:ref:`correction <td2acorrectionsession5rst>`)
- **TD 6 : algorithme et puzzle**    
    * Présentations
        * `programmation dynamique <http://www.xavierdupre.fr/enseignement/complements/ENSAE_2A_jj_Seance2.pdf>`_
        * `graphes et algorithmes <http://www.xavierdupre.fr/enseignement/complements/ENSAE_2A_jj_Seance3.pdf>`_
    * notebooks
        * correction de l'exercice de recouvrement proposé à la séance 4 (:ref:`TD 4B : Culture algorithmique <td2acenoncesession4brst>` - :ref:`correction <td2acorrectionsession4brst>`)
        * :ref:`TD 6 : Problèmes et algorithmes <td2acenoncesession6rst>` - :ref:`correction <td2acorrectionsession6rst>` 
          (ces problèmes sont tirées de plusieurs sites dont `Google Code Jam <https://code.google.com/codejam/contests.html>`_)
    * liens
        * types de complexité : `force brute <http://fr.wikipedia.org/wiki/Recherche_exhaustive>`_, 
          `glouton <http://fr.wikipedia.org/wiki/Algorithme_glouton>`_, `dynamique <http://fr.wikipedia.org/wiki/Programmation_dynamique>`_
        * :ref:`l-algoculture`
            


Le cours sera évalué avec un :ref:`projet informatique <l-projinfo2a>`.


Python et autres langages, personnaliser ses notebooks
++++++++++++++++++++++++++++++++++++++++++++++++++++++

    
.. toctree::
    :numbered:

    notebooks/python_r
    notebooks/python_csharp
    notebooks/ipython_custom_magics
    notebooks/matplotlib_zoomable
    
.. _l-td2a-start:
    
Getting started
+++++++++++++++

Il faut vous reporter à la section :ref:`l-install` pour installer python.        
Certaines séances pratiques utilisent des données depuis ce site. 
Elles sont facilement téléchargeables avec ces deux modules :

* `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_
* `pyensae <http://www.xavierdupre.fr/app/pyensae/helpsphinx/>`_


.. _l-td2a-biblio:

Bibliographie
+++++++++++++

**Livres sur le machine learning**

* `The Elements of Statistical Learning <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_, Trevor Hastie, Robert Tibshirani, Jerome Friedman
* `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_, Wes McKinney
* `Building Machine Learning Systems with Python <https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python>`_, Willi Richert, Luis Pedro Coelho
* `Learning scikit-learn: Machine Learning in Python <https://www.packtpub.com/big-data-and-business-intelligence/learning-scikit-learn-machine-learning-python>`_, Raúl Garreta, Guillermo Moncecchi
* `Modeling Creativity: Case Studies in Python <http://arxiv.org/abs/1410.0281>`_, Tom De Smedt
* `Critical Mass: How One Thing Leads to Another <http://www.philipball.co.uk/index.php?option=com_content&view=article&id=15:critical-mass-how-one-thing-leads-to-another&catid=3:books&Itemid=4>`_, Philip Ball
* `Bugra Akyildiz <http://bugra.github.io/>`_


**Livres sur les algorithmes**

* `Introduction to Algorithms <http://mitpress.mit.edu/books/introduction-algorithms>`_, Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein
* `The Algorithm Design Manual <http://www.algorist.com/>`_, Steven S. Skiena
* `Competitive Programming <http://www.comp.nus.edu.sg/~stevenha/myteaching/competitive_programming/cp1.pdf>`_, Steven Halim

**Liens**

* `Python Scientific Lecture Notes <http://scipy-lectures.github.io/>`_
* `Introduction to Data Processing with Python <http://opentechschool.github.io/python-data-intro/>`_
* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* Quelques idées de livres : `Python for Data Scientists <https://www.packtpub.com/books/content/python-data-scientists>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* `A Tour of Machine Learning Algorithms <http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/>`_
* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
  ` <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
  `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
  `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski
* `Prédire les épidémies avec Wikipedia <http://www.lemonde.fr/sante/article/2014/11/13/predire-les-epidemies-avec-wikipedia_4523461_1651302.html>`_, Le Monde
* `FastML <http://fastml.com/>`_  (blog sur le machine learning)
* :ref:`question_projet_2014`
* `Introduction to matplotlib <https://scipy-lectures.github.io/intro/matplotlib/matplotlib.html>`_

**MOOC**

* `Machine Learning par Andrew Y. Ng <https://www.class-central.com/mooc/835/coursera-machine-learning>`_ 
  (les chapitres X et XI de la semaine 6 aborde la construction d'un système de machine learning).
* `Coursera Machine Learning <https://www.coursera.org/course/ml>`_
* `Coursera Machine Algorithm <https://www.coursera.org/course/algo>`_
* `CSE373 - Analysis of Algorithms - 2007 SBU <https://www.youtube.com/playlist?list=PL5F43156F3F22C349>`_
* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ (la liste des vidéos disponibles est en bas)

**Autres cours, notebooks**

* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ - `TD <https://github.com/cs109/content>`_
* `Advanced Statistical Computing, Chris Fonnesbeck (Vanderbilt University) <http://nbviewer.ipython.org/github/fonnesbeck/Bios366/tree/master/notebooks/>`_
* `CS 188: Artificial Intelligence (Berkeley) <http://inst.eecs.berkeley.edu/~cs188/fa10/lectures.html>`_ 

**Articles d'auteurs très connus**

* `Latent Dirichlet Allocation <http://ai.stanford.edu/~ang/papers/jair03-lda.pdf>`_, David M. Blei, Andrew Y. Ng, Michael I. Jordan 
* `Analysis of a Random Forests Model <http://www.jmlr.org/papers/volume13/biau12a/biau12a.pdf>`_, Gerard Biau
* `Adaptivity of Averaged Stochastic Gradient Descent to Local Strong Convexity for Logistic Regression <http://jmlr.csail.mit.edu/papers/volume15/bach14a/bach14a.pdf>`_, Francis Bach
* `Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising <http://jmlr.csail.mit.edu/papers/volume14/bottou13a/bottou13a.pdf>`_, Léon Bottou, Jonas Peter et Al.
* `Tutorial on Practical Prediction Theory for Classification <http://www.jmlr.org/papers/volume6/langford05a/langford05a.pdf>`_, John Langford
* `Sparse Online Learning via Truncated Gradient <http://jmlr.org/papers/volume10/langford09a/langford09a.pdf>`_, John Langford, Lihong Li, Tong Zhang
* `Low-dimensional Embeddings for Interpretable Anchor-based Topic Inference <http://mimno.infosci.cornell.edu/papers/EMNLP2014138.pdf>`_, Moontae Lee, David Mimno
* `ABC model choice via random forests <http://arxiv.org/abs/1406.6288>`_, Pierre Pudlo, Jean-Michel Marin, Arnaud Estoup, Jean-Marie Cornuet, Mathieu Gautier, Christian P. Robert 
* `Mondrian Forests: Efficient Online Random Forests <http://arxiv.org/pdf/1406.2673v1.pdf>`_, Balaji Lakshminarayanan, Daniel M. Roy, Yee Whye Teh
* `Stochastic Gradient Tricks <http://leon.bottou.org/papers/bottou-tricks-2012>`_
* `SiGMa: Simple Greedy Matching for Aligning Large Knowledge Bases <http://arxiv.org/abs/1207.4525>`_, Simon Lacoste-Julien, Konstantina Palla, Alex Davies, Gjergji Kasneci, Thore Graepel, Zoubin Ghahramani
* `Learning from Partial Labels <http://www.seas.upenn.edu/~taskar/pubs/partial_labels_jmlr11.pdf>`_, Timothee Cour, Benjamin Sapp, Ben Taskar
* `Word Alignment via Quadratic Assignment <http://www.seas.upenn.edu/~taskar/pubs/naacl06_qap.pdf>`_, Simon Lacoste-Julien, Ben Taskar, Dan Klein, Michael I. Jordan
* `Contextual Bandit Learning with Predictable Rewards <http://arxiv.org/abs/1202.1334>`_, Alekh Agarwal, Miroslav Dudík, Satyen Kale, John Langford, Robert E. Schapire
* `Learning from Logged Implicit Exploration Data <http://papers.nips.cc/paper/3977-learning-from-logged-implicit-exploration-data>`_, Alex Strehl, John Langford, Lihong LiSham, M. Kakade


**Librairies de machine learning**

* `scikit-learn <http://scikit-learn.org/stable/index.html>`_
* `Vowpal Wabbit <https://github.com/JohnLangford/vowpal_wabbit/wiki>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_

**Compétition de code**

* `Google Code Jam <https://code.google.com/codejam>`_
* `TopCoder <http://www.topcoder.com/>`_
* `UVa Online Judge <http://uva.onlinejudge.org/>`_
* `Le problème des huit reines <http://zanotti.univ-tln.fr/algo/REINES.html>`_
* `Projet Euler <https://projecteuler.net/>`_


Pour finir, `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_ :

.. image:: http://scikit-learn.org/stable/_static/ml_map.png
    :width: 500

.. toctree::
    :hidden:
    
    td_2a_enonce
    td_2a_correction
    td_2a_s5_synthese
    debutermlprojet
    specials/algorithm_culture
    entretiens

    
