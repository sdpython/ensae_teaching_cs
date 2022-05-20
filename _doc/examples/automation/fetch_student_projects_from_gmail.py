# -*- coding: utf-8 -*-
"""
Récupérer des mails d'étudiants en pièce jointe (1:1)
=====================================================

Récupère des fichiers en pièce jointe provenant d'étudiants comme un rendu de projet.
Le programme suppose qu'il n'y en a qu'un par étudiant, que tous les mails ont été
archivés dans un répertoire d'une boîte de message, ici :epkg:`gmail`.
Il faut supprimer le contenu du répertoire pour mettre à jour l'ensemble
des projets. Dans le cas contraire, le code est prévu pour mettre à jour le répertoire
à partir des derniers mails recensés dans le fichiers *mails.txt*.
La récupération se passe souvent en deux étapes.
La première récupère tous les mails et crée un premier archivage
sans tenir compte des groupes. On créé alors un fichier :epkg:`Excel`
qui ressemble à peu près à ceci :

.. runpython::

    from pandas import DataFrame
    df = DataFrame(dict(groupe=[1, 1, 2], mail=['a.a@m', 'b.b@m', 'c.c@m'],
                        sujet=['sub1', 'sub1', 'sub2']))
    print(df)

On efface tout excepté ce fichier puis on récupère une seconde fois
tous les projets afin de ne créer qu'un répertoire par groupe.

.. _script-fetch-students-projets-py:
"""

#########################################
# import
import sys
import os
import pandas
import warnings
from pyquickhelper.loghelper import get_password

#################################
# Paramètres de la récupération,
# tous les mails doivent être dans le même répertoire
# de la boîte de message.

server = "imap.gmail.com"
school = "ENSAE"
date = "20-Apr-2022"
year = '1A'
exam = 'projet'
pattern = "Python_{0}_{1}".format(year, exam)
group_def = "groupes.xlsx"
col_subject, col_group, col_mail, col_student = "sujet", "groupe", "mail", "Nom"
final_dest = ["2021-2022", "{}-{}".format(year, exam)]


