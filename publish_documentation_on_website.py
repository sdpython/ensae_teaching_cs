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
try:
    import pyquickhelper
except ImportError:
    sys.path.append(r"../pyquickhelper/src")
try:
    import pyensae
except ImportError:
    sys.path.append(r"../pyensae/src")
try:
    import pymyinstall
except ImportError:
    sys.path.append(r"../pymyinstall/src")
try:
    import ensae_teaching_cs
except ImportError:
    sys.path.append(r"../ensae_teaching_cs/src")

from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
from pyquickhelper.funcwin import open_window_params
from ensae_teaching_cs.automation.ftp_publish_helper import publish_teachings_to_web

if True:
    params = {"password": "", login: ""}
    params = open_window_params(params, title="password",
                                help_string="password",
                                key_save="my_password")
    password = params["password"]
    login = params["loging"]
else:
    raise NotImplementedError()

publish_teachings_to_web(login=login, ftpsite="ftp.xavierdupre.fr", google_id="UA-2815364-1",
        modules=["pyquickhelper",
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
                 "ensae_teaching_cs"],
        password=password)