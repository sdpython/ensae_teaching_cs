#-*- coding: utf-8 -*-
"""
@file
@brief Helpers to publish the documentation of python to a website
"""

import os
from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
from pyquickhelper.filehelper.ftp_transfer_files import content_as_binary as pqh_content_as_binary


def trigger_on_specific_strings(content, filename=None, force_allow=None):
    """
    look for specific string such as
    *USERNAME*, *USERDNSDOMAIN*, *HOMEPATH*, *USERNAME*, *COMPUTERNAME*, *LOGONSERVER*,
    and returns None if it was found or modifies the content to remove it

    @param      content     content of a file
    @param      filename    only used when an exception is raised
    @param      force_allow allow these expressions even if they seem to be credentials
    @return                 modified content
    """
    strep = [(r"C:\\%s\\__home_\\_data\\" % os.environ["USERNAME"], "somewhere"),
             ("C:\\%s\\__home_\\_data\\" %
              os.environ["USERNAME"], "somewhere"),
             ("C:\\%s\\__home_\\_data\\" %
              os.environ["USERNAME"], "somewhere"),
             ("C:%s__home__data" % os.environ["USERNAME"], "somewhere"),
             ("%s__home__data" % os.environ["USERNAME"], "somewhere"),
             ]
    for s, b in strep:
        if s in content:
            content = content.replace(s, b)

    if force_allow is None:
        force_allow = set()
    else:
        force_allow = set(force_allow)
    lower_content = content.lower()
    for st in ["USERNAME", "USERDNSDOMAIN", "HOMEPATH", "USERNAME",
               "COMPUTERNAME", "LOGONSERVER"]:
        if st in os.environ:
            s = os.environ[st].lower()
            if s not in force_allow and s in lower_content:
                raise Exception(
                    'string {0}:{1} was found in\n  File "{2}", line 1'.format(st, s, filename))
                return None
    return content


def content_as_binary(filename):
    """
    overloads function `content_as_finary <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/filehelper/ftp_transfer_files.html?highlight=content_as_binary#pyquickhelper.filehelper.ftp_transfer_files.content_as_binary>`_ from
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/">`_

    determines if filename is binary or None before transfering it

    @param      filename        filename
    @return                     boolean
    """
    if pqh_content_as_binary(filename):
        return True
    ff = os.path.split(filename)[-1]
    if ff == "footer.html":
        return True
    return False


def text_transform(ftpp, filename, content):
    """
    if filename is rss.xml, replaces the string *__BLOG_ROOT__* by *self._root_web*

    @param      ftpp        object FolderTransferFTP
    @param      filename    filename
    @param      content     content of the file
    @return                 new content
    """
    if filename.endswith("rss.xml"):
        web = ftpp._root_web
        if not web.startswith("http://"):
            web = "http://" + web.strip("/")
        ftpp.fLOG("[text_transform] replace __BLOG_ROOT__ by ", web)
        return content.replace("__BLOG_ROOT__", web)
    else:
        return content


