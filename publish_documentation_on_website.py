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
