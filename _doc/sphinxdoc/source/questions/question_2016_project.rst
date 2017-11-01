
.. _question_projet_2016:

Questions 2016
==============

.. contents::
    :local:

.. _question_2016_projet_2A_json:

.. index:: json

Comment convertir un fichier *.txt* en *.json* ?
++++++++++++++++++++++++++++++++++++++++++++++++

Le format *json* est très utilisés par les sites internet car il est léger
et permet de représenter des `informations partiellement structurées <https://en.wikipedia.org/wiki/Semi-structured_data>`_.
Il ressemble beaucoup aux dictionnaires et aux listes en Python et à toute combinaison.
La fonction `to_json <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_json.html>`_
du module pandas permet de convertir facilement une table de données.

::

    import pandas
    df = pandas.read_csv("un_fichier.txt", sep="\t")
    df.to_json("results.json")