def publish_documentation(docs, ftpsite=None, login=None, password=None,
                          key_save="my_password", footer_html=None,
                          content_filter=trigger_on_specific_strings,
                          is_binary=content_as_binary, force_allow=None,
                          fLOG=print):
    """
    publish the documentation and the setups of a python module on a webiste,
    it assumes the modules is organized the same way as
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_.

    @param      docs            list of dictionaries (see below)
    @param      ftpsite         something like ``ftp.something.``
    @param      login           login
    @param      password        password
    @param      key_save        see function `open_window_params <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/tkinterquickhelper/funcwin/frame_params.html#tkinterquickhelper.funcwin.frame_params.open_window_params>`_
    @param      footer_html     append this HTML code to any uploaded page (such a javascript code to count the audience)
    @param      content_filter  filter the content of a file (it raises an exception if the result is None),
                                appies only on text files
    @param      is_binary       a function to tell if a content of a file is binary or not
    @param      force_allow     a file is not published if it contains something which looks like credentials
                                except if this string is part of *force_allow*
    @param      fLOG            logging function

    *docs* is a list of dictionaries which must contain for each folder
    to transfer:

    - ``local``: local folder
    - ``root_local``: local paths will be related to this root
    - ``root_web``: prefix to add to the remote paths
    - ``status_file``: a file where the function populates the transfered files and some information about them

    A local file is composed by ``<local_root>/<relative_path>``, it
    will be uploaded to ``<web_root>/<relative_path>``.

    If one of the three first parameters is None, the function
    will open a popup windows to ask the missing information.
    See `open_window_params <http://www.xavierdupre.fr/app/tkinterquickhelper/helpsphinx/tkinterquickhelper/funcwin/frame_params.html#tkinterquickhelper.funcwin.frame_params.open_window_params>`_.
    """

    params = {"ftpsite": ftpsite,
              "login": login,
              "password": password}

    nbnone = len([v for k, v in params.items() if v is None or len(v) == 0])
    if nbnone > 0:
        from tkinterquickhelper.funcwin import open_window_params
        fLOG("retrying to get parameters from users")
        for k, v in sorted(params.items()):
            fLOG("  {0}={1}".format(k, v))
        params = open_window_params(
            params,
            title="Website and Credentials",
            help_string="ftp site + login + password",
            key_save=key_save)

    nbnone = [v for k, v in params.items() if v is None or len(v) == 0]
    if len(nbnone) > 0:
        raise Exception("one of the parameters is None:\n" + str(nbnone))

    password = params["password"]
    login = params["login"]
    ftpsite = params["ftpsite"]

    filter_out = "([/\\\\]((moduletoc.html)|(blogtoc.html)|(searchbox.html)))|([.]buildinfo)"

    ftp = TransferFTP(ftpsite, login, password, fLOG=fLOG)

    for project in docs:

        fLOG("######################################################################")
        for k, v in sorted(project.items()):
            fLOG("  {}={}".format(k, v))

        location = project["local"]
        root_local = project["root_local"]
        root_web = project["root_web"]

        sfile = project["status_file"]
        rootw = project["root_web"]

        # documentation + setup
        fLOG("-------------------------", location)

        ftn = FileTreeNode(root_local)
        fftp = FolderTransferFTP(ftn, ftp, sfile,
                                 root_web=rootw,
                                 fLOG=fLOG,
                                 footer_html=footer_html,
                                 content_filter=content_filter,
                                 is_binary=is_binary,
                                 text_transform=text_transform,
                                 filter_out=filter_out,
                                 force_allow=force_allow)

        fftp.start_transfering()

        ftn = FileTreeNode(os.path.join(root_local, ".."),
                           filter=lambda root, path, f, dir: not dir)
        fftp = FolderTransferFTP(ftn, ftp, sfile,
                                 root_web=root_web.replace(
                                     "helpsphinx", ""),
                                 fLOG=fLOG,
                                 footer_html=footer_html,
                                 content_filter=content_filter,
                                 is_binary=is_binary,
                                 text_transform=text_transform)

        fftp.start_transfering()

    ftp.close()


