# coding:latin-1
import math
import sys

# extrait les données depuis un site internet, puis les écrit à côté du programme
# ne fait rien si le fichier a déjà été téléchargé


def import_module_or_file_from_web_site(module):
    import os
    if os.path.exists("data\\equipement_sportifs_2011\\" + module):
        return "data\\equipement_sportifs_2011\\" + module
    if not os.path.exists(module):
        url = "http://www.xavierdupre.fr/enseignement/complements/" + module
        import urllib2
        if module.lower().endswith("zip"):
            f = urllib2.urlopen(url, "rb")
            t = f.read()
            f.close()
            f = open(module, "wb")
            f.write(t)
            f.close()
        else:
            f = urllib2.urlopen(url)
            t = f.read()
            f.close()
            f = open(module, "w")
            f.write(t)
            f.close()
    return module

# extrait le fichier texte contenu dans le fichier zip
# et l'enregistre à côté du programme
# ne fait rien si cela est déjà fait


def unzip_fichier(fichier_zip):
    import zipfile
    import os
    file = zipfile.ZipFile(fichier_zip, "r")
    res = None
    for info in file.infolist():
        filename = info.filename
        res = filename
        if not os.path.exists(filename):
            data = file.read(filename)
            f = open(filename, "w")
            if sys.version.startswith("3."):
                data = str(data, encoding="iso-8859-1")
                data = data.replace("\r", "").split("\n")
                data = [_ for _ in data if len(_) > 1]
                data = "\n".join(data)
            f.write(data)
            f.close()
    file.close()
    return res

# construit le tableau extrait du fichier précédent
# les deux premières lignes contiennent la description des colonnes
# les autres lignes contiennent les données elles-même
# pour aller plus vite à chaque exécution, on peut limiter le nombre de lignes
# il faudra toutes les utiliser pour l'exécution final


def construit_matrice(fichier, stop_apres=-1):
    def float_except(x):
        try:
            return float(x)
        except:
            return -1
    f = open(fichier, "r")
    lines = [line.replace("\n", "").split("\t")[:107]
             for line in f.readlines()[:stop_apres]]
    f.close()
    colonne = lines[:2]
    lines = lines[2:]
    lines = [line[:2] + [float_except(x) for x in line[2:]]
             for line in lines if len(line) > 5]
    intitule = [line[:2] for line in lines]
    lines = [line[2:] for line in lines]
    return colonne, intitule, lines


def coefficient_gini(valeurs):
    # voir http://fr.wikipedia.org/wiki/Coefficient_de_Gini
    valeurs.sort()
    gini = 0
    s = 0
    for (i, v) in enumerate(valeurs):
        gini += (i + 1) * v
        s += v
    gini = 2 * gini / (len(valeurs) * s) - (len(valeurs) + 1.0) / len(valeurs)
    return gini


if __name__ == "__main__":
    fichier_zip = import_module_or_file_from_web_site(
        "equipements_sportif_2011.zip")
    fichier_texte = unzip_fichier(fichier_zip)

    # enlever le dernier paramètre 500 pour avoir le tableau complet
    colonne, intitule, variables = construit_matrice(fichier_texte, 500)

    import numpy
    intitule = numpy.array(intitule)
    variables = numpy.array(variables)

    # affichage des colonnes
    for i in range(len(colonne[0])):
        print(i, colonne[0][i], " --- ", colonne[1][i])

    # utilisation de numpy pour sélectionner des lignes spécifiques
    print(intitule[intitule[:, 1] == "Chevroux", :])
    print(variables[intitule[:, 1] == "Chevroux", :])
