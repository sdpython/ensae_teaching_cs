# -*- coding: utf-8 -*-
"""
Exécuter des scripts python envoyé en pièce jointe
==================================================

Script utilisé pour exécuter des scripts python envoyés en pièces
jointes par des étudiants. Ces programmes sont récupérés par
le script :ref:`fetch_student_projects_from_gmail.py <script-fetch-students-projets-py>`.

.. _script-execute-script:
"""

#########################################
# import
import sys
import os
import pandas

#########################################
# logging
from pyquickhelper.loghelper import fLOG  # execute_student_projects
fLOG(OutputPrint=True)

#########################################
# import des fonctions dont on a besoin
from ensae_teaching_cs.automation_students.interro_motif import execute_python_scripts, _get_code

###########################
# paramètre du programme
neworder = "nom_prenom key pattern_id cmp motif_dans_sortie sortie_dans_motif dist time size program err out content url".split()
dest_folder = os.path.normpath(os.path.abspath(os.path.join(
    *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", "ENSAE", "2016-2017", "1A_november"]))))
# expected outputs
url = "http://www.xavierdupre.fr/enseignement/examens/1A_2016/enonce_{0}.txt"
excel_filename = os.path.join(dest_folder, "exo_1A_2016.xlsx")
out_filename = os.path.join(dest_folder, "results_2016.xlsx")

###########################
# fonctions générant différentes versions de noms ou prénoms


def gen_mail(mail):
    yield mail
    yield mail.lower()
    yield mail.replace("-paristech", "")
    yield mail.lower().replace("-paristech", "")


###########################
# lecture du fichier récupéré par le script
# fetch_student_projects_from_gmail.py
input = pandas.read_excel(excel_filename)

###########################
# exécution des scripts
col_names = dict(folder="nom_prenom", mail="nom_prenom")
df = execute_python_scripts(".", input, col_names=col_names, url=url,
                            fLOG=fLOG, gen_mail=gen_mail, eol="/")

###########################
# enregistrement des résultats
print(df.columns)
df = df[neworder]
df.to_excel(out_filename)

#########################
# construction d'un résumé
short = df["nom_prenom key pattern_id cmp dist time size program".split()]
short = short["nom_prenom dist".split()].groupby(
    "nom_prenom", as_index=False).min()
total = df.merge(short, on="nom_prenom", suffixes=("", "_2"))
print(total.shape)
print(short.shape)
print(df.shape)
total = total[total.dist == total.dist_2]
total["OK"] = total.dist <= 1
print(total.shape)
new_total = total.groupby("nom_prenom").first()
new_total.to_excel(out_filename + ".summary.xlsx")