def publish_teachings_to_web(login, ftpsite="ftp.xavierdupre.fr", google_id=None,
                             location="d:\\jenkins\\pymy\\%s\\%s%s\\dist\\%s",
                             rootw="/www/htdocs/app/%s/%s",
                             rootw2="/lesenfantscodaient.fr", folder_status=".",
                             layout=[("html", "helpsphinx")],
                             modules=["pyquickhelper",
                                      "cpyquickhelper",
                                      "jyquickhelper",
                                      "tkinterquickhelper",
                                      "pyensae",
                                      "pymyinstall",
                                      "pysqllike",
                                      "pyrsslocal",
                                      "pymmails",
                                      "python3_module_template",
                                      "actuariat_python",
                                      "code_beatrix",
                                      "ensae_projects",
                                      "jupytalk",
                                      "mlstatpy",
                                      "teachpyx",
                                      "ensae_teaching_cs"
                                      ],
                             password=None,
                             force_allow=None,
                             suffix=("_UT_36_std",),
                             fLOG=print,
                             exc=True):
    """
    copy the documentation to the website

    @param      login           login
    @param      ftpsite         ftp site
    @param      google_id       google_id
    @param      location        location of Jenkins build
    @param      rootw           root on ftp site
    @param      rootw2          root for ``lesenfantscodaient.fr``
    @param      folder_status   folder status
    @param      modules         list of modules to publish
    @param      password        if None, if will asked
    @param      layout          last part of the folders
    @param      suffix          suffixes to append to the project name
    @param      force_allow     allow to publish files even if they contain these strings
                                whereas they seem to be credentials
    @param      exc             raise exception if not found (True) or skip (False)
    @param      fLOG            logging function

    Example of use::

        import sys
        import os
        from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
        from tkinterquickhelper.funcwin import open_window_params
        from ensae_teaching_cs.automation.ftp_publish_helper import publish_teachings_to_web

        login = "..."
        website = "ftp...."
        rootw = "/www/htdocs/app/%s/%s"
        rootw2 = "/lesenfantscodaient.fr"

        password = None

        publish_teachings_to_web(login, ftpsite=website,
            google_id="google_id",
            location="<something>\\\\%s\\\\%s%s\\\\dist\\\\%s",
            rootw=rootw,
            rootw2=rootw2,
            folder_status=os.path.abspath("."),
            password=password)

    """
    import os
    from tkinterquickhelper.funcwin import open_window_params
    from ensae_teaching_cs.automation.ftp_publish_helper import publish_documentation

    if google_id is None:
        google_id = ""
    else:
        footer = """
        <script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
        <script type="text/javascript">
        _uacct = "{}";
        urchinTracker();
        </script>
        """.format(google_id)

    if password is None:
        params = {"password": ""}
        params = open_window_params(
            params, title="password", help_string="password", key_save="my_password")
        password = params["password"]

    location = os.path.abspath(location)
    if folder_status is None:
        folder_status = os.path.abspath(os.path.dirname(__file__))
    else:
        folder_status = os.path.abspath(folder_status)

    if not isinstance(suffix, (tuple, list)):
        suffix = [suffix]

    projects = []
    for module in modules:

        fLOG("  +", module, " -- ", layout)

        for lay in layout:
            for suf in suffix:
                root = os.path.abspath(location %
                                       (module, module, suf, lay[0]))
                keepsuf = suf
                if os.path.exists(root):
                    break
            if not os.path.exists(root):
                if exc:
                    raise FileNotFoundError("first tried '{0}'\n last tried '{1}'".format(root,
                                                                                          os.path.abspath(location % (module, module, suffix[0], lay[0]))))
                else:
                    fLOG("[publish_teachings_to_web] skip", root)
                    continue
                fLOG("   ", root)
            if module != "code_beatrix":
                rw = rootw % (module, lay[1])
            else:
                rw = rootw2

            project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                           local=root, root_local=root, root_web=rw)
            projects.append(project)

        if module == "ensae_teaching_cs":
            lay = [_ for _ in layout if _[0] == "html"][0]
            if not os.path.exists(root):
                if exc:
                    raise FileNotFoundError(root)
                else:
                    fLOG("[publish_teachings_to_web] skip", root)
                    continue

            project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                           local=root.replace("\\html", "\\html2"),
                           root_local=root.replace("\\html", "\\html2"),
                           root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx2"))
            projects.append(project)

            project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                           local=root.replace("\\html", "\\html3"),
                           root_local=root.replace("\\html", "\\html3"),
                           root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx3"))
            projects.append(project)

            # pres

            for sufpress in ["", "_2A", "_3A", "_1Ap"]:
                root = os.path.abspath(location % (
                    module, module, keepsuf, "html"))
                if not os.path.exists(root):
                    if exc:
                        raise FileNotFoundError(root)
                    else:
                        fLOG("[publish_teachings_to_web] skip", root)
                        continue
                project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                               local=root.replace(
                                   "\\html", "\\html_pres" + sufpress),
                               root_local=root.replace(
                                   "\\html", "\\html_pres" + sufpress),
                               root_web=(rootw % (module, lay[1])).replace("/helpsphinx", "/pressphinx" + sufpress).replace("_no_clean", ""))
                projects.append(project)

        elif module == "python3_module_template":
            lay = [_ for _ in layout if _[0] == "html"][0]
            if not os.path.exists(root):
                if exc:
                    raise FileNotFoundError(root)
                else:
                    fLOG("[publish_teachings_to_web] skip", root)
                    continue

            project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                           local=root.replace("\\html", "\\html2"),
                           root_local=root.replace("\\html", "\\html2"),
                           root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx2"))
            projects.append(project)

    # publish

    publish_documentation(projects, ftpsite=ftpsite, login=login, password=password,
                          key_save="my_module_password", footer_html=footer,
                          force_allow=force_allow, fLOG=fLOG)
