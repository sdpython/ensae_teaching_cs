"""
copy the documentation to the website
"""
login = "LOGIN"
website = "ftp.SOMETHING"
rootw = "/www/htdocs/app/%s/helpsphinx"
rootw2 = "/lesenfantscodaient.fr"

footer = """
<script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
<script type="text/javascript">
_uacct = "GOOGLE_ANALYTICS_CODE";
urchinTracker();
</script>
"""

import sys
import os
sys.path.append(r"../pyquickhelper/src")
sys.path.append(r"../pyensae/src")
sys.path.append(r"../ensae_teaching_cs/src")

from pyquickhelper import TransferFTP, FileTreeNode, FolderTransferFTP, open_window_params
from ensae_teaching_cs.automation.ftp_publish_helper import publish_documentation

params = {"password": ""}
params = open_window_params(params, title="password",
                            help_string="password",
                            key_save="my_password")
password = params["password"]

location = os.path.abspath(r"..\GitHub\%s\dist\html")
this = os.path.abspath(os.path.dirname(__file__))


projects = []
for module in [
        "pyquickhelper",
        "pyensae",
        "pymyinstall",
        "pysqllike",
        "pyrsslocal",
        "pymmails",
        "python_project_template",
        "actuariat_python",
        "code_beatrix",
        "ensae_teaching_cs",
]:

    root = os.path.abspath(location % module)
    root_web = rootw2 if module == "code_beatrix" else rootw % module
    project = dict(status_file=os.path.join(this, "status_%s.txt" % module),
                   local=root,
                   root_local=root,
                   root_web=root_web)
    projects.append(project)

    # others versions
    if module == "ensae_teaching_cs":

        project = dict(status_file=os.path.join(this, "status_%s.txt" % module),
                       local=root.replace("\\html", "\\html2"),
                       root_local=root.replace("\\html", "\\html2"),
                       root_web=(rootw % module).replace("/helpsphinx", "/helpsphinx2"))
        projects.append(project)

        root = os.path.abspath(location % module)
        project = dict(status_file=os.path.join(this, "status_%s.txt" % module),
                       local=root.replace("\\html", "\\html3"),
                       root_local=root.replace("\\html", "\\html3"),
                       root_web=(rootw % module).replace("/helpsphinx", "/helpsphinx3"))
        projects.append(project)

        # pres

        for suffix in ["", "_2A", "_3A", "_1Ap"]:
            root = os.path.abspath(location % module)
            project = dict(status_file=os.path.join(this, "status_%s.txt" % module),
                           local=root.replace(
                               "\\html", "\\html_pres" + suffix),
                           root_local=root.replace(
                               "\\html", "\\html_pres" + suffix),
                           root_web=(rootw % module).replace("/helpsphinx", "/pressphinx" + suffix).replace("_no_clean", ""))
            projects.append(project)


# publish

publish_documentation(projects,
                      ftpsite=website,
                      login=login,
                      password=password,
                      key_save="my_module_password",
                      footer_html=footer)
