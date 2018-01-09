"""
@file
@brief Some automation helpers to grab mails from student about project.
"""

from pyquickhelper.loghelper import noLOG
from pymmails import MailBoxImap


def grab_addresses(mailbox, subfolder, date, no_domain=False, max_dest=5, names=False, fLOG=noLOG):
    """
    Looks for some emails in a mail box
    from specific emails or sent to specific emails.

    @param      mailbox         MailBoxImap object (we assume you are logged in)
    @param      date            date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder       folder of the mailbox to look into
    @param      no_domain       remove domain when searching for emails
    @param      max_dest        number of receivers to have a valid mail
    @param      names           if true, return suggestions for names for each mail
    @param      fLOG            logging function
    @return                     list of emails or tuple(list of emails, dictionary(email: name)) if names is True

    .. exref::
        :title: Collect email addresses from mails in an inbox folder)
        :tag: Automation

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
    """
    emails = mailbox.enumerate_mails_in_folder(
        subfolder, date=date, body=False)
    res = []
    suggestions = {}
    for i, mail in enumerate(emails):
        if i % 25 == 0:
            if len(suggestions) == 0:
                fLOG("[grab_addresses] {0} collected {1}".format(i, len(res)))
            else:
                fLOG("[grab_addresses] {0} collected {1} names {2}".format(
                    i, len(res), len(suggestions)))
        tos = mail.get_to()
        cc = mail.get_to(cc=True)
        if cc:
            tos.extend(cc)
        if max_dest > 0 and len(tos) <= max_dest:
            tos = [(m[1].split('@')[0] if no_domain else m[1])
                   for m in tos if m and m[1]]
            res.extend(tos)
        frs = [mail.get_from()]
        frs = [(m[1].split('@')[0] if no_domain else m[1])
               for m in frs if m and m[1]]
        if names:
            identity = mail.get_name()
            if identity is not None:
                for m in frs:
                    if m not in suggestions:
                        suggestions[m] = {identity}
                    elif identity not in suggestions[m]:
                        suggestions[m].add(identity)
        res.extend(frs)
    res = list(sorted(set(res)))
    return (res, suggestions) if names else res


def extract_students_mail_and_name_from_gmail(user=None, pwd=None, server="imap.gmail.com", mailfolder=["ensae/actuariat"],
                                              date="1-Jan-2016", fLOG=noLOG):
    """
    Extracts mails and names from a mail box.

    @param      user                user of the gmail inbox
    @param      pwd                 password of the gmail inbox
    @param      server              gmail server, it should be ``"imap.gmail.com"``,
                                    it works with others mail servers using the *IMAP* protocol
    @param      mailfolder          folder in your inbox to look into,
                                    there can be several
    @param      date                when to start looking (do not change the format,
                                    look at the default value)
    @param      fLOG                logging function
    @return                         list of dictionary ``[{"name": ..., "mail": ...}]``
    """
    box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
    box.login()
    emails, suggestions = grab_addresses(
        box, mailfolder, date, names=True, fLOG=fLOG)
    box.logout()

    rows = []
    for mail in emails:
        el = {"mail": mail}
        if mail in suggestions:
            el["name"] = ";".join(sorted(suggestions[mail]))
        rows.append(el)
    return rows
