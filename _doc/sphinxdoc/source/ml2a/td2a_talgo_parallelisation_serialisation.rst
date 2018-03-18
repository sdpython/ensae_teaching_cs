
.. |pyecopng| image:: ../_static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: ../_static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pystatpng|

Parallélisation, sérialisation
++++++++++++++++++++++++++++++

La sérialisation est le fait de convertir n'importe quelle structure de données en un
tableau d'octets, c'est indispensable pour la communication entre deux machines, deux processus.

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_parallelisation
    ../notebooks/_gs2a_serialisation

*Modules*

* `dask <http://dask.pydata.org/en/latest/>`_
* `cytoolz <https://github.com/pytoolz/cytoolz>`_
* `joblib <https://pythonhosted.org/joblib/>`_

*Lectures*

* `Out-of-Core Dataframes in Python: Dask and OpenStreetMap <https://jakevdp.github.io/blog/2015/08/14/out-of-core-dataframes-in-python/>`_ *(2015/12)*
* `Combining random forest models in scikit learn <http://stackoverflow.com/questions/28489667/combining-random-forest-models-in-scikit-learn>`_
* `Better Python compressed persistence in joblib <http://gael-varoquaux.info/programming/new_low-overhead_persistence_in_joblib_for_big_data.html>`_
