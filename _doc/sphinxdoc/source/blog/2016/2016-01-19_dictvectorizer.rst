
.. blogpost::
    :title: DictVectorizer en un peu plus simple
    :keywords: machine learning, pipeline
    :date: 2016-01-19
    :categories: scikit-learn

    La classe `DictVectorizer <http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer>`_
    n'accepte pas de `DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_.
    Le code suivant n'est pas correct :

    ::

        import pandas
        from sklearn.feature_extraction import DictVectorizer

        vec = DictVectorizer()

        df = pandas.DataFrame( [{"cat": "a"}, {"cat": "b"}] )
        vec.fit_transform(df)  # plante ici

    Et on veut juste transformer le text en catégorie
    sans avoir besoin de transformer le DataFrame :

    .. runpython::
        :showcode:

        import pandas
        from ensae_teaching_cs.ml import CategoriesToIntegers
        df = pandas.DataFrame( [{"cat": "a"}, {"cat": "b"}] )
        trans = CategoriesToIntegers()
        trans.fit(df)
        newdf = trans.transform(df)
        print(newdf)

    Voir :ref:`CategoriesToIntegers <ensae_teaching_cs.ml.categories_to_integers.CategoriesToIntegers>`.
