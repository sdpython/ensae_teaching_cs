"""
@file
@brief Customize a Windows Setup for these teachings
"""

import os
import shutil

from pyquickhelper.filehelper import remove_folder


def last_function(innosetup, folders, verbose=False, fLOG=print):
    """
    applies last modifications to the setup

    @param          innosetup   innosetup script which defines the setup
    @param          folders     dictionary with keys *workspace*, *python*, *tools*, *build*, *docs*
    @param          verbose     verbose
    @param          fLOG        logging function
    """
    from pymyinstall.win_installer.win_setup_r import r_run_script

    work = folders["workspace"]
    python = folders["python"]
    tools = folders["tools"]
    build = os.path.join(folders["build"], "custom_ensae_teaching_cs")
    docs = os.path.join(work, "docs")
    logs = folders["logs"]
    this = os.path.abspath(os.path.dirname(__file__))
    doc_annee = [os.path.join(this, "..", "..", "..", "_doc", "notebooks", sub)
                 for sub in ["td1a", "td2a", "td3a", "1a", "2a", "expose"]]

    if not os.path.exists(build):
        os.mkdir(build)

    # folders
    fLOG("folders:", folders)
    fLOG("innosetup:", innosetup)

    # docs
    fLOG("--- cleaning creating folder", docs)
    if os.path.exists(docs):
        remove_folder(docs)
    os.mkdir(docs)

    # RSS
    fLOG("--- update rss.list.xml")
    # flake8 is no happy with: from .. import __blog__
    __blog__ = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "rss_teachings.xml"))

    rssfile = os.path.join(folders["config"], "rss_list.xml")
    shutil.copy(__blog__, rssfile)

    # R_install
    fLOG("--- R install")
    r_script = os.path.join(os.path.dirname(__file__), "R_install.r")
    if os.path.exists(r_script):
        r_run_script(os.path.join(tools, "R"), r_script, os.path.join(
            logs, "r_ensae_teaching_cs.install.log.txt"))

    # documentation
    fLOG("--- documentation, TDs +++")
    for dist in doc_annee:
        end = os.path.split(dist)[-1]
        to = os.path.join(docs, end)
        if not os.path.exists(to):
            os.mkdir(to)
        for ipy in os.listdir(dist):
            if ipy.endswith("ipynb"):
                if verbose:
                    fLOG("copy ", ipy)
                full = os.path.join(dist, ipy)
                shutil.copy(full, to)

    # others packages not from Microsoft
    from pymyinstall import ModuleInstall
    from pymyinstall.win_installer.win_packages import win_install_package_other_python, is_package_installed

    # modules
    modules = [ModuleInstall("pyquickhelper", "pip"),
               ModuleInstall("pyensae", "pip"),
               ModuleInstall("pyrsslocal", "pip"),
               ModuleInstall("code_beatrix", "pip"),
               ModuleInstall("pymmails", "pip"),
               ModuleInstall("pymyinstall", "pip"),
               ModuleInstall("ensae_teaching_cs", "pip"),
               ModuleInstall("actuariat_python", "pip"),
               ]

    # new packages
    fLOG("--- download new packages")
    pack = []
    for mod in modules:
        mname = mod.mname if mod.mname is not None else mod.name
        if not is_package_installed(python, [mod.name, mname]):
            fLOG("download:", mod.name)
            p = mod.download(temp_folder=build)
            pack.append((p, mod))

    # install packages
    fLOG("--- install packages")
    for p, mod in pack:
        fLOG("install", os.path.split(p)[-1])
        win_install_package_other_python(python, p, verbose=verbose, fLOG=fLOG)

    # remove unnecessary folders
    fLOG("--- remove too big folfers")
    to_remove = []
    for rem in to_remove:
        sub = os.path.join(python, rem)
        if os.path.exists(sub):
            fLOG("remove", sub)
            remove_folder(sub)

    # modifies the setup
    fLOG("--- modifies the setup")
    with open(innosetup, "r", encoding="utf8") as f:
        content = f.read()
    with open(innosetup, "w", encoding="utf8") as f:
        f.write(content)
