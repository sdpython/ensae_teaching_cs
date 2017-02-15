
.. blogpost::
    :title: Combiner des random forest
    :keywords: scikit-learn, machine learning, random forest
    :date: 2017-02-15
    :categories: machine learning

    C'est une astuce que m'ont fait découvrir deux étudiants dans leur
    projet associé au cours de troisième année :ref:`l-td3a`.
    Ils ont utilisé une propriété rendue possible par l'implémentation
    des `random forest <http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_
    de `scikit-learn <http://scikit-learn.org/>`_ : il est possible de construire
    une random forest issue de l'assemblage de deux random forest.
    De là à paralléliser l'apprentissage d'une random forest,
    il n'y a qu'un pas. L'article en question :
    `Combining random forest models in scikit learn <http://stackoverflow.com/questions/28489667/combining-random-forest-models-in-scikit-learn>`_.
