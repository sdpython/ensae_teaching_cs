"""
@file
@brief Some automation helpers to grab mails from students about projects.
"""

import os
from pyquickhelper.loghelper import noLOG, run_cmd
from pyquickhelper.texthelper import remove_diacritics


def git_clone(local_folder, url_https, user=None, password=None, timeout=60,
              init=True, fLOG=noLOG):
    """
    Clones a project from a git repository in a non empty local folder,
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

    .. exref::
        :tag: Automation
        :title: Clone many folders in one row

        ::

            eleves = "project1;project2;..."
            root = r"destination"

            for el in eleves.split(";"):
                cl = el.lower().replace(".","-")
                fold = os.path.join(root, el)
                if not os.path.exists(fold):
                    print("clone", el)
                    url = "https://<gitlab>/<group>/{0}.git".format(cl)
                    git_clone(  fold, url,user=user,password=password, init=False,fLOG=print)

    """
    url_user = git_url_user_password(url_https, user, password)
    timeout = 60
    local_folder = os.path.normpath(os.path.abspath(local_folder))

    if init:
        if not os.path.exists(local_folder):
            fLOG("creating folder", local_folder)
            os.mkdir(local_folder)

        hg = os.path.join(local_folder, ".git")
        if os.path.exists(hg):
            raise Exception("folder {0} should not exist".format(local_folder))

        if not os.path.exists(hg):
            cmds = """
                    cd {0}
                    git init
                    git remote add origin {1}
                    git fetch
                    """.format(local_folder, url_user).replace("                    ", "").strip(" \n\r\t")
            cmd = cmds.replace("\n", "&")
            sin = ""  # "{0}\n".format(password)
            out, err = run_cmd(
                cmd, sin=sin, wait=True, timeout=timeout, fLOG=fLOG)
            git_check_error(out, err, fLOG)

        return local_folder
    else:
        if not os.path.exists(local_folder):
            fLOG("creating folder", local_folder)
            os.mkdir(local_folder)

        hg = os.path.join(local_folder, ".git")
        if os.path.exists(hg):
            raise Exception("folder {0} should not exist".format(local_folder))

        final = os.path.split(url_user)[-1].replace(".git", "")
        locf = os.path.join(local_folder, final)
        if os.path.exists(locf):
            raise Exception(
                "folder {0} should not exists before cloning".format(locf))

        cmds = """
                cd {0}
                git clone {1} .
                """.format(local_folder, url_user).replace("                ", "").strip(" \n\r\t")
        cmd = cmds.replace("\n", "&")
        sin = ""  # "{0}\n".format(password)
        out, err = run_cmd(cmd, sin=sin, wait=True, timeout=timeout, fLOG=fLOG)
        git_check_error(out, err, fLOG)

        return locf


def git_change_remote_origin(local_folder, url_https, user=None, password=None,
                             add_fetch=False, timeout=10, fLOG=noLOG):
    """
    Changes the origin of the repository. The url and the password
    refer to the new repository.

    @param      local_folder   local folder
    @param      url_https       url, example ``https://gitlab.server/folder/project_name``
    @param      user            part 1 of the credentials
    @param      password        part 2 of the credentials
    @param      timeout         timeout for the command line
    @param      add_fetch       add instruction ``fetch``
    @param      fLOG            logging function
    @return                     something

    The function runs the instruction::

        git remote remove origin
        git remote add origin url

    """
    url_user = git_url_user_password(url_https, user, password)
    cmds = """
            cd {0}
            git remote remove origin
            git remote add origin {1}
            """.format(local_folder, url_user).replace("            ", "").strip(" \n\r\t")
    if add_fetch:
        cmds += "\ngit fetch"
    cmd = cmds.replace("\n", "&")
    sin = ""  # "{0}\n".format(password)
    out, err = run_cmd(cmd, sin=sin, wait=True, timeout=timeout, fLOG=fLOG)
    git_check_error(out, err, fLOG)


