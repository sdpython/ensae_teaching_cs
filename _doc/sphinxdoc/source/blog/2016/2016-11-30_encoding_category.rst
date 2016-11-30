

.. blogpost::
    :title: Tranformer les variables catégorielles et contrastes
    :keywords: categorie, scikit-learn
    :date: 2016-11-30
    :categories: machine learning
    :lid: encoding-categorie-id
    
    Certains modèles de machine learning requiert de transformer les variables catégorielles
    en variables numériques. Il existe plusieurs façons de faire cela :
    `Patsy: Contrast Coding Systems for categorical variables <http://statsmodels.sourceforge.net/devel/contrasts.html>`_.
    Les `extensions de scikit-learn <https://github.com/scikit-learn-contrib/>`_
    incluent un module qui fait cela aussi mais façon 
    `scikit-learn <http://scikit-learn.org/>`_ :
    `category_encoders <https://github.com/scikit-learn-contrib/categorical-encoding>`_
    implémente les transformations suivantes :
    
    * `Backward Difference Coding <http://contrib.scikit-learn.org/categorical-encoding/backward_difference.html>`_ :
      Voir `Backward Difference Coding <http://www.ats.ucla.edu/stat/sas/webbooks/reg/chapter5/sasreg5.htm#backward>`_
    * `Binary <http://contrib.scikit-learn.org/categorical-encoding/binary.html>`_ :
      cette transformation est identique à *One Hot* mais toutes les colonnes sont regroupées
      en une seule. Chaque nombre a une représentation binaire identique aux colonnes regroupées.
    * `Hashing <http://contrib.scikit-learn.org/categorical-encoding/hashing.html>`_ :
      chaque catégorie est transformée en *hash*. Cela veut dire chaque catégorie est transformée 
      en une chaîne de caractères de longueur fixe. On peut ajuster le hash de telle sorte
      que plusieurs catégories seront encodées de la même manière si le nombre
      de catégories est trpo grand.
    * `Helmert Coding <http://contrib.scikit-learn.org/categorical-encoding/helmert.html>`_ :
      Voir `Helmert <http://www.ats.ucla.edu/stat/sas/webbooks/reg/chapter5/sasreg5.htm#helmert>`_.
    * `One Hot <http://contrib.scikit-learn.org/categorical-encoding/onehot.html>`_ :
      chaque catégorie devient une colonne à part entière qui prend ses valeurs dans :math:`\{0,1\}`
      indiquant si l'observation fait partie de cette catégorie ou non.
      Si la catégorie est renseignée à chaque fois, la somme de ces colonnes fait toujours
      1. Le nouveau jeu de données peut poser des problèmes pour toutes les méthodes
      supposant que la matrice des covariances est inversible.
    * `Ordinal <http://contrib.scikit-learn.org/categorical-encoding/ordinal.html>`_ :
      convertit les catégories en entier stocké dans une seule colonne.
    * `Polynomial Coding <http://contrib.scikit-learn.org/categorical-encoding/polynomial.html>`_ :
      Voir `Orthogonal Polynomial Coding <http://www.ats.ucla.edu/stat/sas/webbooks/reg/chapter5/sasreg5.htm#ORTHOGONAL>`_.
    * `Sum Coding <http://contrib.scikit-learn.org/categorical-encoding/sum.html>`_ :
      Voir `Sum (Deviation) Coding <http://statsmodels.sourceforge.net/devel/contrasts.html#sum-deviation-coding>`_.
      
    L'idée de base derrière tous ces schémas est la notion de *contraste*. On souhaite affecter
    à chaque catégorie une valeur réelle qui soit en adéquation avec le problème de machine learning
    considéré et celles-ci sont estimées en fonction de la variable *Y* à prédire, le plus souvent
    avec une régression linéaire.
    
    Voir également `Coding schemes covered <http://www.ats.ucla.edu/stat/r/library/contrast_coding.htm>`_.