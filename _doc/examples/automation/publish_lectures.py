# -*- coding: utf-8 -*-
"""
Publish documentation
=====================

The script shows how the documentation of this module and others is published.
"""
user = "LOGIN"
ftpsite = "ftp.SOMETHING"
rootw = "/www/htdocs/app/%s/helpsphinx"
footer = """
"""

#########################################
# import

import sys
import os
import random
from pyquickhelper.loghelper import get_keyword


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
user = get_password("web", "ensae_teaching_cs,user")
pwd = get_password("web", "ensae_teaching_cs,pwd")
ftpsite = get_password("web", "ensae_teaching_cs,ftp")
code_google = get_password("web", "ensae_teaching_cs,google")
if pwd is None or user is None or ftpsite is None or code_google is None:
    print("ERROR: password or user or ftpsite is empty, you should execute:")
    print(
        '    set_password("web", "ensae_teaching_cs,user", "..")')
    print(
        '    set_password("web", "ensae_teaching_cs,pwd", "..")')
    print(
        '    set_password("web", "ensae_teaching_cs,ftp", "..")')
    print(
        '    set_password("web", "ensae_teaching_cs,google", "..")')
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
    "deeponnxcustom",
    "ensae_projects",
    "jupytalk",
    "jyquickhelper",
    "mlstatpy",
    "onnxcustom",
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
rootw = "/www/htdocs/app/%s/%s"     # destination sur le site FTP
tracking_id = code_tracking         # identifiant
suffix = ("_UT_%d%d_std" % sys.version_info[:2],)

modules0 = modules
modules = [_ for _ in modules if os.path.exists(
    location % (_, _, suffix[0], "html"))]
if len(modules) == 0:
    _ = modules0[0]
    one = location % (_, _, suffix[0], "html")
    raise ValueError(f"No module can be updated, for example '{one}'")
print("List of modules to publish:")
for i, mod in enumerate(sorted(modules)):
    print(f"  {i + 1}/{len(modules)}: {mod}")

##################
# La fonction :func:`publish_teachings_to_web cache` cache beaucoup de chose.
publish_teachings_to_web(login=user, ftpsite=ftpsite, tracking_id=tracking_id,
                         location=location, rootw=rootw,
                         modules=modules, password=pwd, suffix=suffix,
                         force_allow=["xavierdupre"])
