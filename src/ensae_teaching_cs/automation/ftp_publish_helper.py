#-*- coding: utf-8 -*-
"""
@file
@brief Helpers to publish the documentation of python to a website
"""

import os
import warnings
from pyquickhelper import TransferFTP, FileTreeNode, FolderTransferFTP, open_window_params
from pyquickhelper.filehelper.ftp_transfer_files import content_as_binary as pqh_content_as_binary


def trigger_on_specific_strings(content):
    """
    look for specific string such as
    *USERNAME*, *USERDNSDOMAIN*, *HOMEPATH*, *USERNAME*, *COMPUTERNAME*, *LOGONSERVER*,
    and returns None if it was found or modifies the content to remove it
    """
    strep = [(r"C:\\%s\\__home_\\_data\\" % os.environ["USERNAME"], "somewhere"),
             ("C:\\%s\\__home_\\_data\\" %
              os.environ["USERNAME"], "somewhere"),
             ]
    for s, b in strep:
        if s in content:
            content = content.replace(s, b)

    lower_content = content.lower()
    for st in ["USERNAME", "USERDNSDOMAIN", "HOMEPATH", "USERNAME",
               "COMPUTERNAME", "LOGONSERVER"]:
        if st in os.environ:
            s = os.environ[st].lower()
            if s in lower_content:
                raise Exception("string {0}:{1} was found".format(st, s))
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


def publish_documentation(
        docs,
        ftpsite=None,
        login=None,
        password=None,
        key_save="my_password",
        footer_html=None,
        content_filter=trigger_on_specific_strings,
        is_binary=content_as_binary,
        fLOG=print):
    """
    publish the documentation and the setups of a python module on a webiste,
    it assumes the modules is organized the same way as
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/index.html>`_.

    @param      docs            list of dictionaries (see below)
    @param      ftpsite         something like ``ftp.something.``
    @param      login           login
    @param      password        password
    @param      key_save        see function `open_window_params <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/funcwin/frame_params.html#pyquickhelper.funcwin.frame_params.open_window_params>`_
    @param      footer_html     append this HTML code to any uploaded page (such a javascript code to count the audience)
    @param      content_filter  filter the content of a file (it raises an exception if the result is None),
                                appies only on text files
    @param      is_binary       a function to tell if a content of a file is binary or not
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
    See `open_window_params <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/funcwin/frame_params.html#pyquickhelper.funcwin.frame_params.open_window_params>`_.

    Here is an example of a program which pusblishes several documentations on the
    same website::

        from pyquickhelper import TransferFTP, FileTreeNode, FolderTransferFTP, open_window_params
        from ensae_teaching_cs.automation.ftp_publish_helper import publish_documentation

        footer = '''
        <script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
        <script type="text/javascript">
        _uacct = "something";
        urchinTracker();
        </script>
        '''


        login = "login"
        params = { "password":"" }
        params = open_window_params (params, title="password", help_string = "password", key_save="my_password")
        password = params["password"]

        location = os.path.abspath(r"..\GitHub\%s\dist\html")
        this = os.path.abspath(os.path.dirname(__file__))
        rootw = "/www/htdocs/app/%s/helpsphinx"

        projects = [ ]
        for module in [
                "pyquickhelper",
                "anaconda2_pyquickhelper_27",
                "pyensae",
                "pymyinstall",
                "anaconda2_pymyinstall_27",
                "pysqllike",
                "pyrsslocal",
                "pymmails",
                "python3_module_template",
                "anaconda2_python3_module_template_27",
                "actuariat_python",
                #"code_beatrix",
                "ensae_teaching_cs",
                ] :

            root = os.path.abspath(location % module)
            project = dict ( status_file = os.path.join(this, "status_%s.txt" % module),
                             local = root,
                             root_local = root,
                             root_web = rootw % module.replace("_no_clean","") \\
                                                      .replace("anaconda2_", "") \\
                                                      .replace("_27", ""))
            projects.append (project)

        # doc

        project = dict ( status_file = os.path.join(this, "status_%s.txt" % module),
                         local = root.replace("\\html","\\html2"),
                         root_local = root.replace("\\html","\\html2"),
                         root_web = (rootw % module).replace("_no_clean","").replace("/helpsphinx","/helpsphinx2"))
        projects.append (project)

        root = os.path.abspath(location % module)
        project = dict ( status_file = os.path.join(this, "status_%s.txt" % module),
                         local = root.replace("\\html","\\html3"),
                         root_local = root.replace("\\html","\\html3"),
                         root_web = (rootw % module).replace("_no_clean","").replace("/helpsphinx","/helpsphinx3"))
        projects.append (project)

        # pres
        for suffix in ["", "_2A", "_3A", "_1Ap"]:
            root = os.path.abspath(location % module)
            project = dict ( status_file = os.path.join(this, "status_%s.txt" % module),
                             local = root.replace("\\html","\\html_pres" + suffix),
                             root_local = root.replace("\\html","\\html_pres" + suffix),
                             root_web = (rootw % module).replace("/helpsphinx","/pressphinx" + suffix).replace("_no_clean",""))
            print(project)
            projects.append (project)

        # publication
        publish_documentation   (projects,
                        ftpsite         = "ftp.something.cc",
                        login           = login,
                        password        = password,
                        key_save        = "my_module_password",
                        footer_html     = footer)

    """

    params = {"ftpsite": ftpsite,
              "login": login,
              "password": password,
              }

    nbnone = len([v for k, v in params.items() if v is None or len(v) == 0])
    if nbnone > 0:
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

    filter_out = "[/\\\\]((moduletoc.html)|(blogtoc.html))"

    ftp = TransferFTP(ftpsite,
                      login,
                      password,
                      fLOG=fLOG)

    for project in docs:

        location = project["local"]
        root_local = project["root_local"]
        root_web = project["root_web"]

        m27 = os.path.join(root_local, "..", "..", "dist_module27")
        sfile = project["status_file"]
        rootw = project["root_web"]

        if os.path.exists(m27):
            # python 27.version
            fLOG("-------------------------py27", m27)
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
        else:
            # python 3.4 documentation + setup
            fLOG("-------------------------py34", location)

            ftn = FileTreeNode(root_local)
            fftp = FolderTransferFTP(ftn, ftp, sfile,
                                     root_web=rootw,
                                     fLOG=fLOG,
                                     footer_html=footer_html,
                                     content_filter=content_filter,
                                     is_binary=is_binary,
                                     text_transform=text_transform,
                                     filter_out=filter_out)

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


