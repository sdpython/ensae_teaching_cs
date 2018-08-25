# -*- coding: utf-8 -*-
"""
Publish documentation
=====================

The script shows how the documentation of this module and others is published.
"""
user = "LOGIN"
ftpsite = "ftp.SOMETHING"
rootw = "/www/htdocs/app/%s/helpsphinx"
rootw2 = "/lesenfantscodaient.fr"

footer = """
<script src="http://www.google-analytics.com/urchin.js" type="text/javascript"></script>
<script type="text/javascript">
_uacct = "GOOGLE_ANALYTICS_CODE";
urchinTracker();
</script>
"""

#########################################
# import

import sys
import os
import keyring
import random


#########################################
# logging

from pyquickhelper.loghelper import fLOG  # publish_lectures
fLOG(OutputPrint=True)

#########################################
# import des fonctions dont on a besoin

from pyquickhelper.filehelper import TransferFTP, FileTreeNode, FolderTransferFTP
from ensae_teaching_cs.automation.ftp_publish_helper import publish_teachings_to_web

##################
# accès au site web

# on utilise keyring pour stocker les identifiants
# à commenter ou décommenter au besoin
user = keyring.get_password("web", "ensae_teaching_cs,user")
pwd = keyring.get_password("web", "ensae_teaching_cs,pwd")
ftpsite = keyring.get_password("web", "ensae_teaching_cs,ftp")
code_google = keyring.get_password(
    "web", "ensae_teaching_cs,google")
if pwd is None or user is None or ftpsite is None or code_google is None:
    print("ERROR: password or user or ftpsite is empty, you should execute:")
    print(
        '    keyring.set_password("web", "ensae_teaching_cs,user", "..")')
    print(
        '    keyring.set_password("web", "ensae_teaching_cs,pwd", "..")')
    print(
        '    keyring.set_password("web", "ensae_teaching_cs,ftp", "..")')
    print(
        '    keyring.set_password("web", "ensae_teaching_cs,google", "..")')
    print("Exit")
    sys.exit(0)
if code_google is None:
    raise ValueError("code_google is empty")


##################
# liste des modules à mettre à jouer
# commenter ou décommenter les modules
modules = [
    "actuariat_python",
    "code_beatrix",
    "cpyquickhelper",
    "ensae_projects",
    "jupytalk",
    "jyquickhelper",
    "mlstatpy",
    "pyensae",
    "pymmails",
    "pymyinstall",
    "pyquickhelper",
    "tkinterquickhelper",
    "pyrsslocal",
    "pysqllike",
    "python3_module_template",
    "teachpyx",
    #
    "ensae_teaching_cs"
]

random.shuffle(modules)

##################
# valeurs par défaut

# emplacement local de la documentation
location = "d:\\jenkins\\pymy\\%s\\%s%s\\dist\\%s"
rootw = "/www/htdocs/app/%s/%s"                   # destination sur le site FTP
# seconde destination pour le site lesenfantscodaient.fr
rootw2 = "/lesenfantscodaient.fr"
google_id = code_google                         # identifiant google analytics
suffix = ("_UT_%d%d_std" % sys.version_info[:2],)

modules0 = modules
modules = [_ for _ in modules if os.path.exists(
    location % (_, _, suffix[0], "html"))]
if len(modules) == 0:
    _ = modules0[0]
    one = location % (_, _, suffix[0], "html")
    raise ValueError("No module can be updated, for example '{0}'".format(one))
print("List of modules to publish:")
for i, mod in enumerate(sorted(modules)):
    print("  {0}/{1}: {2}".format(i + 1, len(modules), mod))

##################
# La fonction :func:`publish_teachings_to_web cache` cache beaucoup de chose.
publish_teachings_to_web(login=user, ftpsite=ftpsite, google_id=google_id,
                         location=location, rootw=rootw, rootw2=rootw2,
                         modules=modules, password=pwd, suffix=suffix,
                         force_allow=["xavierdupre"])
