# -*- coding: utf-8 -*-
"""
Send many mails
===============

Send mail to students. The script consider two columns from
one spreadsheets. The first one is about the receivers,
the second one about the customized message for each of them.
"""

#########################################
# Cette section ajoute des chemins pour des modules que je développe
# et que je n'installe jamais. Je pourrais me servir d'un environnement
# virtuel mais en pratique, c'est toujours un peu compliqué
# de mettre le mettre à jour en permanence.

import os
import sys

this = os.path.abspath(os.path.dirname(__file__))
if "ensae_teaching_cs" in this:
    this = this.split("ensae_teaching_cs")[0].rstrip("\\/")
for module in ["jyquickhelper", "pyquickhelper", "pyensae",
               "pyrsslocal", "pymmails", "pymyinstall",
               "ensae_teaching_cs"]:
    try:
        exec("import %s" % module)
    except ImportError:
        p = os.path.join(this, module, "src")
        print("add path", p)
        sys.path.append(p)
        exec("import %s" % module)

#########################################
# logging

from pyquickhelper.loghelper import fLOG  # publish_lectures
fLOG(OutputPrint=True)

#########################################
# import des fonctions dont on a besoin
from ensae_teaching_cs.automation_students import enumerate_feedback, enumerate_send_email
import pymmails

#########################################
# On définit le contenu du mail.

cc = []
sujet = "Python pour un data scientist / économiste, feedback sur le projet"
only = None
skip = 0
folder = os.path.normpath(os.path.abspath(os.path.join(
    *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", "ENSAE", "2016-2017", "1A_pitch"]))))
student = os.path.join(folder, "Python_1A_pitch_2017_reviews.xlsx")
if not os.path.exists(student):
    raise FileNotFoundError(student)

##############################
# début commun
begin = """
Bonjour,

""" + \
    """
Voici mes remarques suite à la lecture de votre pitch.

""".replace("\n", " ")

#####################
# fin commune
end = """

""".replace("\n", " ") + \
    """

Je te laisse transférer ce mail aux autres membres du groupes s'il y a en a.
Je m'excuse pour ce retard.

Xavier
"""

###################################
# Lecture des de la feuille Excel

import pandas
df = pandas.read_excel(student, sheetname=0, skiprows=0)

if len(df.columns) < 4:
    raise ValueError("Probably an issue while reading the spreadsheet:\n{0}\n{1}".format(
        df.columns, df.head()))
if len(" ".join(df.columns).split("Unnamed")) > 4:
    raise ValueError("Probably an issue while reading the spreadsheet:\n{0}\n{1}".format(
        df.columns, df.head()))
fLOG("shape", df.shape)
fLOG("columns", df.columns)

###################################
# mot de passe

import keyring
user = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "user")
pwd = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "pwd")

###################################
# On envoie les mails.
# Le paramètre delay_sending retourne une fonction qu'il suffit d'exécuter
# pour envoyer le mail.
# Si mailbox est None, la fonction affiche les résultats mais ne fait rien.

col_name = "Noms"
col_mail = "nom_prenom"
columns = ["sujet", "observation"]
delay_sending = False

fLOG("connect", user)
mailbox = pymmails.sender.create_smtp_server("gmail", user, pwd)
fLOG("send")
# remplacer mailbox par None pour voir le premier mail sans l'envoyer
mails = enumerate_send_email(mailbox,
                             sujet, user + "@gmail.com",
                             df, exc=True, fLOG=fLOG, delay_sending=delay_sending,
                             begin=begin, end=end, skip=skip,
                             cc=cc, only=only, col_group=None,
                             col_name=col_name, col_mail=col_mail,
                             cols=columns)

for i, m in enumerate(mails):
    fLOG("------------", m)

###################################
# fin
mailbox.close()
fLOG("Done")
