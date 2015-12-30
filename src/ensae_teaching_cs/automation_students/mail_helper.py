"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re
import os
from pyquickhelper import noLOG, run_cmd, remove_diacritics


def grab_addresses(mailbox, subfolder, date, no_domain=False, max_dest=5, fLOG=noLOG):
    """
    look for some emails in a mail box
    from specific emails or sent to specific emails

    @param      mailbox         MailBoxImap object (we assume you are logged in)
    @param      date            date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder       folder of the mailbox to look into
    @param      no_domain       remove domain when searching for emails
    @param      max_dest        number of receivers to have a valid mail
    @param      fLOG            logging function
    @return                     list of emails

    @example(AutoTeachings___Collect email addresses from mails in an inbox folder)

    ::

        from ensae_teaching_cs.automation_students import grab_addresses
        from pymmails import MailBoxImap

        user = "xavier.dupre"
        pwd = "***"
        server = "imap.gmail.com"
        mailfolder = ["ensae/ENSAE_2016", "ensae/ensae_interro_2015"]
        date = "1-Dec-2015"

        box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
        box.login()
        emails = grab_addresses(box, mailfolder, date, fLOG=fLOG)
        box.logout()

    @endexample
    """
    emails = mailbox.enumerate_mails_in_folder(
        subfolder, date=date, body=False)
    mid = {}
    res = []
    for mail in emails:
        tos = mail.get_to()
        if max_dest > 0 and len(tos) <= max_dest:
            tos = [(m[1].split('@')[0] if no_domain else m[1])
                   for m in tos if m and m[1]]
            res.extend(tos)
        frs = [mail.get_from()]
        frs = [(m[1].split('@')[0] if no_domain else m[1])
               for m in frs if m and m[1]]
        res.extend(frs)
    res = list(sorted(set(res)))
    return res
