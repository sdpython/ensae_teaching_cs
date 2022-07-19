# -*- coding: utf-8 -*-
"""
@file
@brief Helpers to publish the documentation of :epkg:`python` to a website.
"""
import sys
import os
from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
from pyquickhelper.filehelper.ftp_transfer_files import content_as_binary as pqh_content_as_binary
from .teaching_modules import get_teaching_modules


def trigger_on_specific_strings(content, filename=None, force_allow=None):
    """
    Looks for specific string such as
    *USERNAME*, *USERDNSDOMAIN*, *HOMEPATH*, *USERNAME*, *COMPUTERNAME*,
    *LOGONSERVER*, *USER*, *HOME*, *LOGNAME*
    and returns None if it was found or modifies the content to remove it.

    @param      content     content of a file
    @param      filename    only used when an exception is raised
    @param      force_allow allow these expressions even if they seem to be credentials
    @return                 modified content
    """
    strep = [('/var/lib/jenkins/workspace/_automation/_automation_FORK_', 'somewhere'),
             ('/var/lib/jenkins', 'somewhere')]
    for env in ['USERNAME', 'USER']:
        if env in os.environ and os.environ[env] != "jenkins":
            for sub in ["_data", "GitHub"]:
                strep.extend([(r"C:\\%s\\__home_\\%s\\" % (os.environ[env], sub), "somewhere"),
                              ("C:\\%s\\__home_\\%s\\" %
                               (os.environ[env], sub), "somewhere"),
                              ("C:\\%s\\__home_\\%s\\" %
                               (os.environ[env], sub), "somewhere"),
                              (f"C:{os.environ[env]}__home_{sub}", "somewhere"),
                              (f"{os.environ[env]}__home_{sub}", "somewhere")
                              ])
    for s, b in strep:
        if s in content:
            content = content.replace(s, b)

    if force_allow is None:
        force_allow = set()
    else:
        force_allow = set(force_allow)
    lower_content = content.lower()
    for st in ["USERNAME", "USERDNSDOMAIN", "HOMEPATH", "USERNAME",
               "COMPUTERNAME", "LOGONSERVER", "USER", 'HOME', 'LOGNAME']:
        if st in os.environ:
            s = os.environ[st].lower()
            if s == 'jenkins':
                continue
            if s in ('administrateur', 'administrator'):
                continue
            if s not in force_allow and s in lower_content:
                raise Exception(
                    f'string {st}:{s} was found in\n  File "{filename}", line 1')
    return content


