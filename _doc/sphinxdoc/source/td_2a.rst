

.. _l-td2a:

==========================================
Python pour un Data Scientist / Economiste
==========================================

.. index:: 2A

`ENSAE - OMI2F2 <http://www.ensae.fr/formations-navhorizontale-172/statisticien-conomiste-navhorizontale-48/2me-anne-formationsdiplome-95.html?id=101352>`_

Cours animé par :
`Xavier Dupré <mailto:xavier.dupre AT gmail.com>`_  (ENSAE 1999) [#fwrite1]_, 
Anne Muller (ENSAE 2012) [#fwrite1]_,
Elodie Royant (ENSAE 2008) [#fwrite2]_,
Antoine Thabault (ENSAE 2012) [#fwrite2]_,
Jérémie Jakubowicz (ENSAE 2002) [#fwrite2]_,
Nicolas Rousset [#fwrite2]_,
Antoine Ly (ENSAE 2015),
Benjamin Donnot (ENSAE 2015),
Gaël Varoquaux [#fwrite2]_


Ce cours s'étale sur 6 séances de cours/TD d'une durée de 4h.
Les outils proposés sont en langage `Python <https://www.python.org/>`_. 
Ils sont tous `open source <http://fr.wikipedia.org/wiki/Open_source>`_,
pour la plupart disponibles sur `GitHub <https://github.com/>`_ et en développement actif.
Python est récemment devenu une alternative plus que probante 
pour les scientifiques et comme c'est un langage générique, il est 
possible de gérer l'ensemble des traitements appliqués aux données, depuis
le traitements des sources de données jusqu'à leur visualisation sans changer de langage.

Le cours est prévu pour des profils plutôt statistiques |pystatpng| 
ou plutôt économiques |pyecopng|. Ces images reviendront pour indiquer 
si les contenus s'adressent plutôt aux uns ou aux autres.
La présentation 
`ENSAE 2A - Données, Machine Learning et Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html>`_ |slideslogo|
donne un aperçu des thèmes abordés.

* :ref:`feuille de route 2016 <l-feuille-de-route-2016-2A>`
* :ref:`projet informatique <l-projinfo2a>`. 

**Thèmes :**

.. contents::
    :local:
    :maxpdeth: 2
    
.. |slideslogo| image:: _static/slides_logo.png
             :height: 20
             :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/pressphinx_2A/index.html


.. |pyecopng| image:: _static/pyeco.png
            :alt: Economie
            
.. |pystatpng| image:: _static/pystat.png
            :alt: Statistique
            
            
Rappels de programmation
========================

|pyecopng| 

.. toctree::
    :maxdepth: 2

    notebooks/td2_eco_rappels_1a


.. index:: sérialisation, index, dataframe

    
Matrices et DataFrames - numpy pandas
=====================================

|pyecopng| |pystatpng|

Notions abordées :

- import/export de données dans un DataFrame
- manipulation selon une logique SQL
- utilité des index
- lambda function
- premiers graphiques
- commandes magiques

.. toctree::
    :maxdepth: 2
    
    ext2a/sql_doc
    notebooks/_gs2a_dataframe
    notebooks/_gs2a_sql    
    notebooks/_gs2a_magic_commands


Visualisation
=============

|pystatpng| |pyecopng|

Graphes
+++++++

Plan

* Présenter `10 plotting libraries at PyData 2016 <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_.
* Grouper les étudiants par deux
* Considérer un jeu de données
* Chaque groupe essaye une librairie différente
* Insister sur la visualisation de gros jeu de données

Il existe de nombreuses librairies de visualisation réparties en deux grandes familles.
La première produit des images
(`matplotlib <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_matplotlib.html#immatplotlibrst>`_,
`seaborn <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_seaborn.html#imseabornrst>`_,
`networkx <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_),
la seconde produit des graphes animés à l'aide de Javascript
(`bokeh <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/js_bokeh.html#jsbokehrst>`_,
`bqplot <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/im_networkx.html#imnetworkxrst>`_).
Les librairies les plus récentes implémentent les deux modes en cherchant toujours plus
de simplicité. A ce sujet, il faut jeter un coup d'oeil à 
`flexx <https://flexx.readthedocs.io/en/stable/>`_. Elles explorent aussi 
la visualisation animée de gros jeux de données telle que 
`datashader <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/notebooks/big_datashader.html#bigdatashaderrst>`_.

*matplotlib*

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_visu

*Javascript*

.. toctree::
    :maxdepth: 2
    
    ext2a/javascript_doc

* Lire :ref:`Javascript et traitement de données <blog-js-data>`

Cartes
++++++

* format de cartes 
  `shapefiles <https://en.wikipedia.org/wiki/Shapefile>`_,
  `topoJSON <https://en.wikipedia.org/wiki/GeoJSON#TopoJSON>`_,
  `geoJSON <https://en.wikipedia.org/wiki/GeoJSON>`_
* conversion de coordonnées en longitude / latitude
* librairies 
  `basemap <http://matplotlib.org/basemap/>`_, ...
* sources :
  `DataMaps <http://datamaps.github.io/>`_,
  `Find Data <https://bost.ocks.org/mike/map/#finding-data>`_

Machine Learning
================

.. _l-ml-skgael:

Bases
+++++


|pyecopng| |pystatpng|

*Présentation 1* - cours de `Gaël Varoquaux <http://gael-varoquaux.info/>`_

* `notes de lectures <https://github.com/GaelVaroquaux/sklearn_ensae_course>`_
* machine learning et `scikit-learn <http://scikit-learn.org/stable/>`_
  (`tutoriels sur scikit-learn <http://nbviewer.jupyter.org/github/GaelVaroquaux/sklearn_pandas_tutorial/tree/master/rendered_notebooks/>`_),  
* Quelques extraits :
    - Par définition les plus proches voisins ne font pas d'erreur sur la base d'apprentissage,
      l'apprentissage consiste à forcer le modèle à faire des erreurs.
    - `Overfitting <http://en.wikipedia.org/wiki/Overfitting>`_ et 
      `régularisation <http://en.wikipedia.org/wiki/Regularization_(mathematics)>`_
    - Erreur `L2 <http://en.wikipedia.org/wiki/Lp_space>`_ 
      et pénalisation `L1 <http://fr.wikipedia.org/wiki/Espace_L1>`_
    - `RandomizedPCA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.RandomizedPCA.html>`_, 
      `GridSearch <http://scikit-learn.org/stable/modules/grid_search.html>`_, `LassoCV <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html>`_
    - `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_
    
*Prolongements*
    
.. toctree::
    :maxdepth: 2
    
    questions/some_ml

*Notebooks*

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_statdes
    notebooks/_gs2a_ml

*Lectures*

* :ref:`Travailleur les features ou changer de modèle <mlfeaturesmodelrst>`
* :ref:`Bien démarrer un projet de machine learning <l-debutermlprojet>`
* :ref:`question_projet_2014`
* `MA 2823 Foundations of Machine Learning (Fall 2016) <http://cazencott.info/index.php/pages/MA-2823-Foundations-of-Machine-Learning-%28Fall-2016%29>`_
* `A Random Forest Guided Tour <http://www.lsta.upmc.fr/BIAU/bs.pdf>`_, Gérard Biau, Erwan Scornet
* `Courbe ROC <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_

*Recherche*

* `Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife <http://jmlr.csail.mit.edu/papers/volume15/wager14a/wager14a.pdf>`_
* `Making Tree Ensembles Interpretable <https://arxiv.org/pdf/1606.05390v1.pdf>`_
* `Random Rotation Ensembles <http://www.jmlr.org/papers/volume17/blaser16a/blaser16a.pdf>`_
* `Understanding variable importances in forests of randomized trees <http://papers.nips.cc/paper/4928-understanding-variable-importances-in-forests-of-randomized-trees.pdf>`_
* `XGBoost: A Scalable Tree Boosting System <https://arxiv.org/pdf/1603.02754.pdf>`_

*Multilabel*

* `A Ranking-based KNN Approach for Multi-Label Classification <http://www.jmlr.org/proceedings/papers/v25/chiang12/chiang12.pdf>`_
* `Classification by Selecting Plausible Formal Concepts in a Concept Lattice <http://ceur-ws.org/Vol-977/paper5.pdf>`_
* `Large-scale Multi-label Learning with Missing Labels <http://jmlr.org/proceedings/papers/v32/yu14.pdf>`_
* `Multiclass-Multilabel Classification with More Classes than Examples <http://www.jmlr.org/proceedings/papers/v9/dekel10a/dekel10a.pdf>`_

*Digressions*

* `A Network That Learns Strassen Multiplication <http://www.jmlr.org/papers/volume17/16-074/16-074.pdf>`_
* `Learning Algorithms for Second-Price Auctions with Reserve <http://www.jmlr.org/papers/volume17/14-499/14-499.pdf>`_
* `Learning Theory for Distribution Regression <http://www.jmlr.org/papers/volume17/14-510/14-510.pdf>`_

Reinforcement Learning
++++++++++++++++++++++

|pystatpng|

*(année prochaine)*


*Lectures*

* `A Comprehensive Survey on Safe Reinforcement Learning <http://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf>`_
* `RLPy: A Value-Function-Based Reinforcement Learning Framework for Education and Research <http://www.jmlr.org/papers/volume16/geramifard15a/geramifard15a.pdf>`_



Deep Learning
+++++++++++++

|pystatpng|    


*Modèles pré-entraînés*

* `Places CNN <http://places.csail.mit.edu/downloadCNN.html>`_,
  `Pre-release of Places365-CNNs <https://github.com/metalbubble/places365>`_
  (deep learning)
  
*Lectures*

* `Deep Residual Learning for Image Recognition <https://arxiv.org/pdf/1512.03385v1.pdf>`_
* `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_, Yoshua Bengio, Ian Goodfellow and Aaron Courville
* `LeNet5 <http://yann.lecun.com/exdb/lenet/>`_
* `mxnet <https://github.com/dmlc/mxnet>`_
* `Benchmarking State-of-the-Art Deep Learning Software Tools <http://arxiv.org/pdf/1608.07249v5.pdf>`_
* `Wide & Deep Learning: Better Together with TensorFlow <https://research.googleblog.com/2016/06/wide-deep-learning-better-together-with.html>`_,
  `Wide & Deep Learning for Recommender Systems <https://arxiv.org/pdf/1606.07792v1.pdf>`_
* `To go deep or wide in learning? <http://www.jmlr.org/proceedings/papers/v33/pandey14.pdf>`_
* `Three Classes of Deep Learning Architectures and Their Applications: A Tutorial Survey <https://www.microsoft.com/en-us/research/publication/three-classes-of-deep-learning-architectures-and-their-applications-a-tutorial-survey/>`_
* `Tutorial: Learning Deep Architectures <http://www.cs.toronto.edu/~rsalakhu/deeplearning/yoshua_icml2009.pdf>`_
* `Deep Learning <https://en.wikipedia.org/wiki/Deep_learning>`_ (wikipédia)

    

Traitement du langage
=====================

|pyecopng| |pystatpng|


.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_nlp

*Lectures*

* `Système de complétion <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_nlp/completion.html>`_ :
  la complétion est utilisée par tous les sites Internet pour aider les utilisateurs
  à saisir leur recherche. N'importe quel site commercial l'utiliser
  pour guider les utilisateurs plus rapidement vers le produit qu'ils recherchent.
  

.. _l-2a-scraping:

Webscrapping et API
===================

|pyecopng| 

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_eco_scraping
    notebooks/_gs2a_eco_api
    
*Ressources*

* `API de geocoding <https://www.data.gouv.fr/fr/faq/reuser/>`_
* `adresse.data.gouv.fr <https://adresse.data.gouv.fr/csv/>`_

    
.. _l-cluster-non-struct-2a:

Big data sans cluster, données non structurées
==============================================

|pystatpng|

*Données structurées*

* `présentation données structurées <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_

*Données non structurées*

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_no_sql_exo
    notebooks/_gs2a_no_sql_twitter
    notebooks/_gs2a_big_in_memory


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


.. _l-2a-cplusplus-para-serie:

Parallélisation, C++, R, sérialisation
======================================

|pystatpng|

Notion abordées :

* techniques de parallélisation
* utiliser un autre langage pour accélérer les calculs
* sérialisation : le fait de convertir n'importe quelle structure de données en un
  tableau d'octets, c'est indispensable pour la communication entre deux machines,
  deux processus
  
.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_parallelisation
    notebooks/_gs2a_langages
    notebooks/_gs2a_serialisation
    notebooks/_gs1a_D_calcul_dicho_cython

*Lectures*

* :ref:`l-python_cplusplus`
  

Timeseries - Séries temporelles
===============================

.. toctree::
    :maxdepth: 2

    notebooks/_gs2a_timeseries
    
*Lectures*

* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* `Consistent Algorithms for Clustering Time Series <http://www.jmlr.org/papers/volume17/khaleghi16a/khaleghi16a.pdf>`_


.. _l-puzzlealgo2A:
      
Puzzles algorithmiques
======================

|pystatpng|


*Présentations*

* `Eléments d'Algorithmique <http://www.xavierdupre.fr/enseignement/complements/Seance4_algorithme.pdf>`_
* `Programmation dynamique <http://www.xavierdupre.fr/enseignement/complements/ENSAE_2A_jj_Seance2.pdf>`_
* `Graphes et algorithmes <http://www.xavierdupre.fr/enseignement/complements/ENSAE_2A_jj_Seance3.pdf>`_
    
*Notebooks*

Ces problèmes sont tirés de plusieurs sites dont
`Google Code Jam <https://code.google.com/codejam/contests.html>`_.

.. toctree::
    :maxdepth: 2
    
    notebooks/_gs2a_puzzle

      
*Lectures*

* types de complexité : `force brute <http://fr.wikipedia.org/wiki/Recherche_exhaustive>`_, 
  `glouton <http://fr.wikipedia.org/wiki/Algorithme_glouton>`_, `dynamique <http://fr.wikipedia.org/wiki/Programmation_dynamique>`_
* :ref:`l-algoculture`
* :ref:`l-expose-explication` 




.. _l-td2a-biblio:

Bibliographie
=============

**Livres sur le machine learning**

* `The Elements of Statistical Learning <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_, Trevor Hastie, Robert Tibshirani, Jerome Friedman
* `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_, Wes McKinney
* `Building Machine Learning Systems with Python <https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python>`_, Willi Richert, Luis Pedro Coelho
* `Learning scikit-learn: Machine Learning in Python <https://www.packtpub.com/big-data-and-business-intelligence/learning-scikit-learn-machine-learning-python>`_, Raúl Garreta, Guillermo Moncecchi
* `Modeling Creativity: Case Studies in Python <http://arxiv.org/abs/1410.0281>`_, Tom De Smedt
* `Critical Mass: How One Thing Leads to Another <http://www.philipball.co.uk/index.php?option=com_content&view=article&id=15:critical-mass-how-one-thing-leads-to-another&catid=3:books&Itemid=4>`_, Philip Ball
* `Bugra Akyildiz <http://bugra.github.io/>`_
* `Deep Learning <http://www-labs.iro.umontreal.ca/~bengioy/dlbook/>`_, Yoshua Bengio, Ian Goodfellow and Aaron Courville
* `Artificial Intelligence: A Modern Approach <http://aima.cs.berkeley.edu/>`_, Stuart Russell, Peter Norvig *(2016/08)*
* `Speech and Language Processing <http://www.cs.colorado.edu/~martin/slp.html>`_,  Daniel Jurafsky and James H. Martin *(2016/08)*,
  see also `Draft chapters in progress <https://web.stanford.edu/~jurafsky/slp3/>`_

**Livres sur les algorithmes**

* `Introduction to Algorithms <http://mitpress.mit.edu/books/introduction-algorithms>`_, Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein
* `The Algorithm Design Manual <http://www.algorist.com/>`_, Steven S. Skiena
* `Competitive Programming <http://www.comp.nus.edu.sg/~stevenha/myteaching/competitive_programming/cp1.pdf>`_, Steven Halim

**Livres sur la programmation**

* `High Performance Python <http://shop.oreilly.com/product/0636920028963.do>`_, Micha Gorelick, Ian Ozsvald.
   Le livre est très bien conçu et les exemples sont très clairs. Si vous souhaitez accélérer un programme Python
   en utilisant le multithreading, `OpenMP <http://openmp.org/wp/>`_, 
   `Numba <http://numba.pydata.org/>`_, `Cython <http://cython.org/>`_
   `PyPy <http://cython.org/>`_, ou `CPython <https://en.wikipedia.org/wiki/CPython>`_, 
   je recommande d'y jeter un coup d'oeil d'abord.

**Liens**

* `Python Scientific Lecture Notes <http://scipy-lectures.github.io/>`_
* `Introduction to Data Processing with Python <http://opentechschool.github.io/python-data-intro/>`_
* Quelques idées de livres : `Python for Data Scientists <https://www.packtpub.com/books/content/python-data-scientists>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_
* `Don't use Hadoop - your data isn't that big <http://www.chrisstucchio.com/blog/2013/hadoop_hatred.html>`_
* `A Roundup of Recent Text Analytics and Vis Work <http://blogger.ghostweather.com/2014/10/a-roundup-of-recent-text-analytics-and.html>`_
* `A Tour of Machine Learning Algorithms <http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/>`_
* `Efficient Estimation of Word Representations in Vector Space <http://arxiv.org/abs/1301.3781>`_, Tomas Mikolov, Kai Chen, Greg Corrado, Jeffrey Dean,
  `Distributed Representations of Words and Phrases and their Compositionality <http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf>`_, Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, Jeff Dean,
  `word2vec Parameter Learning Explained <http://arxiv.org/abs/1411.2738>`_, Xin Rong,
  `Tutorial on Auto-Encoders <http://piotrmirowski.wordpress.com/2014/03/27/tutorial-on-auto-encoders/>`_, Piotr Mirowski
* `Prédire les épidémies avec Wikipedia <http://www.lemonde.fr/sante/article/2014/11/13/predire-les-epidemies-avec-wikipedia_4523461_1651302.html>`_, Le Monde
* `FastML <http://fastml.com/>`_  (blog sur le machine learning)
* `Introduction to matplotlib <https://scipy-lectures.github.io/intro/matplotlib/matplotlib.html>`_
* `Probabilistic Context-Free Grammars (PCFGs) <http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf>`_
* `Ultimate guide for Data Exploration in Python using NumPy, Matplotlib and Pandas <http://www.analyticsvidhya.com/blog/2015/04/comprehensive-guide-data-exploration-sas-using-python-numpy-scipy-matplotlib-pandas/#One>`_
* `A Visual Introduction to Machine Learning <http://www.r2d3.us/visual-intro-to-machine-learning-part-1/>`_
* `Mathematical optimization: finding minima of functions <http://scipy-lectures.github.io/advanced/mathematical_optimization/index.html>`_
* `Out-of-Core Dataframes in Python: Dask and OpenStreetMap <https://jakevdp.github.io/blog/2015/08/14/out-of-core-dataframes-in-python/>`_ *(2015/12)*
* `Evaluation of Deep Learning Toolkits <https://github.com/zer0n/deepframeworks/blob/master/README.md>`_ *(2015/12)*
* `12 Algorithms Every Data Scientist Should Know <https://datafloq.com/read/12-algorithms-every-data-scientist-should-know/2024>`_ *(2016/06)*
* `10+2 Data Science Methods that Every Data Scientist Should Know in 2016 <http://tjo-en.hatenablog.com/entry/2016/04/18/190000>`_ *(2016/06)*
* `you can take the derivative of a regular expression?! <http://jvns.ca/blog/2016/04/25/how-regular-expressions-go-fast/>`_ *(2016/06)*
* `"Why Should I Trust You?" Explaining the Predictions of Any Classifier <http://arxiv.org/pdf/1602.04938v1.pdf>`_ *(2016/06)*
* `How to trick a neural network into thinking a panda is a vulture <https://codewords.recurse.com/issues/five/why-do-neural-networks-think-a-panda-is-a-vulture>`_ *(2016/06)*
* `Matrix Factorization: A Simple Tutorial and Implementation in Python <http://www.quuxlabs.com/blog/2010/09/matrix-factorization-a-simple-tutorial-and-implementation-in-python/>`_ *(2016/06)*
* `Complete Guide to Parameter Tuning in XGBoost (with codes in Python) <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/>`_ *(2016/08)*
* `colah's blog <http://colah.github.io/>`_ *(2016/08)* blog/cours sur le deep learning 
* `Factorization Machines with libFM <http://www.csie.ntu.edu.tw/~b97053/paper/Factorization%20Machines%20with%20libFM.pdf>`_ *(2016/09)*


**Tutoriels**

* `PyData Seattle 2015 Scikit-learn Tutorial <https://github.com/jakevdp/sklearn_pydata2015>`_ *(2015/12)*
* `Pythonic Perambulations <https://jakevdp.github.io/>`_ *(2015/12)*
* `Python Scripts posted on Kaggle <https://www.kaggle.com/scripts?language=Python>`_ *(2016/02)*
* `Pandas cookbook <https://github.com/jvns/pandas-cookbook>`_ *(2016/06)*
* `Machine Learning & Deep Learning Tutorials <https://github.com/ujjwalkarn/Machine-Learning-Tutorials>`_ *(2016/06)* :
  lien vers une liste assez longue de tutoriels, on y trouve aussi des *cheat sheets* comme
  `Probability Cheatsheet <http://static1.squarespace.com/static/54bf3241e4b0f0d81bf7ff36/t/55e9494fe4b011aed10e48e5/1441352015658/probability_cheatsheet.pdf>`_

**MOOC**

* `Machine Learning par Andrew Y. Ng <https://www.class-central.com/mooc/835/coursera-machine-learning>`_ 
  (les chapitres X et XI de la semaine 6 aborde la construction d'un système de machine learning).
* `Coursera Machine Learning <https://www.coursera.org/course/ml>`_
* `Coursera Machine Algorithm <https://www.coursera.org/course/algo>`_
* `CSE373 - Analysis of Algorithms - 2007 SBU <https://www.youtube.com/playlist?list=PL5F43156F3F22C349>`_
* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ (la liste des vidéos disponibles est en bas)

**Autres cours, notebooks**

* `CS109 Data Science (Harvard) <http://cs109.github.io/2014/>`_ - 
  `TD <https://github.com/cs109/content>`_ - 
  `Talks <http://cm.dce.harvard.edu/2015/01/14328/publicationListing.shtml>`_
* `Notes and assignments for Stanford CS class CS231n <https://github.com/cs231n/cs231n.github.io>`_ 
  `Convolutional Neural Networks for Visual Recognition <http://vision.stanford.edu/teaching/cs231n/>`_
* `Advanced Statistical Computing, Chris Fonnesbeck (Vanderbilt University) <http://nbviewer.jupyter.org/github/fonnesbeck/Bios366/tree/master/notebooks/>`_
* `CS 188: Artificial Intelligence (Berkeley) <http://inst.eecs.berkeley.edu/~cs188/fa10/lectures.html>`_ 
* `IAPR: Teaching materials for machine learning <http://homepages.inf.ed.ac.uk/rbf/IAPR/researchers/MLPAGES/mlteach.htm>`_
* machine learning et musique `Audio Content Analysis, teachings <http://www.audiocontentanalysis.org/teaching/>`_
* `ogrisel's notebook <https://github.com/ogrisel/notebooks>`_ (2016/04)
* `L'apprentissage profond <https://www.college-de-france.fr/site/yann-lecun/course-2015-2016.htm>`_, Yann LeCun au Collège de France *(2016/06)*
* `MA 2823 Foundations of Machine Learning (Fall 2016) <http://cazencott.info/index.php/pages/MA-2823-Foundations-of-Machine-Learning-%28Fall-2016%29>`_ *(2016/10)*

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
* `The Metropolis-Hastings algorithm <http://arxiv.org/abs/1504.01896>`_, Christian P. Robert
* `From RankNet to LambdaRank to LambdaMART: An Overview <http://research.microsoft.com/pubs/132652/MSR-TR-2010-82.pdf>`_, Christopher J.C. Burges

**Compétition de code**

* `Google Hash Code <https://hashcode.withgoogle.com/>`_, a lieu chaque année en deux tours, le second tour a lieu chez Google à Paris.
* `Google Code Jam <https://code.google.com/codejam>`_
* `TopCoder <http://www.topcoder.com/>`_
* `UVa Online Judge <http://uva.onlinejudge.org/>`_
* `Le problème des huit reines <http://zanotti.univ-tln.fr/algo/REINES.html>`_
* `Projet Euler <https://projecteuler.net/>`_

**Articles sur des librairies de machine learning**

* `XGBoost: A Scalable Tree Boosting System <http://arxiv.org/pdf/1603.02754v1.pdf>`_,
  Tianqi Chen, Carlos Guestrin


Pour finir, `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_ :

.. image:: http://scikit-learn.org/stable/_static/ml_map.png
    :width: 500
    

**Librairies Python**

* `Simple/limited/incomplete benchmark for scalability, speed and accuracy of machine learning libraries for classification <https://github.com/szilard/benchm-ml>`_
* `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
* `Related Projects (of machine learning) <http://scikit-learn.org/stable/related_projects.html>`_ (2016/03)

**Librairies de machine learning**

* `CNTK <https://github.com/Microsoft/CNTK>`_ (2016/04)
* `Keras <http://keras.io/>`_
* `scikit-learn <http://scikit-learn.org/stable/index.html>`_
* `TensorFlow <https://github.com/tensorflow/tensorflow>`_
* `theano <http://deeplearning.net/software/theano/>`_
* `Vowpal Wabbit <https://github.com/JohnLangford/vowpal_wabbit/wiki>`_
* `xgboost <https://github.com/dmlc/xgboost>`_

**Librairies de visualisation**

* `10 plotting libraries <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_
* :ref:`l-visualisation`
* `basemap <http://matplotlib.org/basemap/>`_, `phshp <https://pypi.python.org/pypi/pyshp>`_, `shapely <https://pypi.python.org/pypi/Shapely>`_ : 
  tout ce qu'il faut pour tracer des cartes

    
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
    :title: aborder d'autres librairies
    :tag: plus
    
    scikit-learn, h2o, xgboost, scikit-learn-contrib, mlxtend, gensim, 
    py-earth, polylearn, lightning, imbalanced-learn, theano, pytorch
    forest-confidence-interval, boruta, wendelin.core, zodb,
    (requires transaction, zc.lockfile, zodbpickle, ZODB, zdaemon, ZEO, ZODB3, wendelin.core),
    ghost.py (scrapping)
    h5py, PyTables, lda
    See `Related Projects <http://scikit-learn.org/stable/related_projects.html>`_,
    `Python extensions to do machine learning <http://www.xavierdupre.fr/blog/2013-09-15_nojs.html>`_
    
.. todoext::
    :title: Aborder theano, keras, GPU et les types de deep strucures
    :tag: plus
    
    Et les autres caffee, tensorflow, cntk, torch, h2o
    (voir `libraries <http://www.teglor.com/b/deep-learning-libraries-language-cm569/>`_,
    `librairies 1 <http://machinelearningmastery.com/popular-deep-learning-libraries/>`_,
    `librairies 2 <http://www.datasciencecentral.com/profiles/blogs/here-are-15-libraries-in-various-languages-to-help-implement-your>`_,
    `comparison <https://en.wikipedia.org/wiki/Comparison_of_deep_learning_software>`_
    et différents types de structures DNN, CNN
    `deep learning <https://en.wikipedia.org/wiki/Deep_learning>`_
    
.. todoext::
    :title: rédiger un ou deux notebook sur le traitement du langage
    :tag: plus
    
    Aborder la distance d'édition, n-grams, NLTK, gensim,
    word2vec, LDA (Latent Dirichlet Application), traduction statistique,
    td-idf, coocurrence, analyse de sentiment, stemming
    `SMT <https://en.wikipedia.org/wiki/Statistical_machine_translation>`_,
    alignement, 
    `moses <http://www.statmt.org/moses/>`_
    

.. todoext::
    :title: techniques de webscrapping
    :tag: plus
    
    * beautifulsoup, ghost.py, scrappy
    * structure de données JSON, HTML, XML
    * créer son site web Flask, `Falcon <https://falconframework.org/>`_, Django
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
    :title: ajouter un notebook sur numba, llvmlite
    :tag: plus
    
    Il n'y pas que CPython pour ooptimiser les calculs.
    Aborder les notions de JIT.
        
.. todoext::
    :title: sérialisation JSON
    :tag: plus
    
    Très utilisée sur internet donc incontournable.

.. todoext::
    :title: ajouter MILP
    :tag: plus
    
    avec des modules tels que `pyomo <http://www.pyomo.org/>`_,
    lire `Mixed integer programming for machine learning <http://www.litislab.fr/wp-content/uploads/2015/12/Canu-S.pdf>`_,
    `GLPK/Python <https://en.wikibooks.org/wiki/GLPK/Python#Python-GLPK>`_,
    `optlang <http://optlang.readthedocs.io/en/latest/>`_

.. todoext::
    :title: ajouter ctypes
    :tag: plus
    
    utilisation du module ctypes pour les import C++





    

    

.. [#fwrite1] Contributeur, encadrant et coordinateur du cours.

.. [#fwrite2] Contributeur, encadrant.
