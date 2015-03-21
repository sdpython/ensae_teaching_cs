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
