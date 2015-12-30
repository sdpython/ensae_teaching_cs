"""
@file
@brief Some automation helpers to grab mails from student about project.
"""
import re
import os
from .repository_exception import RegexRepositoryException, TooManyProjectsException
from pyquickhelper import noLOG, run_cmd, remove_diacritics


class ProjectsRepository:
    """
    handle a repository of students projects
    """

    _email_regex = re.compile("[*] *e?mails? *: *([^*+\\n]+)")
    _gitlab_regex = re.compile("[*] *gitlab *: *([^*+\\n]+[.]git)")
    _video_regex = re.compile("[*] *videos? *: *([^*\\n]+)")

    def __init__(self, location, suivi="suivi.rst"):
        """
        location of the repository

        @param      location        location of the repository
        @param      suivi           name of the file gathering information about each project
        """
        self._location = location
        self._suivi = suivi

    @property
    def Location(self):
        """
        @return     location of the repository
        """
        return self._location

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

        return allmails

    def get_emails(self):
        """
        retrieve student emails from file ``suivi.rst``

        @return                     list of mails
        """
        allmails = ProjectsRepository.get_regex(
            self._location, ProjectsRepository._email_regex, self._suivi)
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

    def get_videos(self):
        """
        retrieve student emails from file ``suivi.rst``
        @return                     list of videos
        """
        return get_regex(self._location, ProjectsRepository._video_regex, self._suivi)

    def get_sections(self):
        """
        extract sections from a filename used to follow a group of students

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
        path = self._location
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

    @staticmethod
    def create_folders_from_dataframe(df,
                                      root,
                                      report="suivi.rst",
                                      col_student="Eleves",
                                      col_group="Groupe",
                                      col_subject="Sujet",
                                      overwrite=False,
                                      email_function=None):
        """
        creates a series of folders for groups of students

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
                raise TooManyProjectsException(
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

        return ProjectsRepository(root, suivi=report)
