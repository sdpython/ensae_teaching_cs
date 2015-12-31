"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re
import os
from pyquickhelper import noLOG, run_cmd, remove_diacritics
from pyquickhelper.filehelper import remove_folder, explore_folder_iterfile
from pyquickhelper.filehelper import zip_files
from pymmails import EmailMessageRenderer
from .repository_exception import RegexRepositoryException, TooManyProjectsException
from ..td_1a import edit_distance


class ProjectsRepository:
    """
    handle a repository of students projects

    @example(AutoTeachings___Collect students work)

    The following example dumps mails from students
    and their attachments as well in a folder.

    ::

        from pyquickhelper import fLOG
        fLOG(OutputPrint=True)

        from ensae_teaching_cs.automation_students import ProjectsRepository, grab_addresses
        from pymmails import MailBoxImap, EmailMessageRenderer, EmailMessageListRenderer
        from pymmails.render.email_message_style import template_email_html_short
        import pandas

        # gather mails

        fLOG("fetch mails")
        filename = "emails.txt"

        user = "xavier.dupre"
        pwd = "***"
        server = "imap.gmail.com"
        mailfolder = ["ensae/ENSAE_2016", "ensae/ensae_interro_2015"]
        date = "1-Dec-2015"

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf8") as f:
                lines = f.readlines()
            emails = [l.strip("\r\t\n ") for l in lines]
        else:
            box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
            box.login()
            emails = grab_addresses(box, mailfolder, date, fLOG=fLOG)
            box.logout()

            with open(filename, "w", encoding="utf8") as f:
                f.write("\n".join(emails))

        fLOG(emails)

        # gathers groups for students

        def replace_parts(s):
            # in case there is something to do
            return s.replace("to replace", "")

        folder = os.path.abspath(".")
        df = pandas.read_excel("notes_eleves_2015_2016.xlsx", skiprows=5)
        df = df[(df["Groupe"] != "moyenne") & (~df["Eleves"].isnull())].copy()
        df["Eleves"] = df["Eleves"].apply(lambda f: replace_parts(f))

        proj = ProjectsRepository(folder, fLOG=fLOG)
        groups = proj.Groups
        if len(groups) < 10:
            fLOG("creation")
            proj = ProjectsRepository.create_folders_from_dataframe(df, folder,
                        col_subject=None, fLOG=fLOG, col_group=None,
                        email_function=emails, skip_if_nomail=True,
                        must_have_email=False)

        # gathers mails

        if True:
            email_render = EmailMessageRenderer(tmpl=template_email_html_short, fLOG=fLOG)
            render = EmailMessageListRenderer(title="list of mails",
                            email_renderer=email_render, fLOG=fLOG)

            box = MailBoxImap(user, pwd, server, ssl=True, fLOG=fLOG)
            box.login()
            mails = proj.dump_group_mails(render, group=None,
                            mailbox=box, subfolder=mailfolder, date=date)

            box.logout()

        # cleaning files

        if True:
            for group in proj.Groups:
                files = list(proj.enumerate_group_files(group))
                att = [_ for _ in files if ".html" in _]
                if len(att) <= 1:
                    fLOG("remove ", group)
                    proj.remove_group(group)

        # summary

        if True:
            proj.write_summary()

        # zip everything
        filename = "td_note_2015.zip"

        if True:
            if os.path.exists(filename):
                os.remove(filename)
            proj.zip_group(None, filename)
            
        # encryption
        enc = filename + ".enc"

        if True:
            fLOG("encryption")
            encrypt_stream(b"password" * 2, filename, enc, chunksize=2**30)            

    @endexample
    """

    class MailNotFound(Exception):
        """
        raises an exception if mail not found
        """
        pass

    _email_regex = re.compile("[*] *e?mails? *: *([^*+\\n]+)")
    _gitlab_regex = re.compile("[*] *gitlab *: *([^*+\\n]+[.]git)")
    _video_regex = re.compile("[*] *videos? *: *([^*\\n]+)")

    def __init__(self, location, suivi="suivi.rst", fLOG=noLOG):
        """
        location of the repository

        @param      location        location of the repository
        @param      suivi           name of the file gathering information about each project
        """
        self._location = location
        self._suivi = suivi
        self.fLOG = fLOG

    @property
    def Location(self):
        """
        @return     location of the repository
        """
        return self._location

    @property
    def Groups(self):
        """
        returns all available groups in the repository
        """
        return [_ for _ in os.listdir(self._location)
                if os.path.isdir(os.path.join(self._location, _))]

    def get_group_location(self, group):
        """
        return the local folder associated to a group

        @param      group       group name
        @return                 local folder
        """
        return os.path.join(self._location, group)

    @staticmethod
    def get_regex(path, regex, suivi="suivi.rst"):
        """
        retrieve data from file ``suivi.rst`` using a regular expression

        @param      path            sub folder to look into
        @param      suivi           name of the file ``suivi.rst``
        @return                     list of mails
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

        mails = regex.findall(content)
        if len(mails) == 0:
            raise Exception(
                "unable to find the regular expression {0} in {1}".format(
                    regex.pattern,
                    filename))

        allmails = []
        for m in mails:
            allmails.extend(m.strip("\n\r\t ").split(";"))

        return [_.strip() for _ in allmails for _ in allmails]

    def get_emails(self, group):
        """
        retrieve student emails from file ``suivi.rst``

        @param      group           group
        @return                     list of mails
        """
        path = os.path.join(self._location, group)
        allmails = ProjectsRepository.get_regex(
            path, ProjectsRepository._email_regex, self._suivi)
        for a in allmails:
            if "\n" in a:
                raise ValueError(
                    "unable to interpret " + str([a]) + " from path " + path)
            ff = a.split("@")
            if len(ff) != 2:
                raise RegexRepositoryException(
                    "unable to understand mail {0} in {1} (suivi={2} (mail separator is ;)".format(
                        a,
                        path,
                        self._suivi))
        return allmails

    def get_videos(self, group):
        """
        retrieve student emails from file ``suivi.rst``

        @param      group           group
        @return                     list of videos
        """
        return get_regex(group, ProjectsRepository._video_regex, self._suivi)

    def get_sections(self, group):
        """
        extract sections from a filename used to follow a group of students

        @param      group           group
        @return                     dictionary { section : content }

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
        path = os.path.join(self._location, group)
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        filename = os.path.join(path, self._suivi)
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

    _regex_split = re.compile("[-;,. ]")

    @staticmethod
    def match_mail(name, emails, threshold=3, exc=True):
        """
        tries to match a name among a list of mails

        @param      name        a name (first name last name separated by a space)
        @param      emails      list of emails
        @param      threshold   above this threshold, mails and names don't match
        @param      exc         raise an Exception if not found
        @return                 list of available mails, boolean

        The second results is True if no email were found in the list.
        """
        pieces = [_.strip() for _ in ProjectsRepository._regex_split.split(
            remove_diacritics(name.lower()))]
        pieces.sort()
        pieces = " ".join(pieces)
        res = []
        for email in emails:
            spl = [_.strip() for _ in ProjectsRepository._regex_split.split(
                remove_diacritics(email.split("@")[0].lower()))]
            spl.sort()
            mail = " ".join(spl)
            d, p = edit_distance(mail, pieces)
            res.append((d, email))
        if "foy" in name.lower():
            res.sort()
            print(name, res)
        res = [_ for _ in res if _[0] <= threshold]
        res.sort()
        if exc and len(res) == 0:
            raise ProjectsRepository.MailNotFound(
                "unable to find a mail for {0} among\n{1}".format(name, "\n".join(emails)))
        return res

    @staticmethod
    def match_mails(names, emails, threshold=3, exc=True):
        """
        tries to match a series of names among a list of mails

        @param      names       list of names (first name last name separated by a space)
        @param      emails      list of emails
        @param      threshold   above this threshold, mails and names don't match
        @param      exc         raise an Exception if not found
        @return                 list of available mails, boolean

        The second results is True if no email were found in the list.
        """
        res = []
        skip = False
        for name in names:
            r = ProjectsRepository.match_mail(name, emails, threshold, exc)
            if not r:
                skip = True
            res.extend([_[1] for _ in r])
        return res, skip

    @staticmethod
    def create_folders_from_dataframe(df,
                                      root,
                                      report="suivi.rst",
                                      col_student="Eleves",
                                      col_group="Groupe",
                                      col_subject="Sujet",
                                      overwrite=False,
                                      email_function=None,
                                      must_have_email=True,
                                      skip_if_nomail=False,
                                      fLOG=noLOG):
        """
        creates a series of folders for groups of students

        @param      root                where to create the folders
        @param      col_student         column which contains the student name (firt name + last name)
        @param      col_group           index of the group (it can be None if each student is a group)
        @param      col_subject         column which contains the subject
        @param      df                  DataFrame
        @param      email_function      function which infers email from first and last names, see below
        @param      report              report file
        @param      overwrite           if False, skip if the report already exists
        @param      must_have_email     if True, raises an exception if no mail is found
        @param      skip_if_nomail      skip a name if no mail is found
        @return                         list of creates folders

        The function *email_function* has the following signature::

            def email_function(names):
                # part of a names is a list of tokens
                # ...
                return list of mails, skip=boolean

        The boolean tells the function to skip this group.
        *email_function* can be a list of mails. In that case,
        this function is replaced by @see me match_mails.
        """
        def local_email_function(names):
            return ProjectsRepository.match_mails(names, email_function, exc=False)

        if isinstance(email_function, list):
            local_function = local_email_function
        else:
            local_function = email_function

        def split_name(name):
            name = remove_diacritics(name).split(" ")
            first = name[-1]
            last = " ".join(name[:-1])
            return first, last

        def ul(last):
            res = ""
            for i, c in enumerate(last):
                if c == " ":
                    res += "."
                elif c == "-":
                    res += "."
                else:
                    res += c
            return res

        folds = []

        if col_group:
            gr = df.groupby(col_group)
        else:
            df2 = df.copy()
            df2["gid"] = df.index
            df2["gid2"] = df2.gid.apply(lambda x: "G%d" % x)
            gr = df2.groupby("gid2")

        fLOG("ProjectsRepository.create_folders_from_dataframe [number of groups {0}]".format(
            len(gr)))

        for name, group in gr:
            if col_subject:
                s = list(set(group[col_subject].copy()))
                if len(s) > 1:
                    raise TooManyProjectsException(
                        "more than one subject for group: " +
                        str(name) +
                        "\n" +
                        str(s))

                subject = s[0]
            else:
                subject = None

            eleves = list(group[col_student])
            eleves.sort()

            if email_function is not None:
                mails, skip = local_function(eleves)
                if must_have_email and (skip or len(mails) == 0):
                    if isinstance(email_function, list):
                        raise ProjectsRepository.MailNotFound("unable to find a mail for {0} among\n{1}".format(" ;".join(eleves),
                                                                                                                "\n".join(email_function)))
                    else:
                        raise ProjectsRepository.MailNotFound(
                            "unable to find a mail for {0} with function\n{1}".format(" ;".join(eleves), email_function))
                if skip_if_nomail and (skip or len(mails) == 0):
                    fLOG("ProjectsRepository.create_folders_from_dataframe [skipping {0}]".format(
                        "; ".join(eleves)))
                    continue
                if mails:
                    jmail = "; ".join(mails)
                else:
                    jmails = None
            else:
                jmail = None

            members = ", ".join(eleves)
            content = [members]
            content.append("=" * len(members))
            content.append("")

            content.append("* members: {0}".format(members))
            if subject:
                content.append("* subject: {0}".format(subject))
            content.append("* G: {0}".format(name))

            if jmail:
                content.append("* mails: " + jmail)

            content.append("")
            content.append("")

            last = "-".join(ul(a) for a in sorted(eleves))

            folder = os.path.join(root, last)
            filename = os.path.join(folder, report)

            if not os.path.exists(folder):
                os.mkdir(folder)

            if overwrite or not os.path.exists(filename):
                with open(filename, "w", encoding="utf8") as f:
                    f.write("\n".join(content))

                folds.append(folder)

        return ProjectsRepository(root, suivi=report, fLOG=fLOG)

    def enumerate_group_mails(self, group, mailbox, subfolder, date=None,
                              skip_function=None, max_dest=5):
        """
        enumerates all mails sent by or sent to a given group

        @param      group           group (if None, goes through all mails)
        @param      mailbox         mailbox (see `pymmails <http://www.xavierdupre.fr/app/pymmails/helpsphinx/>`_)
        @param      subfolder       which subfolder of the mailbox to look into
        @param      date            date
        @param      skip_function   if not None, use this function on the header/body to avoid loading the entire message (and skip it)
        @param      max_dest        maximum number of receivers
        @return                     iterator on mails
        """
        if group is None:
            for group in self.Groups:
                self.fLOG(
                    "ProjectsRepository.enumerate_group_mails [group={0}]".format(group))
                iter = self.enumerate_group_mails(group, mailbox, subfolder=subfolder,
                                                  date=date, skip_function=skip_function, max_dest=max_dest)
                for mail in iter:
                    yield mail
        else:
            mails = self.get_emails(group)
            self.fLOG("ProjectsRepository.enumerate_group_mails [mails={0} folder={1} date={2}]".format(
                str(mails), subfolder, date))
            iter = mailbox.enumerate_search_person(
                person=mails,
                folder=subfolder,
                skip_function=skip_function,
                date=date,
                max_dest=5)
            for mail in iter:
                yield mail

    def dump_group_mails(self, renderer, group, mailbox, subfolder, date=None,
                         skip_function=None, max_dest=5, filename="index_mails.html",
                         overwrite=False):
        """
        enumerates all mails sent by or sent to a given group

        @param      renderer        instance of class `EmailMessageListRenderer <http://www.xavierdupre.fr/app/pymmails/helpsphinx/pymmails/render/email_message_list_renderer.html>`_
        @param      group           group
        @param      mailbox         mailbox (see `pymmails <http://www.xavierdupre.fr/app/pymmails/helpsphinx/>`_)
        @param      subfolder       which subfolder of the mailbox to look into
        @param      date            date
        @param      skip_function   if not None, use this function on the header/body to avoid loading the entire message (and skip it)
        @param      max_dest        maximum number of receivers
        @param      filename        filename which gathers a link to every mail
        @param      overwrite       overwrite
        @return                     list of files (see `EmailMessageListRenderer.write <http://www.xavierdupre.fr/app/pymmails/helpsphinx/pymmails/render/email_message_list_renderer.html>`_)
        """
        if group is None:
            res = []
            for group in self.Groups:
                self.fLOG(
                    "ProjectsRepository.dump_group_mails [group={0}]".format(group))
                r = self.dump_group_mails(renderer, group, mailbox, subfolder=subfolder,
                                          date=date, skip_function=skip_function, max_dest=max_dest)
                res.extend(r)
            return res
        else:
            mails = self.get_emails(group)
            self.fLOG("ProjectsRepository.dump_group_mails [mails={0} folder={1} date={2}]".format(
                str(mails), subfolder, date))
            iter = mailbox.enumerate_search_person(person=mails, folder=subfolder,
                                                   skip_function=skip_function, date=date, max_dest=max_dest)
            location = self.get_group_location(group)
            r = renderer.write(iter=iter, location=location,
                               filename=filename, overwrite=overwrite)
            renderer.flush()
            return r

    def remove_group(self, group):
        """
        remove a group

        @param      group       group
        @return                 list of removed files

        see `remove_folder <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx//pyquickhelper/filehelper/synchelper.html#module-pyquickhelper.filehelper.synchelper>`_
        """
        loc = self.get_group_location(group)
        return remove_folder(loc)

    def enumerate_group_files(self, group):
        """
        enumerate all files in a group

        @param      group       group
        @return                 iterator on files
        """
        if group is None:
            for g in self.Groups:
                for _ in self.enumerate_group_files(g):
                    yield _
        else:
            loc = self.get_group_location(group)
            for _ in explore_folder_iterfile(loc):
                yield _

    def zip_group(self, group, outfile):
        """
        zip a group

        @param      group       group
        @param      outfile     output file
        @return                 list of zipped files
        """
        return zip_files(outfile, self.enumerate_group_files(group), root=self._location)
        
    def write_summary(self, render=None, link="index_mails.html", 
                      outfile="index.html", title="summary"):
        """
        produces a summary and uses a Jinja2 template
        
        @param      render      instance of `EmailMessageRenderer <http://www.xavierdupre.fr/app/pymmails/helpsphinx//pymmails/render/email_message_renderer.html>`_),
                                can be None
        @param      link        look for this file in each folder
        @param      outfile     output file
        @return                 summary
        
        the current default template is::
        
            <?xml version="1.0" encoding="utf-8"?>
            <body>
            <html>
            <head>
            <title>{{ title }}</title>
            <link rel="stylesheet" type="text/css" href="{{ css }}">
            </head>
            <body>
            <h1>{{ title }}</h1>
            <ul>
            {% for link, group, nb, size in groups %}
                <li><a href="{{ link }}">{{ group }}</a> {{ nb }} files, {{ size }} bytes</li>
            {% endfor %}
            </ul>
            </body>
            </html> 
        
        """
        groups = []
        for group in self.Groups:
            l = os.path.join(self.get_group_location(group), link)
            if os.path.exists(l):
                c = os.path.relpath(l, self._location), group
            else:
                c = "file:///{0}".format(group), group
            nb_files = 0
            size = 0
            for name in self.enumerate_group_files(group):
                loc = self.get_group_location(group)
                nb_files += 1
                size += os.stat(os.path.join(loc, name)).st_size
            c =  (c[0].replace("\\", "/"), c[1], nb_files, size)
            groups.append(c)
        
        if render is None:
            tmpl = """<?xml version="1.0" encoding="utf-8"?>
                    <body>
                    <html>
                    <head>
                    <title>{{ title }}</title>
                    <link rel="stylesheet" type="text/css" href="{{ css }}">
                    </head>
                    <body>
                    <h1>{{ title }}</h1>
                    <ul>
                    {% for link, group, nb, size in groups %}
                        <li><a href="{{ link }}">{{ group }}</a> {{ nb }} files, {{ size }} bytes</li>
                    {% endfor %}
                    </ul>
                    </body>
                    </html> 
                    """.replace("                    ", "")
            render = EmailMessageRenderer(tmpl=tmpl)
            return render.write(filename=outfile, location=".", 
                        mail=None, attachments=None, groups=groups,
                        title=title)
            