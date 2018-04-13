# -*- coding: utf-8 -*-
"""
@file
@brief Arrays to display in notebooks.
"""
from io import StringIO
import pandas


def regex_cases():
    text = """
    Cas;Explications
    -------;Bases
    "a";a
    -------;Quantificateurs
    "abc?";ab suivi par 0 ou 1 c
    "abc*";ab suivi par 0.. c
    "abc+";ab suivi par 1.. c
    "abc{3}";ab suivi par 3 c
    "abc{3,5}";ab suivi par 3, 4 ou 5 c
    ;Groupes
    "(abc)+";1..8 abc
    "(a|b)c";ac ou bc
    -------;Intervalles (type 1)
    ".";n'importe quel caractère (un seul)
    "[aB9]";a ou B ou 9
    "[0-9]";n'importe quel caractère numérique
    "[a-zA-Z]";n'importe quel caractère alphabétique
    "[^a-c]";n'importe quel caractère SAUF a, b et c
    -------;Intervalles (type 2)
    "\\d";comme "[0-9]"
    "\\w";comme "[a-zA-Z0-9_]"
    "\\W";comme "[^a-zA-Z0-9_]"
    "\\s";espaces (" ", "\\n", "\\t", "\\r")
    "\\S";tout ce qui n'est pas un espace
    -------;Ancres
    "^abc";commence par "abc"
    "abc$";termine par "abc"
    """.replace("    ", "")
    df = pandas.read_csv(StringIO(text), sep=";").fillna('')
    return df
