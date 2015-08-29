# -*- coding: utf-8 -*-
"""
@file
@brief Quelques problèmes récurrents avec `pandas <http://pandas.pydata.org/>`_.
"""


def read_csv(filepath_or_buffer, encoding="utf8", sep="\t", **args):
    """
    Calls function `read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html?highlight=read_csv#pandas.read_csv>`_
    with different defaults values. If the encoding is utf8 and the data is a file name, the function
    checks there is no BOM at the beginning. Otherwise, it uses the encoding ``utf-8-sig``.

    @param      encoding                encoding
    @param      filepath_or_buffer      filepath_or_buffer
    @param      sep                     column separator
    @return                             DataFrame

    @FAQ(pandas___Caractères bizarres en utf8 et sous Windows (BOM) ?)

    .. index:: encoding, BOM, UTF8

    Sous Windows, certains logiciels comme `Notepad <http://fr.wikipedia.org/wiki/Bloc-notes_%28Windows%29>`_
    permettent d'enregister un fichier sous différents `encodings <http://en.wikipedia.org/wiki/Character_encoding>`_.
    Avec l'encoding `UTF8 <http://fr.wikipedia.org/wiki/UTF-8>`_, on a parfois un problème avec le premier caractère
    ``\\ufeff`` car Notepad ajoute ce qu'on appelle un `BOM <http://fr.wikipedia.org/wiki/Indicateur_d%27ordre_des_octets>`_.
    Par exemple ::

        import pandas
        df = pandas.read_csv("dataframe.txt",sep="\\t", encoding="utf8")
        print(df)

    Provoque une erreur des plus énervantes ::

        UnicodeEncodeError: 'charmap' codec can't encode character '\\ufeff' in position 0: character maps to <undefined>

    Pour contrecarrer ceci, il suffit de modifier l'encoding par `utf-8-sig <https://docs.python.org/3.4/library/codecs.html#encodings-and-unicode>`_ ::

        import pandas
        df = pandas.read_csv("dataframe.txt",sep="\\t", encoding="utf-8-sig")
        print(df)

    @endFAQ
    """
    import pandas
    if isinstance(filepath_or_buffer, str):
        if encoding in ["utf8", "utf-8"]:
            try:
                df = pandas.read_csv(
                    filepath_or_buffer,
                    encoding=encoding,
                    sep=sep,
                    **args)
                if df.columns[0].startswith("\ufeff"):
                    raise UnicodeError(
                        "'charmap' codec can't encode characters in position 0-1325: character maps to <undefined>")
                return df
            except UnicodeError:
                df = pandas.read_csv(
                    filepath_or_buffer,
                    encoding="utf-8-sig",
                    sep=sep,
                    **args)
                return df
            except UnicodeDecodeError:
                df = pandas.read_csv(
                    filepath_or_buffer,
                    encoding="utf-8-sig",
                    sep=sep,
                    **args)
                return df
        else:
            return pandas.read_csv(
                filepath_or_buffer, encoding=encoding, sep=sep, **args)
    else:
        return pandas.read_csv(
            filepath_or_buffer, encoding=encoding, sep=sep, **args)


def df_to_clipboard(df, **args):
    """
    Copy a dataframe as csv text into the clipboard

    @param      df      dataframe
    @param      sep     by default the separator is ``\\t`` for this function until it is defined otherwise

    It relies on method
    `to_clipboard <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_clipboard.html>`_.

    @FAQ(pandas___Copier un dataframe dans le presse-papier - clipboard)

    Pour récupérer un dataframe dans Excel, on peut utiliser la méthode
    `to_excel <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html>`_
    puis ouvrir le fichier dans Excel ou le copier dans le presse-papier et le coller
    dans une feuille ouverte dans Excel. C'est l'objet de la méthode
    `to_clipboard <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_clipboard.html>`_ ::

        df = pandas.DataFrame ( ... )
        df.to_clipboard(sep="\\t")

    @endFAQ
    """
    if "sep" in args:
        df.to_clipboard(**args)
    else:
        df.to_clipboard(sep="\t", **args)


def df_equal(df1, df2):
    """
    compares two dataframe and tells if they are equal

    @param          df1     first dataframe
    @param          df2     second dataframe
    @return                 boolean

    The function compare column one by one.
    It does not check the order of the columns is the same.
    It reorders the columns before doing the comparison.

    If you need more complex comparison,
    you can look into function `assert_frame_equal <https://github.com/pydata/pandas/blob/master/pandas/util/testing.py>`_.

    The function does not handle well NaN values because ``numpy.nan != numpy.nan`` is true.
    It also compares types:

    @FAQ(pandas___Comment comparer deux dataframe?)

    Ecrire ``df1 == df2`` ne compare pas deux dataframes entre deux
    car le sens n'est pas forcément le même pour tout le monde.
    Même si les valeurs sont les mêmes, est-ce l'ordre des colonnes
    est important ?
    Il faut donc le faire soi-même. Le code ci-dessus
    compare d'abord les dimensions, ensuite compare l'ordre
    des colonnes puis enfin les valeurs ::

        if df1.shape != df2.shape:
            return False
        l1 = list(df1.columns)
        l2 = list(df2.columns)
        l1.sort()
        l2.sort()
        if l1 != l2:
            return False
        df1 = df1[l1]
        df2 = df2[l2]
        t = (df1 == df2).all()
        s = set(t)
        return False not in s

    @endFAQ
    """
    if df1.shape != df2.shape:
        return False
    l1 = list(df1.columns)
    l2 = list(df2.columns)
    l1.sort()
    l2.sort()
    if l1 != l2:
        return False
    df1 = df1[l1]
    df2 = df2[l2]
    s = set((df1.dtypes == df2.dtypes))
    if False in s:
        return False
    s = set((df1 == df2).all())
    return False not in s


def groupby_topn(df, by_keys, sort_keys, ascending=True, n=1, as_index=True):
    """
    takes the top n rows per group

    @param      df          dataframe
    @param      by_keys     rows will be grouped by these columns
    @param      sort_keys   rows will be sorted by these columns
    @param      ascending   parameter associated to sord function
    @param      n           n in top *n*
    @param      as_index    if False, remove the index after the group by
    @return                 result

    @FAQ(pandas___top n lignes avec pandas)

    Grouper puis garder les premières observations de ce groupe est un problème
    classique. Il n'existe pas de meilleure façon de le faire,
    cela dépend du nombre d'obervations par groupe. Le moyen le plus simple
    de le faire avec pandas est :

    * grouper les lignes
    * trier les lignes dans chaque groupe
    * garder les premières lignes dans chaque groupe

    Ceci donne ::

        df.groupby(by_keys)
          .apply(lambda x: x.sort(sort_keys, ascending=ascending).head(head))
          .reset_index(drop=True)

    La dernière instruction supprimer l'index ce qui donne au dataframe final
    la même structure que le dataframe initial.

    .. runpython::
        :showcode:

        import pandas
        l = [ dict(k1="a", k2="b", v=4, i=1),
              dict(k1="a", k2="b", v=5, i=1),
              dict(k1="a", k2="b", v=4, i=2),
              dict(k1="b", k2="b", v=1, i=2),
              dict(k1="b", k2="b", v=1, i=3)]
        df = pandas.DataFrame(l)
        df.groupby(["k1", "k2"]).apply(lambda x: x.sort(["v", "i"], ascending=True).head(1))

    @endFAQ
    """
    res = df.groupby(by_keys).apply(lambda x: x.sort(
        sort_keys, ascending=ascending).head(n))
    if not as_index:
        res = res.reset_index(drop=True)
    return res