if school == 'ENSAE':
    do_mail = True
    mailfolder = ["ensae/ENSAE_%s" % year]
    dest_folder = os.path.normpath(os.path.abspath(os.path.join(
        *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", school] + final_dest))))
    print("dest", dest_folder)
elif school == 'ASSAS':
    do_mail = True
    mailfolder = ["ensae/assas"]
    dest_folder = os.path.normpath(os.path.abspath(os.path.join(
        *([os.path.dirname(__file__)] + ([".."] * 5) + ["_data", "ecole", school] + final_dest))))
    print("dest", dest_folder)
else:
    raise NotImplementedError()

###########################
# End of customization.

path_df = os.path.join(dest_folder, group_def)
if os.path.exists(path_df):
    df_group = pandas.read_excel(path_df, engine='openpyxl')
    for col in [col_subject, col_mail, col_group, col_student]:
        if col not in df_group.columns:
            raise Exception('{0} not in {1}'.format(
                col, list(df_group.columns)))
else:
    df_group = None

basename = pattern.format(mailfolder[0].split("/")[-1])
filename_zip = os.path.join(dest_folder, basename + ".zip")
convert_files = True

filename_mails = os.path.join(dest_folder, "emails.txt")
filename_excel = os.path.join(dest_folder, basename + ".xlsx")

#########################################
# Creates the folder if it does not exist.

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

#########################################
# Logging et import des fonctions dont on a besoin.

from pyquickhelper.loghelper import fLOG  # fetch_student_projects_from_gmail
fLOG(OutputPrint=True)

from ensae_teaching_cs.automation_students import ProjectsRepository, grab_addresses
from pyquickhelper.filehelper import encrypt_stream
from pymmails import MailBoxImap, EmailMessageRenderer, EmailMessageListRenderer
from pymmails.render.email_message_style import template_email_html_short

###########
# Identifiants.

user = get_password("gmail", "ensae_teaching_cs,user")
pwd = get_password("gmail", "ensae_teaching_cs,pwd")
password = get_password("enc", "ensae_teaching_cs,pwd")
if user is None or pwd is None or password is None:
    print("ERROR: password or user or crypting password is empty, you should execute:")
    print(
        'set_password("gmail", "ensae_teaching_cs,user", "..")')
    print(
        'set_password("gmail", "ensae_teaching_cs,pwd", "..")')
    print(
        'set_password("enc", "ensae_teaching_cs,pwd", "..")')
    print("Exit")
    sys.exit(0)

password = bytes(password, "ascii")

print([user, pwd, password])

###########
# Les adresses à éviter...
skip_address = {
    'xavier.dupre@gmail.com',
    'xavier.dupre@ensae.fr',
    'xavierdupre@gmail.com',
}


###############
# Gathers mails and creates a dataframe if it does not exist.

fLOG("[fetch_student_projects_from_gmail] start")

if df_group is None:
    if os.path.exists(filename_mails):
        with open(filename_mails, "r", encoding="utf8") as f:
            lines = f.readlines()
        emails = [l.strip("\r\t\n ") for l in lines]
        emails = [_ for _ in emails if _ not in skip_address]
    else:
        box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
        box.login()
        emails = grab_addresses(box, mailfolder, date, fLOG=fLOG)
        box.logout()
        emails = list(sorted(set([_.strip("<>").lower()
                                  for _ in emails if _ not in skip_address])))
        emails = [_ for _ in emails if _ not in skip_address]
        allmails = "\n".join(emails)
        with open(filename_mails, "w", encoding="utf8") as f:
            f.write(allmails)
else:
    emails = [_ for _ in df_group[col_mail] if _ not in skip_address]


#####################
# Creates a dataframe.

if df_group is None:
    import pandas
    rows = [{col_mail: mail, col_subject: "?", col_group: i + 1,
             col_student: mail.split('@')[0]} for i, mail in enumerate(emails)]
    df = pandas.DataFrame(rows)
    fLOG("[fetch_student_projects_from_gmail] dataframe", df.shape)
    df.to_excel(filename_excel)
else:
    df = df_group

##################################
# Creates folders for each student or group.

mappings = {}
folder = dest_folder

proj = ProjectsRepository(folder, fLOG=fLOG)
groups = proj.Groups
if do_mail or len(groups) < 10:
    fLOG("[fetch_student_projects_from_gmail] create list of groups")
    proj = ProjectsRepository.create_folders_from_dataframe(
        df, folder, col_subject=col_subject,
        col_group=col_group, col_mail=col_mail,
        email_function=emails, skip_if_nomail=False,
        must_have_email=True, fLOG=fLOG,
        col_student=col_student)
elif len(groups) < 10:
    fLOG("[fetch_student_projects_from_gmail] skip fetching mails: {0} groups already".format(
        len(groups)))
fLOG("[fetch_student_projects_from_gmail] nb groups", len(proj.Groups))

#############
# dump mails

if do_mail:
    email_render = EmailMessageRenderer(
        tmpl=template_email_html_short, fLOG=fLOG)
    render = EmailMessageListRenderer(title="list of mails",
                                      email_renderer=email_render, fLOG=fLOG)

    box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
    box.login()
    mails = proj.dump_group_mails(render, group=None,
                                  mailbox=box, subfolder=mailfolder, date=date,
                                  overwrite=False, convert_files=convert_files)
    box.logout()

################
# write summary

if True:
    fLOG("[fetch_student_projects_from_gmail] summary")
    index = os.path.join(dest_folder, "index.html")
    if os.path.exists(index):
        os.remove(index)
    proj.write_run_command()
    proj.write_summary()


#################
# zip everything

if True:
    if os.path.exists(filename_zip):
        os.remove(filename_zip)
    proj.zip_group(None, filename_zip,
                   addition=[index, os.path.join(dest_folder, "mail_style.css"),
                             filename_excel, filename_mails])

############
# encryption

if True:
    fLOG("[fetch_student_projects_from_gmail] encryption")
    enc = filename_zip.replace(".zip", ".enc")
    encrypt_stream(password, filename_zip, enc, chunksize=2**30)
