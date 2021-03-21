
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-td2a-manip:

========================
Agilité avec les données
========================

Faire du machine learning veut d'abord dire
être capable de manipuler les données comme bon vous semble
et les représenter à l'aide de graphiques.

.. contents::
    :local:

.. |pyecopng| image:: _static/pyeco.png
            :height: 20
            :alt: Economie
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
            :height: 20
            :alt: Statistique
            :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

|pyecopng| |pystatpng|

DataFrame
+++++++++

*Notebooks*

.. toctree::
    :maxdepth: 1

    ../notebooks/td2a_cenonce_session_1
    ../notebooks/td2a_correction_session_1
    ../notebooks/pandas_iterator
    ../notebooks/pandas_iterator_correction
    ../notebooks/td2a_eco_exercices_de_manipulation_de_donnees
    ../notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_a
    ../notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_b
    ../notebooks/td2a_eco_exercices_de_manipulation_de_donnees_correction_c
    ../notebooks/2020_carte

*Modules*

* `pandas <http://pandas.pydata.org/>`_
* `py-polars <https://github.com/ritchie46/polars>`_
* `csvkit <https://csvkit.readthedocs.io/en/latest/index.html>`_
* `geopandas <https://geopandas.org/>`_
  (pour manipuler des coordonnées géographiques)

*Modules - grands jeux de données*

* `pandas_streaming <https://github.com/sdpython/pandas_streaming/>`_
* `vaex <https://docs.vaex.io/en/latest/installing.html>`_
* `py-polars <https://github.com/ritchie46/polars>`_

*Optimisation*

* `swifter <https://github.com/jmcarpenter2/swifter>`_ :
  optimisation des lambdas de :epkg:`pandas`
* `modin.dataframe <https://github.com/modin-project/modin>`_ :
  cette implémentation des dataframes copie l'interface de :epkg:`pandas`
  mais propose des implémentations parallélisées sur une ou plusieurs
  machines (:epkg:`xarray`, :epkg:`dask`)
