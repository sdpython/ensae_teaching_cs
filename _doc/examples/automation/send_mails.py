# -*- coding: utf-8 -*-
"""
Send many mails
===============

Send mail to students. The script consider two columns from
one spreadsheets. The first one is about the receivers,
the second one about the customized message for each of them.
"""

#########################################
# logging et import
import os
import warnings
from pyquickhelper.loghelper import fLOG
fLOG(OutputPrint=True)
from ensae_teaching_cs.automation_students import enumerate_feedback, enumerate_send_email
import pymmails

#########################################
# On définit le contenu du mail.

cc = []
sujet = "Question de code - ENSAE 1A - projet de programmation"
col_name = None  # "mail"
col_mail = "mail"
columns = ["sujet", "Question de code"]
col_group = "groupe"
delay_sending = False
test_first_mail = False  # regarder le premier mail avant de les envoyer
skip = 0   # to start again after a failure
only = None
skiprows = 1

folder = os.path.normpath(os.path.abspath(os.path.join(
    *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", "ENSAE", "2017-2018", "1A_projet"]))))
student = os.path.join(folder, "ENSAE 1A - projet python.xlsx")
if not os.path.exists(student):
    raise FileNotFoundError(student)

##############################
# début commun
begin = """
Bonjour,

""" + \
    """
Bonjour,

Voici les questions de code. Celles-ci sont
extraites des programmes que vous m'avez transmis.
Les noms de fonctions que j'utilise y font référence
quand je ne recopie pas le code. La réponse est souvent
liée à la performance.

""".replace("\n", " ")

#####################
# fin commune
end = """

""".replace("\n", " ") + \
    """

Xavier
"""

###################################
# Lecture des de la feuille Excel

import pandas
df = pandas.read_excel(student, sheet_name=0, skiprows=skiprows, engine='openpyxl')

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

with warnings.catch_warnings():
    warnings.simplefilter('ignore', DeprecationWarning)
    import keyring

user = keyring.get_password("gmail", "ensae_teaching_cs,user")
pwd = keyring.get_password("gmail", "ensae_teaching_cs,pwd")

###################################
# On envoie les mails.
# Le paramètre delay_sending retourne une fonction qu'il suffit d'exécuter
# pour envoyer le mail.
# Si mailbox est None, la fonction affiche les résultats mais ne fait rien.


fLOG("connect", user)
mailbox = pymmails.sender.create_smtp_server("gmail", user, pwd)
fLOG("send")
# remplacer mailbox par None pour voir le premier mail sans l'envoyer
mails = enumerate_send_email(mailbox if not test_first_mail else None,
                             sujet, user + "@gmail.com",
                             df, exc=True, fLOG=fLOG, delay_sending=delay_sending,
                             begin=begin, end=end, skip=skip,
                             cc=cc, only=only, col_group=col_group,
                             col_name=col_name, col_mail=col_mail,
                             cols=columns)

for i, m in enumerate(mails):
    fLOG("------------", m)

###################################
# fin
mailbox.close()
fLOG("Done")
