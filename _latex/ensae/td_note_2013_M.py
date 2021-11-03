# coding:latin-1
import numpy
import td_note_2013_novembre_2012_exoM as exoM

fichier_zip = exoM.import_module_or_file_from_web_site(
    "equipements_sportif_2011.zip")
fichier_texte = exoM.unzip_fichier(fichier_zip)

# enlever le dernier paramètre 500 pour avoir le tableau complet
colonne, intitule, variables = exoM.construit_matrice(fichier_texte)

import numpy
intitule = numpy.array(intitule)
variables = numpy.array(variables)

# question 1, exo M (2 ou 3)
code_postaux = [intitule[i, 0][:2] for i in range(intitule.shape[0])]
intitule3 = numpy.column_stack((intitule, code_postaux))

# question 2, exo M (2 ou 3)
comptage = {}
for i in range(intitule3.shape[0]):
    comptage[intitule3[i, 2]] = 0
departements = [k for k in comptage]
departements.sort()

# question 3, exo M (2 ou 3)
D = numpy.zeros((len(departements), variables.shape[1]))
for i in range(len(departements)):
    d = departements[i]
    for j in range(variables.shape[1]):
        D[i, j] = variables[intitule3[:, 2] == d, j].sum()

# question 4, exo M (2 ou 3)
E = numpy.zeros(D.shape)
for i in range(E.shape[0]):
    E[i, :] = D[i, :] / D[i, 5]

# question 5, exo M (2 ou 3)
ginis = []
for j in range(E.shape[1]):
    li = list(E[:, j])
    gini = exoM.coefficient_gini(li)
    ginis.append((gini, colonne[0][j + 2]))
ginis.sort()
for line in ginis:
    print line

# les dernières lignes du tableau sont :
#(0.86910090569180598, 'Domaine skiable')
#(0.88139092467853186, 'Sports nautiques avec au moins une aire de pratique couverte')
#(0.89326137963164931, 'Domaine skiable - nombre de pistes')
#(0.9348918282098031,  'Parcours sportif avec au moins un parcours couvert')
#(0.93902978850018792, 'Domaine skiable avec au moins une piste \xe9clair\xe9e')
#(0.94625459043715754, '\xc9quipement de cyclisme avec au moins une piste couverte')
#(0.95743849241598267, 'Sports nautiques - nombre de places en tribune')
#(0.97248425032547758, 'Domaine skiable avec au moins une piste couverte')
#(0.97718065858676906, 'Parcours sportif - nombre de places en tribune')
#(0.98637386313881081, 'Terrain de golf - nombre de places en tribune')
#(0.98969072164948457, 'Domaine skiable - nombre de places en tribune')
