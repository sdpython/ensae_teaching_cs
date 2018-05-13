"""
@file
@brief A couple of functons which automates everything.
"""

import os
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import encrypt_stream
from pymmails import MailBoxImap, EmailMessageRenderer, EmailMessageListRenderer
from pymmails.render.email_message_style import template_email_html_short
from .projects_repository import ProjectsRepository
from .mail_helper import grab_addresses


def extract_students_mails_from_gmail_and_stores_in_folders(folder=".", filemails="emails.txt",
                                                            user=None, pwd=None, server="imap.gmail.com",
                                                            mailfolder=[
                                                                "ensae/ENSAE_2016_3A"],
                                                            date="1-Jan-2016", zipfilename="projet_3A_2016.zip",
                                                            zipencpwd=b"sixteenbyteskeys", dataframe=None,
                                                            columns={
                                                                "name": "nom_prenom", "group": "groupe", "subject": "sujet"},
                                                            skip_names=None, process_name=None,
                                                            title="List of emails", nolink_if=None, fLOG=fLOG):
    """
    The scenario is the following:

    * You are the teacher.
    * Students started their projects at date *t*.
    * They can work alone or by group.
    * They send mails, you reply.
    * Their address mail follows the convention: ``<first name>.<last name>@anything``
      so it is to associate a mail address to a student name.
    * You move every mail you received in a separate folder in your inbox.
    * Sometime, you send a mail to everybody.
    * Finally they send their project with attachments.
    * You want to store everything (mails and attachements) in folders, one per group.
    * You want a summary of what was received.
    * You want to build a zip file to share their work with others teachers.
    * You want to update the folder if a new mail was sent.

    This function looks into a folder of your inbox and grabs every mails and
    attachements from a groups of students.

    @param      folder              where to store the results
    @param      filemails           files used to store students address,
                                    the operation is done once, remove the file
                                    to force the function to rebuild the information.
    @param      user                user of the gmail inbox
    @param      pwd                 password of the gmail inbox
    @param      server              gmail server, it should be ``"imap.gmail.com"``,
                                    it works with others mail servers using the *IMAP* protocol
    @param      mailfolder          folder in your inbox to look into,
                                    there can be several
    @param      date                when to start looking (do not change the format,
                                    look at the default value)
    @param      zipfilename         name of the zip file to create
    @param      zipencpwd           the zip file is also encrypted for a safer share with this key
                                    and function `encrypt_stream <http://>`_.
    @param      dataframe           dataframe which contains the definition of students groups
    @param      columns             columns the function will look into, students names, group definition
                                    (a unique number for all students in the same group), subject
    @param      skip_names          list of names to skip
    @param      process_name        to operate a transformation before matching students names with
                                    their emails
    @param      title               each group folder contains a html file connecting them,
                                    this is its title
    @param      nolink_if           The summary extracts links from url, it skips the urls which
                                    contains on the substrings included in that list (None to use a default set)
    @param      fLOG                logging function
    @return                         :ref:`ProjectsRepository <ensae_teaching_cs.automation_students.projects_repository.ProjectsRepository>`

    By default, Gmail does not let you programmatically access you own inbox,
    you need to modify your gmail parameters to let this function do so.
    """
    folder = os.path.abspath(".")
    filemails = os.path.join(folder, filemails)
    zipfilename = os.path.join(folder, zipfilename)
    zipfilenameenc = zipfilename + ".enc"

    # load the groups
    if isinstance(dataframe, pandas.DataFrame):
        df = dataframe
    elif dataframe.endswith("xlsx"):
        fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] read dataframe", dataframe)
        df = pandas.read_excel(dataframe)
    else:
        df = pandas.read_csv(dataframe, sep="\t", encoding="utf8")

    # check mails
    if "mail" not in columns:
        if os.path.exists(filemails):
            fLOG(
                "[extract_students_mails_from_gmail_and_stores_in_folders] read addresses from ", filemails)
            with open(filemails, "r", encoding="utf8") as f:
                lines = f.readlines()
            emails = [l.strip("\r\t\n ") for l in lines]
        else:
            fLOG(
                "[extract_students_mails_from_gmail_and_stores_in_folders] mine address ")
            box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
            box.login()
            emails = grab_addresses(box, mailfolder, date, fLOG=fLOG)
            box.logout()

            with open(filemails, "w", encoding="utf8") as f:
                f.write("\n".join(emails))
    else:
        # nothing to do mail already present
        emails = set(df[columns["mail"]])

    # we remove empty names
    df = df[~df[columns["name"]].isnull()].copy()

    if process_name:
        df[columns["name"]] = df[columns["name"]].apply(
            lambda f: process_name(f))

    fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] create groups folders in", folder)
    proj = ProjectsRepository(folder, fLOG=fLOG)

    proj = ProjectsRepository.create_folders_from_dataframe(df, folder,
                                                            col_subject=columns[
                                                                "subject"], fLOG=fLOG, col_group=columns["group"],
                                                            col_student=columns[
                                                                "name"], email_function=emails, skip_if_nomail=False,
                                                            col_mail=columns["mail"], must_have_email=True, skip_names=skip_names)
    fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] nb groups", len(
        proj.Groups))

    # gathers mails
    email_render = EmailMessageRenderer(
        tmpl=template_email_html_short, fLOG=fLOG)
    render = EmailMessageListRenderer(title=title,
                                      email_renderer=email_render, fLOG=fLOG)

    box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
    box.login()
    proj.dump_group_mails(render, group=None, mailbox=box, subfolder=mailfolder, date=date,
                          overwrite=False, skip_if_empty=True)

    box.logout()

    # cleaning files
    for group in proj.Groups:
        files = list(proj.enumerate_group_files(group))
        att = [_ for _ in files if ".html" in _]
        if len(att) <= 1:
            fLOG(
                "[extract_students_mails_from_gmail_and_stores_in_folders] remove ", group)
            proj.remove_group(group)

    # unzip files and convert notebooks
    for group in proj.Groups:
        proj.unzip_convert(group)

    fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] summary ")
    summary = os.path.join(folder, "index.html")
    if os.path.exists(summary):
        os.remove(summary)
    proj.write_summary(nolink_if=nolink_if)

    fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] zip everything in", zipfilename)
    if os.path.exists(zipfilename):
        os.remove(zipfilename)
    proj.zip_group(None, zipfilename,
                   addition=["index.html", "mail_style.css", "emails.txt"])

    fLOG("[extract_students_mails_from_gmail_and_stores_in_folders] encrypt the zip file in", zipfilenameenc)
    if os.path.exists(zipfilenameenc):
        os.remove(zipfilenameenc)
    encrypt_stream(zipencpwd, zipfilename, zipfilenameenc, chunksize=2 ** 30)

    return proj
