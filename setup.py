# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "ensae_teaching_cs"
sversion = "0.8"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"

KEYWORDS = project_var_name + ', ENSAE, sqllite, database, teachings'
DESCRIPTION = """Materials for teachings, notebooks, helpers..."""
CLASSIFIERS = [
    'Programming Language :: Python :: %d' % sys.version_info[0],
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {project_var_name + ".encrypted": ["*.crypted", "*.vigenere"],
                project_var_name + ".data.data_gutenberg": ["*.txt"],
                project_var_name + ".special.data": ["*.png", "*.txt"],
                project_var_name + ".data.data_1a": ["*.txt"],
                project_var_name + ".data.data_sql": ["*.db", "*.zip"],
                project_var_name + ".data.data_web": ["*.csv", "*.zip"],
                project_var_name + ".data.data_competition": ["*.bin"],
                project_var_name + ".data.zips": ["*.zip"],
                project_var_name + ".automation": ["*.xml", "*.r", "*.ico"],
                project_var_name: ["rss_teachings.xml"],
                }


############
# functions
############


def ask_help():
    return "--help" in sys.argv or "--help-commands" in sys.argv


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    from pyquickhelper.pycode.setup_helper import available_commands_list
    return available_commands_list(sys.argv)


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and not ask_help():
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Git version is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(versiontxt)
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion and not ask_help():
    # avoid uploading with a wrong subversion number
    raise Exception(
        "Git version is empty, cannot upload, is_local()={0}".format(is_local()))

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()

if is_local():
    import pyquickhelper
    logging_function = pyquickhelper.get_fLOG()
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function(OutputPrint=True)
    deps = ["pyquickhelper", "jyquickhelper", "pymmails", "pyensae", "pyenbc",
            "pyrsslocal", "pymyinstall", "mlstatpy", "tkinterquickhelper",
            "pandas_streaming", "fairtest", 'BLIBmpld3', 'manydataapi']
    if "html1" in sys.argv:
        layout = ["html"]
        sys.argv = [_ for _ in sys.argv if _ != "html1"]
    elif "html3" in sys.argv:
        layout = [("html", "build3", {
                           "html_theme": "bootstrap"}, "source/conf3")]
        sys.argv = [_ for _ in sys.argv if _ != "html3"]
    else:
        layout = ["html", ("html", "build3", {
                           "html_theme": "bootstrap"}, "source/conf3")]

    if "nblight" in sys.argv:
        nbformats = ['ipynb', 'html', 'rst', 'github']
        sys.argv = [_ for _ in sys.argv if _ != "nblight"]
    elif "nbpdf":
        nbformats = ['ipynb', 'html', 'python',
                     'rst', 'slides', 'pdf', 'github']
        sys.argv = [_ for _ in sys.argv if _ != "nbpdf"]
    else:
        nbformats = ['ipynb', 'html', 'python',
                     'rst', 'slides', 'github']

    def skip_function(name, code, duration):
        if "notebook test" in code:
            return True
        if "test notebook" in code:
            return True
        return default_skip_function(name, code, duration)

    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name, unittest_modules=[
            "pyquickhelper"],
        additional_notebook_path=deps, requirements=deps, additional_local_path=deps,
        blog_list=os.path.abspath(os.path.join(
            "src", project_var_name, package_data[project_var_name][0])),
        covtoken=("5e030cea-7d27-46e7-bb2e-2fc3db0ae9f6",
                  "'_UT_37_std' in outfile"),
        nbformats=nbformats, layout=layout,
        fLOG=logging_function, github_owner="sdpython")
else:
    r = False

if ask_help():
    from pyquickhelper.pycode import process_standard_options_for_setup_help
    process_standard_options_for_setup_help(sys.argv)

if not r:

    if "try_import" in sys.argv:
        sys.path.append("src")
        from ensae_teaching_cs.automation import *
        from ensae_teaching_cs.automation_students import *
        from ensae_teaching_cs.coding_party import *
        from ensae_teaching_cs.data import *
        from ensae_teaching_cs.faq import *
        from ensae_teaching_cs.helpers import *
        from ensae_teaching_cs.homeblog import *
        from ensae_teaching_cs.ml import *
        from ensae_teaching_cs.special import *
        from ensae_teaching_cs.td_1a import *
        from ensae_teaching_cs.td_2a import *
        from ensae_teaching_cs.tests import *

    else:
        # builds the setup

        from pyquickhelper.pycode import clean_readme
        long_description = clean_readme(long_description)

        setup(
            name=project_var_name,
            version='%s%s' % (sversion, subversion),
            author='Xavier Dupré',
            author_email='xavier.dupre@gmail.com',
            license="MIT",
            url="http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html",
            download_url="https://github.com/sdpython/ensae_teaching_cs/",
            description=DESCRIPTION,
            long_description=long_description,
            keywords=KEYWORDS,
            classifiers=CLASSIFIERS,
            packages=packages,
            package_dir=package_dir,
            package_data=package_data,
            install_requires=[
                "pyquickhelper>=1.8", "pyensae", "pymyinstall", "pymmails",
                "scikit-learn", "pyrsslocal", "pandas", "numpy", "pyenbc",
                "matplotlib", "jupyter", "mlstatpy", "manydataapi"],
        )
