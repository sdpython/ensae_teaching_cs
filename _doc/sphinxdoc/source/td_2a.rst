
.. _l-td2a:


2A
==

**Données, Machine Learning et Programmation**

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

    
- :ref:`TD 1 : Données et Graphes <td2acenoncesession1rst>` (:ref:`correction <td2acorrectionsession1rst>`)
    - import/export de données dans un DataFrame
    - manipulation selon une logique SQL
    - utilité des index
    - lambda function
    - premiers graphiques
- TD 2
    - :ref:`TD 2A : Calcul Matriciel, Optimisation <td2acenoncesession2arst>` (:ref:`correction <td2acorrectionsession2arst>`)
    - :ref:`TD 2B : Python autres langages <td2acenoncesession2brst>` (:ref:`correction <td2acorrectionsession2brst>`)
    - :ref:`TD 2C : IPython et commandes magiques <td2acenoncesession2crst>` (:ref:`correction <td2acorrectionsession2crst>`)
    - :ref:`TD 2D : IPython et calcul distribué <td2acenoncesession2drst>` (:ref:`correction <td2acorrectionsession2drst>`)
    
La séance 3 aura pour thème le `machine learning <http://en.wikipedia.org/wiki/Machine_learning>`_. On le 
traduit en français par `apprentissage statistique <http://fr.wikipedia.org/wiki/Apprentissage_automatique>`_. 
Les deux modules principaux sont `statsmodels <http://statsmodels.sourceforge.net/devel/index.html>`_
et `scikit-learn <>`_.


- TD 3
    - :ref:`TD 3A : Statistiques descriptives <td2acenoncesession3arst>` (:ref:`correction <td2acorrectionsession3arst>`)
    - Présentation de `Gaël Varoquaux <http://gael-varoquaux.info/>`_ : machine learning et `scikit-learn <http://scikit-learn.org/stable/>`_
        - `tutoriels sur scikit-learn <http://nbviewer.ipython.org/github/GaelVaroquaux/sklearn_pandas_tutorial/tree/master/rendered_notebooks/>`_
        - Quelques extraits :
            - Par définition les plus proches voisins ne font pas d'erreur sur la base d'apprentissage, l'apprentissage consiste à forcer le modèle à faire des erreurs.
            - `Overfitting <http://en.wikipedia.org/wiki/Overfitting>`_ et `régularisation <http://en.wikipedia.org/wiki/Regularization_(mathematics)>`_
            - Erreur `L2 <http://en.wikipedia.org/wiki/Lp_space>`_ et pénalisation `L1 <http://fr.wikipedia.org/wiki/Espace_L1>`_
            - `RandomizedPCA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.RandomizedPCA.html>`_, `GridSearch <http://scikit-learn.org/stable/modules/grid_search.html>`_, `LassoCV <http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html>`_
            - `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_
    - :ref:`TD 3B : Arbres de décision et Random Forests <td2acenoncesession3brst>`  (:ref:`correction <td2acorrectionsession3brst>`)
    
- TD 4
    - :ref:`TD 4A : Machine Learning et Marketting <td2acenoncesession4arst>` (:ref:`correction <td2acorrectionsession4arst>`)
        - machine learning
        - `d3.js <http://d3js.org/>`_
    - :ref:`Bien démarrer un projet de machine learning <debutermlprojet>`_
    - :ref:`TD 4B : Culture algorithmique <td2acenoncesession4brst>` (:ref:`correction <td2acorrectionsession4brst>`)
        - `Machine learning et algorithme <http://www.xavierdupre.fr/blog/2014-10-11_nojs.html>`_
        - :ref:`exerciceplusgrandesommerst`
    
    
Les données non structurées et de grandes tailles seront l'objet de la séance 5.


La dernière séance sera consacrée à des problèmes d'algorithmie dont la connaissance
est souvent utile lorsqu'il s'agit d'être astucieux avec les données.


**Bibliographie**

* `The Elements of Statistical Learning <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_, Trevor Hastie, Robert Tibshirani, Jerome Friedman
* `Python for Data Analysis <http://shop.oreilly.com/product/0636920023784.do>`_, Wes McKinney
* `Building Machine Learning Systems with Python <https://www.packtpub.com/big-data-and-business-intelligence/building-machine-learning-systems-python>`_, Willi Richert, Luis Pedro Coelho
* `Learning scikit-learn: Machine Learning in Python <https://www.packtpub.com/big-data-and-business-intelligence/learning-scikit-learn-machine-learning-python>`_, Raúl Garreta, Guillermo Moncecchi
* `Modeling Creativity: Case Studies in Python <http://arxiv.org/abs/1410.0281>`_, Tom De Smedt
* `Critical Mass: How One Thing Leads to Another <http://www.philipball.co.uk/index.php?option=com_content&view=article&id=15:critical-mass-how-one-thing-leads-to-another&catid=3:books&Itemid=4>`_, Philip Ball

**Liens**

* `Python Scientific Lecture Notes <http://scipy-lectures.github.io/>`_
* `Introduction to Data Processing with Python <http://opentechschool.github.io/python-data-intro/>`_
* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* Quelques idées de livres : `Python for Data Scientists <https://www.packtpub.com/books/content/python-data-scientists>`_
* `Quelques astuces pour faire du machine learning <http://www.xavierdupre.fr/blog/2014-03-28_nojs.html>`_

**MOOC**

* `Machine Learning par Andrew Y. Ng <https://www.class-central.com/mooc/835/coursera-machine-learning>`_
* `Coursera Machine Learning <https://www.coursera.org/course/ml>`_

**Articles d'auteurs très connus**

* `Latent Dirichlet Allocation <http://ai.stanford.edu/~ang/papers/jair03-lda.pdf>`_, David M. Blei, Andrew Y. Ng, Michael I. Jordan 
* `Analysis of a Random Forests Model <http://www.jmlr.org/papers/volume13/biau12a/biau12a.pdf>`_, Gerard Biau
* `Adaptivity of Averaged Stochastic Gradient Descent to Local Strong Convexity for Logistic Regression <http://jmlr.csail.mit.edu/papers/volume15/bach14a/bach14a.pdf>`_, Francis Bach
* `Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising <http://jmlr.csail.mit.edu/papers/volume14/bottou13a/bottou13a.pdf>`_, Léon Bottou, Jonas Peter et Al.
* `Tutorial on Practical Prediction Theory for Classification <http://www.jmlr.org/papers/volume6/langford05a/langford05a.pdf>`_, John Langford
* `Sparse Online Learning via Truncated Gradient <http://jmlr.org/papers/volume10/langford09a/langford09a.pdf>`_, John Langford, Lihong Li, Tong Zhang


Pour finir, `Choosing the right estimator <http://scikit-learn.org/stable/tutorial/machine_learning_map/>`_ :

.. image:: http://scikit-learn.org/stable/_static/ml_map.png
    :width: 500

.. toctree::
    :hidden:
    
    td_2a_enonce
    td_2a_correction

    