def git_commit_all(local_folder, url_https, message, user=None,
                   password=None, timeout=300, fLOG=noLOG):
    """
    From a git repository,
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
    cmds = """
            cd {0}
            git add -A
            git commit -m "{1}"
            git push -u origin master
            """.format(local_folder, message).replace("            ", "").strip(" \n\r\t")
    cmd = cmds.replace("\n", "&")
    sin = ""  # "{0}\n".format(password)
    out, err = run_cmd(cmd, sin=sin, wait=True, timeout=timeout, fLOG=fLOG)
    git_check_error(out, err, fLOG)


def git_first_commit_all_projects(local_folder, user=None, password=None,
                                  timeout=300, suivi="suivi.rst", fLOG=noLOG):
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
    filename = os.path.join(local_folder, suivi)
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    with open(filename, "r", encoding="utf8") as f:
        content = f.read()

    global _gitlab_regex
    gitlab = _gitlab_regex.findall(content)
    if len(gitlab) == 0:
        raise Exception(
            "unable to find the regular expression {0} in {1}".format(
                _gitlab_regex.pattern,
                filename))
    if not isinstance(gitlab, list):
        raise TypeError("we expect a list for: " + str(gitlab))
    if len(gitlab) != 1:
        raise Exception(
            "more than one gitlab repo is mentioned {0} in {1}".format(
                _gitlab_regex.pattern,
                filename))
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
        commit = local_folder, gitlab

    return commit


def create_folders_from_dataframe(df, root, report="suivi.rst", col_student="Eleves",
                                  col_group="Groupe", col_subject="Sujet",
                                  overwrite=False, email_function=None):
    """
    Creates a series of folders for groups of students.

    @param      root            where to create the folders
    @param      col_student     column which contains the student name (firt name + last name)
    @param      col_group       index of the grou
    @param      col_subject     column which contains the subject
    @param      df              DataFrame
    @param      email_function  function which infers email from first and last names, see below
    @param      report          report file
    @param      overwrite       if False, skip if the report already exists
    @return                 list of creates folders

    The function *email_function* has the following signature::

        def email_function(first_name, last_name):
            # ....
    """

    def split_name(name):
        name = remove_diacritics(name).split(" ")
        first = name[-1]
        last = " ".join(name[:-1])
        return first, last

    def ul(last):
        res = ""
        for i, c in enumerate(last):
            if c == " ":
                res += "_"
            elif i == 0 or last[i - 1] in [" ", "-", "_"]:
                res += c.upper()
            else:
                res += c.lower()
        return res

    folds = []

    gr = df.groupby(col_group)
    for name, group in gr:
        s = list(set(group[col_subject].copy()))
        if len(s) > 1:
            raise Exception(
                "more than one subject for group: " +
                str(name) +
                "\n" +
                str(s))
        # subject = s[0]
        eleves = list(group[col_student])
        names = [(_,) + split_name(_) for _ in eleves]
        eleves.sort()

        title = ", ".join(eleves)
        content = [title]
        content.append("=" * len(title))
        content.append("")

        content.append("* subject: " + title)
        content.append("* G: %d" % int(name))

        if email_function is not None:
            mails = [email_function(a[1], a[2]) for a in names]
            jmail = "; ".join(mails)
            content.append("* mails: " + jmail)

        content.append("")
        content.append("")

        last = ".".join(ul(a[-1]) for a in sorted(names))

        folder = os.path.join(root, last)
        filename = os.path.join(folder, report)

        if not os.path.exists(folder):
            os.mkdir(folder)

        if overwrite or not os.path.exists(filename):
            with open(filename, "w", encoding="utf8") as f:
                f.write("\n".join(content))

            folds.append(folder)
    return folds


def get_sections(path, suivi="suivi.rst"):
    """
    Extracts sections from a filename used to follow a group of students.

    @param      path        where to find filename
    @param      suivi       file, RST format, section are followed by ``+++++``
    @return                 dictionary { section : content }

    Example of a file::

        rapport
        +++++++

        * bla 1

        extrait
        +++++++

        ::

            paragraphe 1

            paragraphe 2

    """
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    filename = os.path.join(path, suivi)
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    try:
        with open(filename, "r", encoding="utf8") as f:
            content = f.read()
    except UnicodeDecodeError as e:
        raise ValueError(
            'unable to parse file:\n  File "{0}", line 1'.format(filename)) from e

    lines = [_.strip("\r").rstrip() for _ in content.split("\n")]
    added_in = []
    sections = {"": []}
    title = ""
    for i, line in enumerate(lines):
        if len(line) == 0:
            sections[title].append(line)
            added_in.append(title)
        else:
            f = line[0]
            if f == " ":
                if title is not None:
                    sections[title].append(line)
                    added_in.append(title)
                else:
                    sections[""].append(line)
                    added_in.append("")
            elif f in "=+-":
                if line == f * len(line):
                    title = lines[i - 1]
                    if len(added_in) > 0:
                        t = added_in[-1]
                        sections[t] = sections[t][:-1]
                        added_in[-1] = title
                    if f == "=":
                        sections["title"] = [title]
                        added_in.append("title")
                        title = "title"
                    else:
                        sections[title] = []
                        added_in.append(title)
                else:
                    sections[title].append(line)
                    added_in.append(title)
            else:
                sections[title].append(line)
                added_in.append(title)

    return sections


def git_url_user_password(url_https, user, password):
    """
    Builds a url (starting with https) and add the user and the password
    to skip the authentification.

    :param      url_https:       example ``https://gitlab.server/folder/project_name``
    :param      user:            part 1 of the credentials
    :param      password:        part 2 of the credentials
    :return:                     url
    """
    url_user = url_https.replace(
        "https://", "https://{0}:{1}@".format(user, password))
    return url_user


def git_check_error(out, err, fLOG):
    """
    Private function, analyse the output.
    """
    if len(out) > 0:
        fLOG("OUT:\n" + out)
    if len(err) > 0:
        if "error" in err.lower():
            raise Exception("OUT:\n{0}\nERR:\n{1}".format(out, err))
        raise Exception(err)
