# -*- coding: utf-8 -*-
"""
Send many mails
===============

Send mail to students. The script consider two columns from
one spreadsheets. The first one is about the receivers,
the second one about the customized message for each of them.
"""

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
sujet = "Commentaires Python pour un data scientist / économiste"
col_name = "Etudiant"
col_mail = "mail"
columns = ["Sujet", "Commentaires"]
col_group = "groupe"
delay_sending = False
check = None

skip = 0   # to start again after a failure

only = None
skiprows = 0

folder = os.path.normpath(os.path.abspath(os.path.join(
    *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", "ENSAE", "2017-2018", "2A_projet"]))))
student = os.path.join(folder, "Python2A-2018-01.xlsx")
if not os.path.exists(student):
    raise FileNotFoundError(student)

##############################
# début commun
begin = """
Bonjour,

""" + \
    """
Bonjour,

Je m'excuse d'avoir tant tardé à vous transmettre ces commentaires
pris par ceux qui vous ont lus vos travaux. Nous avons noté
le rapport sur 16 points et la vidéo sur 4. Je vous prie de m'excuser
pour les fautes d'orthographes qui sont sans doute encore présentes.
Vous êtes plus de 120 à avoir choisi ce cours pour plus de 75 projets
lus par quatre personnes.

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
df = pandas.read_excel(student, sheetname=0, skiprows=skiprows)

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

user = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "user")
pwd = keyring.get_password("gmail", os.environ["COMPUTERNAME"] + "pwd")

###################################
# On envoie les mails.
# Le paramètre delay_sending retourne une fonction qu'il suffit d'exécuter
# pour envoyer le mail.
# Si mailbox est None, la fonction affiche les résultats mais ne fait rien.


fLOG("connect", user)
mailbox = pymmails.sender.create_smtp_server("gmail", user, pwd)
fLOG("send")
# remplacer mailbox par None pour voir le premier mail sans l'envoyer
mails = enumerate_send_email(mailbox if not check else None,  # put None here to see the first mail
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
