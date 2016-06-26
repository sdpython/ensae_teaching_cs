# -*- coding: utf-8 -*-
"""
@file
@brief Sérialization

"""

import pickle


def df2list(df):
    """
    converts a dataframe into a list of lists

    @param      df      DataFrame
    @return             list of lists

    @FAQ(Convertir un DataFrame en une liste de listes ?)
    @code
    df = DataFrame( ... )
    l  = df.values.tolist()
    @endcode
    @endFAQ

    @FAQ(Comment vérifier que deux DataFrame sont égaux ?)
    Comparer deux `DataFrame <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html>`_
    avec l'opérateur ``==`` ne fonctionne pas.
    On obtient un message d'erreur ::

        ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

    Il faut au préalable convertir le Dataframe en le convertissant en liste ::

        df.values.tolist() == df2.values.tolist()

    @endFAQ
    """
    return df.vales.tolist()


def dump_object(obj, filename_or_stream):
    """
    Sérialize un objet dans un stream ou un fichier

    @param      obj                     objet à sérialiser
    @param      filename_or_stream      nom de fichier ou stream

    @FAQ(Comment gagner du temps lors de la lecture de données ?)

    .. index:: sérialisation, pickle, dill

    Les languages informatiques définissent des structures de données
    qui permettent une utilisation rapide et cela n'a souvent rien
    à voir avec la façon dont on lit ces données.
    La plupart des données apparaissent dans des fichiers
    texte ou fichiers plat. Pour les utiliser, le programme les
    charges en mémoires ce qui peut prendre du temps.
    La première fois qu'on s'en sert, c'st inévitable.
    La seconde fois, on peut stocker les données
    telles qu'elles sont en mémoire.
    Le second chargement est plus rapide.

    @code
    obj = ... # n'importe quoi de sérialisable
    dump_object(obj, "object_sur_disque.bin")
    @endcode

    Pour recharger les données, on écrit :

    @code
    obj = load_object("object_sur_disque.bin")
    @endcode

    Le code de ces deux fonctions fait intervenir
    le module `pickle <https://docs.python.org/3/library/pickle.html>`_.
    Il suffit pour la plupart des usages.
    Pour un usage plus exotique, il faut voir le module
    `dill <https://pypi.python.org/pypi/dill>`_.

    @endFAQ
    """
    if isinstance(filename_or_stream, str):
        stream = open(filename_or_stream, "wb")
        close = True
    else:
        stream = filename_or_stream
        close = False

    pickle.dump(obj, stream)

    if close:
        stream.close()


def load_object(filename_or_stream):
    """
    Charge un objet en mémoire après qu'il a été sérialisé

    @param      filename_or_stream      nom de fichier ou stream
    @return                             objet
    """
    if isinstance(filename_or_stream, str):
        stream = open(filename_or_stream, "rb")
        close = True
    else:
        stream = filename_or_stream
        close = False

    obj = pickle.load(stream)

    if close:
        stream.close()

    return obj