def content_as_binary(filename):
    """
    Overloads function `content_as_finary
    <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/filehelper/ftp_transfer_files.html?
    highlight=content_as_binary#pyquickhelper.filehelper.ftp_transfer_files.content_as_binary>`_ from
    `pyquickhelper <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/>`_.
    Determines if filename is binary or None before transfering it.

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
    If filename is *rss.xml*,
    replaces the string *__BLOG_ROOT__* by *self._root_web*.

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
                          footer_html=None, content_filter=trigger_on_specific_strings,
                          is_binary=content_as_binary, force_allow=None,
                          delay=0.5, exc=False, ftps='FTP',
                          page_transform=None, fLOG=print):
    """
    Publishes the documentation and the setups of a python module on a webiste,
    it assumes the modules is organized the same way as :epkg:`pyquickhelper`.

    @param      docs            list of dictionaries (see below)
    @param      ftpsite         something like ``ftp.something.``
    @param      login           login
    @param      password        password
    @param      footer_html     append this HTML code to any uploaded page (such a javascript code to count the audience)
    @param      content_filter  filter the content of a file (it raises an exception if the result is None),
                                appies only on text files
    @param      is_binary       a function to tell if a content of a file is binary or not
    @param      force_allow     a file is not published if it contains something which looks like credentials
                                except if this string is part of *force_allow*
    @param      delay           delay between file transferring (in average)
    @param      exc             raise exception if not able to transfer
    @param      ftps            use protocol FTP, TLS, or SFTP
    @param      page_transform  function which transforms
                                the page before uploading it,
                                @see fn text_transform
    @param      fLOG            logging function

    *docs* is a list of dictionaries which must contain for each folder
    to transfer:

    - ``local``: local folder
    - ``root_local``: local paths will be related to this root
    - ``root_web``: prefix to add to the remote paths
    - ``status_file``: a file where the function populates the transfered files and some information about them

    A local file is composed by ``<local_root>/<relative_path>``, it
    will be uploaded to ``<web_root>/<relative_path>``.
    """

    params = {"ftpsite": ftpsite,
              "login": login,
              "password": password}

    nbnone = len([v for k, v in params.items() if v is None or len(v) == 0])
    if nbnone > 0:
        raise ValueError(
            f"One of the following parameters is not specified:\n{params}")

    nbnone = [v for k, v in params.items() if v is None or len(v) == 0]
    if len(nbnone) > 0:
        raise Exception("one of the parameters is None:\n" + str(nbnone))

    password = params["password"]
    login = params["login"]
    ftpsite = params["ftpsite"]

    filter_out = "([/\\\\]((moduletoc.html)|(blogtoc.html)|(searchbox.html)))|([.]buildinfo)|([.]pyc)"

    ftp = TransferFTP(ftpsite, login, password, ftps=ftps, fLOG=fLOG)

    if page_transform is None:
        fct_transform = text_transform
    else:

        def combined_transform(ftpp, filename, content):
            text_transform(ftpp, filename, content)
            page_transform(ftpp, filename, content)

        fct_transform = combined_transform

    for project in docs:

        fLOG("######################################################################")
        for k, v in sorted(project.items()):
            fLOG(f"[publish_documentation] loop {k}='{v}'")

        location = project["local"]
        root_local = project["root_local"]
        root_web = project["root_web"]

        sfile = project["status_file"]
        rootw = project["root_web"]

        # documentation + setup
        fLOG(f"[publish_documentation] location='{location}'")

        ftn = FileTreeNode(root_local)
        fftp = FolderTransferFTP(ftn, ftp, sfile, root_web=rootw, fLOG=fLOG, footer_html=footer_html,
                                 content_filter=content_filter, is_binary=is_binary,
                                 text_transform=fct_transform, filter_out=filter_out,
                                 force_allow=force_allow, exc=exc)

        fftp.start_transfering(delay=delay)

        ftn = FileTreeNode(os.path.join(root_local, ".."),
                           filter=lambda root, path, f, dir: not dir)
        fftp = FolderTransferFTP(ftn, ftp, sfile,
                                 root_web=root_web.replace("helpsphinx", ""), fLOG=fLOG,
                                 footer_html=footer_html, content_filter=content_filter,
                                 is_binary=is_binary, text_transform=fct_transform,
                                 filter_out=filter_out)

        fftp.start_transfering()

    ftp.close()


def publish_teachings_to_web(login, ftpsite="ftp.xavierdupre.fr",  # pylint: disable=W0102
                             tracking_id=None,
                             location="c:\\jenkins\\pymy\\%s\\%s%s\\dist\\%s",
                             rootw="/www/htdocs/app/%s/%s",
                             folder_status=".",
                             layout=[("html", "helpsphinx")],
                             modules=None, password=None, force_allow=None,
                             suffix=("_UT_%d%d_std" % sys.version_info[:2],),
                             delay=0.5, exc=False, exc_transfer=False,
                             transfer=True, additional_projects=None,
                             ftps='FTP', page_transform=None, fLOG=print):
    """
    Copies the documentation to the website.

    @param      login               login
    @param      ftpsite             ftp site
    @param      tracking_id         tracking_id
    @param      location            location of Jenkins build
    @param      rootw               root on ftp site
    @param      folder_status       folder status
    @param      modules             list of modules to publish, if None, use @see fn get_teaching_modules
    @param      password            if None, if will asked
    @param      layout              last part of the folders
    @param      suffix              suffixes to append to the project name
    @param      force_allow         allow to publish files even if they contain these strings
                                    whereas they seem to be credentials
    @param      delay               delay between two files being transferred
    @param      exc                 raise exception if not found (True) or skip (False)
    @param      exc_transfer        raise an exception if cannot be transfered
    @param      transfer            starts transfering, otherwise returns the list of
                                    transfering task to do
    @param      additional_projects additional projects
    @param      ftps                use protocol FTP, TLS, or SFTP
    @param      page_transform      function which transforms a page before uploading it,
                                    @see fn text_transform
    @param      fLOG                logging function

    Example of use::

        import sys
        import os
        from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
        from tkinterquickhelper.funcwin import open_window_params
        from ensae_teaching_cs.automation.ftp_publish_helper import publish_teachings_to_web

        login = "..."
        website = "ftp...."
        rootw = "/www/htdocs/app/%s/%s"

        password = None

        publish_teachings_to_web(login, ftpsite=website,
            tracking_id="tracking_id",
            location="<something>\\\\%s\\\\%s%s\\\\dist\\\\%s",
            rootw=rootw,
            folder_status=os.path.abspath("."),
            password=password)

    Example of an additional projects:

    ::

        other_projects = [dict(status_file="status_projects.txt"),
                               root_local="...", root_web="...")]
    """
    if modules is None:
        modules = get_teaching_modules(branch=False)

    if tracking_id is None:
        tracking_id = ""
    else:
        # footer = """
        # """.format(tracking_id)
        footer = ""

    if password is None and transfer:
        raise ValueError("password is empty")

    location = os.path.abspath(location)
    if folder_status is None:
        folder_status = os.path.abspath(os.path.dirname(__file__))
    else:
        folder_status = os.path.abspath(folder_status)

    if not isinstance(suffix, (tuple, list)):
        suffix = [suffix]

    projects = []
    for module in modules:
        fLOG(
            f"[ensae_teaching_cs] PUBLISH '{module}' - layout '{layout}'")
        for lay in layout:
            for suf in suffix:
                root = os.path.abspath(location %
                                       (module, module, suf, lay[0]))
                if transfer and os.path.exists(root):
                    break
            if transfer and not os.path.exists(root):
                if exc:
                    p = os.path.abspath(location %
                                        (module, module, suffix[0], lay[0]))
                    raise FileNotFoundError(
                        f"First tried '{root}'\n last tried '{p}'")
                else:
                    continue
                fLOG("   ", root)
            rw = rootw % (module, lay[1])

            project = dict(status_file=os.path.join(folder_status, f"status_{module}.txt"),
                           local=root, root_local=root, root_web=rw)
            projects.append(project)

        if module == "ensae_teaching_cs":
            lay = [_ for _ in layout if _[0] == "html"][0]
            if transfer and not os.path.exists(root):
                if exc:
                    raise FileNotFoundError(root)
                else:
                    continue

            def _update_path(pth):
                for a, b in [("\\build", "\\build3"),
                             ("\\html", "\\html3"),
                             ("/build", "/build3"),
                             ("/html", "/html3")]:
                    pth = pth.replace(a, b)
                return pth

            local = _update_path(root)
            fLOG(f"[ensae_teaching_cs] checking folder '{local}'")
            fLOG(f"[ensae_teaching_cs] root is '{root}'")
            if os.path.exists(local):
                fLOG(f"[ensae_teaching_cs] found '{local}'")
                project = dict(status_file=os.path.join(folder_status, f"status_3_{module}.txt"),
                               local=local, root_local=local,
                               root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx3"))
                projects.append(project)
                project = dict(status_file=os.path.join(folder_status, f"status_2_{module}.txt"),
                               local=local, root_local=local,
                               root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx2"))
                projects.append(project)
            else:
                fLOG("[ensae_teaching_cs] looking into DOC1, DOC3")
                root1 = root.replace("_UT_", "_DOC1_")
                if transfer:
                    if not os.path.exists(root1):
                        if exc:
                            raise FileNotFoundError(root1)
                        else:
                            pass
                    else:
                        project = dict(status_file=os.path.join(folder_status, f"status_doc1_{module}.txt"),
                                       local=root1, root_local=root1,
                                       root_web=(rootw % (module, lay[1])).replace("_no_clean", ""))
                        projects.append(project)

                root3 = root.replace("_UT_", "_DOC3_").replace("html", "html3")
                if transfer:
                    if not os.path.exists(root3):
                        if exc:
                            raise FileNotFoundError(root3)
                    else:
                        project = dict(status_file=os.path.join(folder_status, f"status_doc3_{module}.txt"),
                                       local=root3, root_local=root3,
                                       root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx3"))
                        projects.append(project)
                        project = dict(status_file=os.path.join(folder_status, f"status_doc2_{module}.txt"),
                                       local=root3, root_local=root3,
                                       root_web=(rootw % (module, lay[1])).replace("_no_clean", "").replace("/helpsphinx", "/helpsphinx2"))
                        projects.append(project)

    # publish
    if additional_projects:
        for proj in additional_projects:
            if 'root_local' not in proj:
                if 'folder' not in proj:
                    raise KeyError(
                        f"Key 'folder' or 'root_local' must be specified in {proj}.")
                proj = proj.copy()
                proj['root_local'] = proj['folder']
            if 'folder' not in proj:
                proj = proj.copy()
                proj['folder'] = proj['root_local']
            if 'local' not in proj:
                proj = proj.copy()
                proj['local'] = os.path.dirname(proj['root_local'])
            projects.append(proj)

    if transfer:
        publish_documentation(projects, ftpsite=ftpsite, login=login, password=password,
                              footer_html=footer, force_allow=force_allow, delay=delay,
                              exc=exc_transfer, ftps=ftps, page_transform=page_transform,
                              fLOG=fLOG)
    return projects