def publish_teachings_to_web(
        login,
        ftpsite="ftp.xavierdupre.fr",
        google_id=None,
        location="C:\\jenkins\\pymy\\%s\\dist\\html",
        rootw="/www/htdocs/app/%s/helpsphinx",
        rootw2="/lesenfantscodaient.fr",
        folder_status=".",
        modules=["anaconda2_pyquickhelper_27",
                 "pyquickhelper",
                 "pyensae",
                 "anaconda2_pymyinstall_27",
                 "pymyinstall",
                 "pysqllike",
                 "pyrsslocal",
                 "pymmails",
                 "anaconda2_python3_module_template_27",
                 "python3_module_template",
                 "actuariat_python",
                 "code_beatrix",
                 "ensae_teaching_cs"],
        password=None):
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
    """
    import os
    import shutil
    from pyquickhelper import open_window_params
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

    projects = []
    for module in modules:

        if module.endswith("27"):
            # C:\jenkins\pymy\anaconda2_pyquickhelper_27\dist_module27\dist
            root = os.path.abspath(location % (module + "\\dist_module27"))
            root = os.path.join(root, "..")

            if not os.path.exists(root):
                warnings.warn(
                    "unable to publish: {0},\n{1} not found".format(module, root))
                continue

            for f in os.listdir(root):
                ext = os.path.splitext(f)[-1]
                if ext in [".whl"]:
                    dest = module.replace("anaconda2_", "").replace("_27", "")
                    dest = location % dest
                    dest = os.path.join(dest, "..")
                    shutil.copy(os.path.join(root, f), dest)
        else:
            root = os.path.abspath(location % module)
            if module != "code_beatrix":
                smod = module.replace("_no_clean", "").replace(
                    "anaconda2_", "").replace("_27", "")
                rw = rootw % smod
            else:
                rw = rootw2
            project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                           local=root,
                           root_local=root,
                           root_web=rw)
            projects.append(project)

    # doc

    project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                   local=root.replace("\\html", "\\html2"),
                   root_local=root.replace("\\html", "\\html2"),
                   root_web=(rootw % module).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx2"))
    projects.append(project)

    root = os.path.abspath(location % module)
    project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                   local=root.replace("\\html", "\\html3"),
                   root_local=root.replace("\\html", "\\html3"),
                   root_web=(rootw % module).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx3"))
    projects.append(project)

    # pres

    for suffix in ["", "_2A", "_3A", "_1Ap"]:
        root = os.path.abspath(location % module)
        project = dict(status_file=os.path.join(folder_status, "status_%s.txt" % module),
                       local=root.replace("\\html", "\\html_pres" + suffix),
                       root_local=root.replace(
                           "\\html", "\\html_pres" + suffix),
                       root_web=(rootw % module).replace("/helpsphinx", "/pressphinx" + suffix).replace("_no_clean", ""))
        print(project)
        projects.append(project)

    # publish

    publish_documentation(projects,
                          ftpsite=ftpsite,
                          login=login,
                          password=password,
                          key_save="my_module_password",
                          footer_html=footer)
