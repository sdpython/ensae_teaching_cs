# -*- coding: utf-8 -*-
"""
@file
@brief  Quelques fonctions à propos de la première séance (2A)

"""

import pandas


def dfs2excel(dfs: dict, excel_file: str):
    """
    Aggrège plusieurs DataFrame dans un seul fichiers excel

    @param  dfs             dictionnaire  ``{ feuille: dataframe }``
    @param  excel_file      nom du fichier Excel
    @return                 ExcelWriter

    @example(science___Enregistrer plusieurs DataFrame dans un seul fichier Excel ?)

    Le code suivant enregistre deux DataFrame dans un seul fichier Excel.
    @code
    import pandas
    writer = pandas.ExcelWriter('example.xlsx')
    df1.to_excel(writer, 'Data 0')
    df2.to_excel(writer, 'Data 1')
    write.save()
    @endcode

    Ou en utilisant cette fonction :
    @code
    dfs2excel( { 'Data 0':df1, 'Data 1':df2 }, "example.xlsx" )
    @endcode
    @endexample

    @FAQ(pandas___Enregistrer plusieurs DataFrame dans un seul fichier Excel ?)

    Le code suivant enregistre deux DataFrame dans un seul fichier Excel.
    @code
    import pandas
    writer = pandas.ExcelWriter('example.xlsx')
    df1.to_excel(writer, 'Data 0')
    df2.to_excel(writer, 'Data 1')
    write.save()
    @endcode

    Ou en utilisant cette fonction :
    @code
    dfs2excel( { 'Data 0':df1, 'Data 1':df2 }, "example.xlsx" )
    @endcode
    @endFAQ

    """
    writer = pandas.ExcelWriter(excel_file)
    for k, df in dfs.items():
        df.to_excel(writer, k)
    writer.save()
    return writer
