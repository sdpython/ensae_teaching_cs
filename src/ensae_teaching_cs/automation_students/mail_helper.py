"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re
import os
from pyquickhelper import noLOG, run_cmd, remove_diacritics


def grab_mails(mailbox, emails, subfolder, date, no_domain=False, fLOG=noLOG):
    """
    look for some emails in a mail box
    from specific emails or sent to specific emails

    @param      mailbox         MailBoxImap object (we assume you are logged in)
    @param      emails          list of emails
    @param      date            date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder       folder of the mailbox to look into
    @param      no_domain       remove domain when searching for emails
    @param      fLOG            logging function
    @return                     list of emails
    """
    mid = {}
    res = []
    for m in emails:
        ms = m.split('@')[0] if no_domain else m
        ms = ms.strip()
        iter = mailbox.enumerate_search_person(ms, subfolder, date=date)
        mails = []
        for m in iter:
            if m["Message-ID"] not in mid:
                mails.append(m)
                mid[m["Message-ID"]] = m
        fLOG("looking for mail:", ms, ":", len(mails), " mails")
        res.extend(mails)
    return res


def get_mails_project(path,
                      mailbox,
                      subfolder,
                      date,
                      suivi="suivi.rst",
                      no_domain=False,
                      fLOG=noLOG):
    """
    This function extracts emails from a mailbox
    received from or sent to people and returns a list of thoses.

    @param      path        folder
    @param      mailbox     MailBoxImap object (we assume you are logged in)
    @param      suivi       filename for ``suivi.rst``
    @param      date        date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder   folder of the mailbox to look into
    @param      no_domain   remove domain when searching for emails
    @param      fLOG        logging function
    @return                 list of emails
    """
    allmails = get_emails(path, suivi)
    listmails = grab_mails(emails=allmails, mailbox=mailbox,
                           subfolder=subfolder, date=date, fLOG=fLOG,
                           no_domain=no_domain)
    return listmails


def dump_mails_project(path,
                       mailbox,
                       subfolder,
                       date,
                       suivi="suivi.rst",
                       dest="emails",
                       no_domain=False,
                       fLOG=noLOG):
    """
    This function extracts emails from a mailbox
    received from or sent to people

    The function expects to find a file ``suivi.rst`` which contains some emails addresses,
    it will look for mails and will dump them into the folder
    in HTML format.

    @param      path        folder
    @param      mailbox     MailBoxImap object (we assume you are logged in)
    @param      suivi       filename for ``suivi.rst``
    @param      dest        destination folder for the emails (relative to path)
    @param      date        date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder   folder of the mailbox to look into
    @param      no_domain   remove domain when searching for emails
    @param      fLOG        logging function
    @return                 list of created files

    @example(Automation___Grab all emails from students)

    The following program assumes each folder contains the files
    of a student project.

    It assumes each folder contains a file ``suivi.rst``
    and emails from students can be extracted with
    by searching the following regular expression:
    ``mails: ....``.
    Then it stores everything into the folder in
    subfolder called ``mails``.

    @code
    from ensae_teaching_cs.automation.project_helper import dump_mails_project
    imap = pymmails.MailBoxImap("gmail.account", "password", "imap.gmail.com", True)
    imap.login()

    sub = os.listdir(".")
    for fold in sub:
        print("***",fold)
        dump_mails_project(
                    os.path.abspath(fold),
                    imap,
                    subfolder = "ensae",
                    date = "1-Oct-2014",
                    no_domain=True,
                    fLOG=print)
    @endcode

    The function expects ``suivi.rst`` must be encoded in ``utf8``.

    @endexample
    """
    allmails = get_emails(path, suivi)

    fLOG("emails", allmails)
    listmails = grab_mails(emails=allmails, mailbox=mailbox,
                           subfolder=subfolder, date=date, fLOG=fLOG,
                           no_domain=no_domain)

    absdest = os.path.join(path, dest)
    fs = mailbox.dump_html(listmails, absdest)

    memo = []
    for mail, filename in fs:
        memo.append((mail.get_date(), filename, mail))
    memo.sort()

    index = os.path.join(path, "index_mail.html")
    with open(index, "w", encoding="utf8") as ff:
        ff.write("<html><body><h1>{0}</h1>\n".format(os.path.split(path)[-1]))
        ff.write("<ul>\n")
        for date, filename, mail in memo:
            fr = mail.get_from()[1]
            dt = date
            su = mail.get_field("subject")
            li = '<li><a href="{0}">{1} - from {2} - {3}</a></li>\n'.format(
                filename,
                dt,
                fr,
                su)
            ff.write(li)
        ff.write("</ul>\n")
        ff.write("</body></html>\n")

    return [_[1] for _ in memo] + [index]
