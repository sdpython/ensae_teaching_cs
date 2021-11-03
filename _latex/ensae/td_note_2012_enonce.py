# coding:latin-1
import urllib
import os
import os.path
import numpy


def charge_donnees(nom="donnees_enquete_2003_television.txt"):
    if os.path.exists(nom):
        # si le fichier existe (il a déjà été téléchargé une fois)
        f = open(nom, "r")
        text = f.read()
        f.close()
    else:
        # si le fichier n'existe pas
        link = "http://www.xavierdupre.fr/enseignement/td_python/" + \
            "python_td_minute/data/examen/" + nom
        url = urllib.urlopen(link)
        text = url.read()
        # on enregistre les données pour éviter de les télécharger une seconde fois
        f = open(nom, "w")
        f.write(text)
        f.close()

    lines = text.split("\n")
    lines = [l.split("\t") for l in lines if len(l) > 3]
    lines = [["0" if s.strip() == "" else s for s in l] for l in lines]
    return lines
