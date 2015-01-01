"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re, os
import pymmails
from pyquickhelper import noLOG, run_cmd

_email_regex  = re.compile("[*] *e?mails? *: *([^*]+)")
_gitlab_regex = re.compile("[*] *gitlab *: *([^*]+[.]git)")

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
        fLOG("looking for mail:", m, ":", len(mails), " mails")
        res.extend(mails)
    return res

def get_emails(path, suivi = "suivi.rst"):
    """
    retrieve student emails from file ``suivi.rst``
    
    @param      path            sub folder to look into
    @param      suivi           name of the file ``suivi.rst``
    @return                     list of mails
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
        raise Exception("unable to find the regular expression {0} in {1}".format(_email_regex.pattern, filename))

    allmails = [ ]
    for m in mails:
        allmails.extend ( m.strip("\n\r\t ").split(";") )

    for a in allmails :
        ff = a.split("@")
        if len(ff) != 2:
            raise Exception("unable to understand mail {0} in {1} (mail separator is ;)".format(a, filename))

    return allmails

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

    @param      path        folder
    @param      mailbox      MailBoxImap object (we assume you are logged in)
    @param      suivi       filename for ``suivi.rst``
    @param      dest        destinaion folder for the emails (relative to path)
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
    
def git_url_user_password(url_https, user, password):
    """
    builds a url (starting with https) and add the user and the password
    to skip the authentification
    
    @param      url_https       example ``https://gitlab.server/folder/project_name``
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @return                     url
    """
    url_user = url_https.replace("https://", "https://{0}:{1}@".format(user, password))
    return url_user
    
def git_check_error(out, err, fLOG):
    """
    private function, analyse the output
    """
    if len(out) > 0 : 
        fLOG("OUT:\n" + out)
    if len(err) > 0 : 
        if "error" in err.lower():
            raise Exception("OUT:\n{0}\nERR:\n{1}".format(out,err))
        fLOG("ERR:\n" + err)    
    
def git_clone(
            local_folder, 
            url_https,
            user = None, 
            password = None, 
            timeout = 60,
            init = True,
            fLOG = noLOG):
    """
    clone a project from a git repository in a non empty local folder,
    it requires `GIT <http://git-scm.com/>`_ to be installed 
    and uses the command line.
    
    @param      local_folder    local folder of the project
    @param      url_https       url, example ``https://gitlab.server/folder/project_name``
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @param      timeout         timeout for the command line
    @param      init            see below (True, use fetch, False, use clone)
    @param      fLOG            logging function
    @return                     local_folder
    
    If the reposity has already been cloned, it does not do it again.
    We assume that git can be run without giving its full location.
    
    The function executes the following commands (if init is True)::
    
        cd [folder]
        git init
        git remote add origin [https://user.password@server/project.git]
        git fetch
        
    Otherwise, it does::
        
        cd [folder]
        git clone origin [https://user.password@server/project.git]
        git fetch
        
    A folder will be created.
        
    """
    url_user = git_url_user_password(url_https, user, password)
    timeout = 60
    local_folder = os.path.normpath(os.path.abspath(local_folder))
    
    if init:
        if not os.path.exists(local_folder):
            fLOG("creating folder", local_folder)
            os.mkdir(local_folder)
            
        hg = os.path.join(local_folder, ".git")
        if not os.path.exists(hg):
            cmds= """
                    cd {0}
                    git init
                    git remote add origin {1}
                    git fetch
                    """.format(local_folder, url_user).replace("                    ","").strip(" \n\r\t")
            cmd = cmds.replace("\n","&")
            sin = "" #"{0}\n".format(password)
            out, err = run_cmd(cmd, sin=sin,wait=True, timeout=timeout)
            git_check_error(out, err, fLOG)
        
        return local_folder
    else:
        if not os.path.exists(local_folder):
            raise FileNotFoundError(local_folder)
        hg = os.path.join(local_folder, ".git")
        if os.path.exists(hg):
            raise Exception("folder {0} should not exists (init is True)".format(local_folder))
            
        final = os.path.split(url_user)[-1].replace(".git","")
        locf = os.path.join(local_folder, final)
        if os.path.exists(locf):
            raise Exception("folder {0} should not exists before cloning".format(locf))
            
        cmds= """
                cd {0}
                git clone {1}
                """.format(local_folder, url_user).replace("                ","").strip(" \n\r\t")
        cmd = cmds.replace("\n","&")
        sin = "" #"{0}\n".format(password)
        out, err = run_cmd(cmd, sin=sin,wait=True, timeout=timeout)
        git_check_error(out, err, fLOG)
        
        return locf
        
def git_change_remote_origin(
                        local_folder, 
                        url_https,
                        user = None, 
                        password = None,
                        timeout = 10,
                        fLOG = noLOG
                        ):
    """    
    Change the origin of the repository. The url and the password
    refer to the new repository.
    
    @param      local_folder   local folder
    @param      url_https       url, example ``https://gitlab.server/folder/project_name``
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @param      timeout         timeout for the command line
    @param      fLOG            logging function
    @return                     something
    
    The function runs the instruction::
    
        git remote remove origin
        git remote add origin url
        
    """
    url_user = git_url_user_password(url_https, user, password)
    cmds= """
            cd {0}
            git remote remove origin
            git remote add origin {0}
            """.format(local_folder, url_user).replace("                ","").strip(" \n\r\t")
    cmd = cmds.replace("\n","&")
    sin = "" #"{0}\n".format(password)
    out, err = run_cmd(cmd, sin=sin,wait=True, timeout=timeout)
    git_check_error(out, err, fLOG)
        
def git_commit_all(
            local_folder, 
            url_https,
            message,
            user = None, 
            password = None,
            timeout = 300,
            fLOG = noLOG):
    """
    from a git repository,
    it requires `GIT <http://git-scm.com/>`_ to be installed 
    and uses the command line.
    
    @param      local_folder    local folder of the project
    @param      url_https       url, example ``https://gitlab.server/folder/project_name``
    @param      message         message for the commit
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @param      timeout         timeout for the command line
    @param      fLOG            logging function
    @return                     None
    
    If the reposity has already been cloned, it does not do it again.
    We assume that git can be run without giving its full location.
    
    The function executes the following commands::
    
        cd [folder]
        git add -A
        git commit -m "[message]"
        git push -u origin master
    
    """
    #url_user = git_url_user_password(url_https, user, password)
    cmds= """
            cd {0}
            git add -A
            git commit -m "{1}"
            git push -u origin master
            """.format(local_folder, message).replace("                ","").strip(" \n\r\t")
    cmd = cmds.replace("\n","&")
    sin = "" #"{0}\n".format(password)
    out, err = run_cmd(cmd, sin=sin,wait=True, timeout=timeout)
    git_check_error(out, err, fLOG)
        
def git_first_commit_all_projects(
            local_folder,
            user = None, 
            password = None,
            timeout = 300,
            suivi = "suivi.rst",
            fLOG = noLOG):
    """
    @param      local_folder    folder
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @param      timeout         timeout for the command line
    @param      suivi           file to open to get the gitlab account
    @param      fLOG            logging function
    @return                     None or ( local_folder, gitlab )
    """
    if not os.path.exists(local_folder):
        raise FileNotFoundError(local_folder)
    filename = os.path.join( local_folder, suivi)
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    with open(filename, "r", encoding="utf8") as f :
        content = f.read()

    global _gitlab_regex
    gitlab = _gitlab_regex.findall(content)
    if len(gitlab) == 0:
        raise Exception("unable to find the regular expression {0} in {1}".format(_gitlab_regex.pattern, filename))
    if not isinstance (gitlab, list):
        raise TypeError("we expect a list for: " + str(gitlab))
    if len(gitlab) != 1:
        raise Exception("more than one gitlab repo is mentioned {0} in {1}".format(_gitlab_regex.pattern, filename))
    gitlab = gitlab[0]
    
    fLOG("* gitlab", gitlab)
    g = os.path.join(local_folder, ".git")
    commit = None
    if not os.path.exists(g):
        fLOG("* initialize", local_folder)
        git_clone(local_folder, gitlab, 
                  user=user, password=password, fLOG=fLOG)
        sub = os.path.split(local_folder)[-1]
        fLOG("* first commit ", gitlab)
        git_commit_all(local_folder, gitlab, 
                       "first commit to " + sub, 
                       user=user, password=password, fLOG=print)
        commit= local_folder, gitlab
                
    return commit