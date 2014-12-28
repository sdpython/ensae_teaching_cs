"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re, os
import pymmails
from pyquickhelper import noLOG

_email_regex = re.compile("[*] *e?mails? *: *([^*]+)")

def grab_mails(mailbox, emails, subfolder, date, no_domain=False, fLOG = noLOG):
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
    res = [ ]
    for m in emails:
        ms = m.split('@')[0] if no_domain else m
        iter = mailbox.enumerate_search_person(ms, subfolder, date=date)
        mails = list(iter)
        mails = [ _ for _ in mails if _.body is not None and len(_.body) > 0 ]
        fLOG("looking for mail:", m, ":", len(mails), " mails")
        res.extend(mails)
    return res

def dump_mails_project(path, 
                    mailbox,
                    subfolder, 
                    date,
                    suivi = "suivi.rst", 
                    dest = "emails",
                    no_domain = False,
                    fLOG = noLOG):
    """
    This function extract emails from a mailbox 
    received from or sent to people
    
    The function expects to find a file ``suivi.rst`` which contains some emails addresses,
    it will look for mails and will dump them into the folder
    in HTML format.
    
    The function expects ``suivi.rst`` must be encoded in ``utf8``.
    
    @param      path        folder
    @param      mailbox      MailBoxImap object (we assume you are logged in)
    @param      suivi       filename for ``suivi.rst``
    @param      dest        destinaion folder for the emails (relative to path)
    @param      date        date (grab emails since ..., example ``1-Oct-2014``)
    @param      subfolder   folder of the mailbox to look into
    @param      no_domain   remove domain when searching for emails
    @param      fLOG        logging function
    @return                 list of created files
    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    filename = os.path.join( path, suivi)
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)
    
    with open(filename, "r", encoding="utf8") as f :
        content = f.read()
       
    global _email_regex
    mails = _email_regex.findall(content)
    if len(mails) == 0:
        raise Exception("unable to find the regular expresion {0} in {1}".format(_email_regex.pattern, filename))
    
    allmails = [ ]
    for m in mails:
        allmails.extend ( m.strip("\n\r\t ").split(";") )
    
    for a in allmails :
        ff = a.split("@")
        if len(ff) != 2:
            raise Exception("unable to understand mail {0} in {1} (mail separator is ;)".format(a, filename))

    fLOG("emails",allmails)
    listmails = grab_mails(emails = allmails, mailbox=mailbox, 
                           subfolder=subfolder, date=date, fLOG=fLOG,
                           no_domain=no_domain)
    
    absdest = os.path.join( path, dest)
    fs = mailbox.dump_html(listmails, absdest)
    
    memo = [ ]
    for mail,filename in fs:
        memo.append ( (mail.get_date(), filename, mail) )
    memo.sort()

    index = os.path.join(path, "index_mail.html")
    with open(index, "w", encoding="utf8") as ff:
        ff.write("<html><body><h1>{0}</h1>\n".format(os.path.split(path)[-1]))
        ff.write("<ul>\n")
        for date, filename, mail in memo:
            fr = mail.get_from()[1]
            dt = date
            su = mail.get_field("subject")
            li = '<li><a href="{0}">{1} - from {2} - {3}</a></li>\n'.format(filename, dt, fr, su)
            ff.write(li)
        ff.write("</ul>\n")
        ff.write("</body></html>\n")
        
    return [ _[1] for _ in memo ] + [ index ]
    