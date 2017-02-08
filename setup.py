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

KEYWORDS = project_var_name + ', ENSAE, sqllite, database, teachings'
DESCRIPTION = """Module which contains materials for teaching puroposes, also includes pythonnet."""
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
package_data = {project_var_name + ".pythonnet.py33": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py33x64": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py34": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py34x64": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py27x64": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py35x64": ["*.pyd", "*.txt", "*.dll"],
                project_var_name + ".pythonnet.py36x64": ["*.pyd", "*.txt", "*.dll", "*."],
                project_var_name + ".pythonnet.csdll": ["*.dll"],
                project_var_name + ".encrypted": ["*.crypted", "*.vigenere"],
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


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    if \
       "bdist_msi" in sys.argv or \
       "build27" in sys.argv or \
       "build_script" in sys.argv or \
       "build_sphinx" in sys.argv or \
       "bdist_wheel" in sys.argv or \
       "bdist_wininst" in sys.argv or \
       "clean_pyd" in sys.argv or \
       "clean_space" in sys.argv or \
       "copy27" in sys.argv or \
       "copy_dist" in sys.argv or \
       "custom_left" in sys.argv or \
       "local_pypi" in sys.argv or \
       "notebook" in sys.argv or \
       "publish" in sys.argv or \
       "publish_doc" in sys.argv or \
       "register" in sys.argv or \
       "unittests" in sys.argv or \
       "unittests_LONG" in sys.argv or \
       "unittests_SKIP" in sys.argv or \
       "unittests_GUI" in sys.argv or \
       "run27" in sys.argv or \
       "sdist" in sys.argv or \
       "setupdep" in sys.argv or \
       "test_local_pypi" in sys.argv or \
       "upload_docs" in sys.argv or \
       "setup_hook" in sys.argv or \
       "build_sphinx_one" in sys.argv or \
       "build_sphinx_catch" in sys.argv or \
       "unittests_all" in sys.argv or \
       "copy_sphinx" in sys.argv or \
       "write_version" in sys.argv or \
       "build_pres" in sys.argv or \
       "build_pres_2A" in sys.argv or \
       "build_pres_3A" in sys.argv or \
       "build_pres_1Ap" in sys.argv:
        try:
            import_pyquickhelper()
        except ImportError:
            return False
        return True
    else:
        return False


def import_pyquickhelper():
    try:
        import pyquickhelper
    except ImportError:
        sys.path.append(
            os.path.normpath(
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__),
                        "..",
                        "pyquickhelper" if sys.version_info[
                            0] >= 3 else "py27_pyquickhelper_27",
                        "src"))))
        try:
            import pyquickhelper
        except ImportError as e:
            message = "module pyquickhelper is needed to build the documentation ({0}), not found in path {1}".format(
                sys.executable,
                sys.path[
                    -1])
            raise ImportError(message) from e
    return pyquickhelper


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

if is_local() and "--help" not in sys.argv and "--help-commands" not in sys.argv:
    def write_version():
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    if sys.version_info[0] != 2:
        write_version()

    if os.path.exists("version.txt"):
        with open("version.txt", "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("subversion is wrong: " + subversion)
    else:
        raise FileNotFoundError("version.txt")
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion:
    # avoid uploading with a wrong subversion number
    try:
        import pyquickhelper
        pyq = True
    except ImportError:
        pyq = False
    raise Exception(
        "subversion is empty, cannot upload, is_local()={0}, pyquickhelper={1}".format(is_local(), pyq))

##############
# common part
##############

if os.path.exists(readme):
    if sys.version_info[0] == 2:
        from codecs import open
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""

if "--verbose" in sys.argv:
    verbose()

if is_local() and "custom_left" not in sys.argv:
    pyquickhelper = import_pyquickhelper()
    logging_function = pyquickhelper.get_fLOG()
    from pyquickhelper.pycode import process_standard_options_for_setup
    logging_function(OutputPrint=True)
    deps = ["pyquickhelper", "jyquickhelper", "pymmails", "pyensae",
            "pyrsslocal", "pymyinstall", "mlstatpy"]
    layout = ["html", ("html", "build2", {"html_theme": "sphinx_py3doc_enhanced_theme"}, "source/conf2"),
              ("html", "build3", {"html_theme": "bootstrap"}, "source/conf3")]

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
                  "'_UT_35_std' in outfile"),
        nbformats=['ipynb', 'html', 'python',
                   'rst', 'slides', 'pdf', 'github'],
        layout=layout,
        fLOG=logging_function)

    if "build_script" in sys.argv and sys.platform.startswith("win"):
        pres = """
            :presentation:
            %pythonexe% -u setup.py build_pres
            if %errorlevel% neq 0 exit /b %errorlevel%
            %pythonexe% -u setup.py build_pres_2A
            if %errorlevel% neq 0 exit /b %errorlevel%
            %pythonexe% -u setup.py build_pres_3A
            if %errorlevel% neq 0 exit /b %errorlevel%
            %pythonexe% -u setup.py build_pres_1Ap
            if %errorlevel% neq 0 exit /b %errorlevel%
            echo #######################################################
            """.replace("            ", "")

        # auto_setup_build_pres.bat

        path_exe = os.path.dirname(sys.executable)
        from pyquickhelper.pycode.windows_scripts import windows_prefix
        with open("auto_setup_build_pres.bat", "w") as f:
            f.write(windows_prefix.replace("__PY35_X64__", path_exe))
            f.write("\n")
            f.write(pres)

else:
    r = False

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)

    if "try_import" in sys.argv:
        pyq = import_pyquickhelper()
        sys.path.append("src")
        from ensae_teaching_cs.automation import *
        from ensae_teaching_cs.automation_students import *
        from ensae_teaching_cs.coding_party import *
        from ensae_teaching_cs.data import *
        from ensae_teaching_cs.faq import *
        from ensae_teaching_cs.helpers import *
        from ensae_teaching_cs.homeblog import *
        from ensae_teaching_cs.ml import *
        from ensae_teaching_cs.mypython import *
        from ensae_teaching_cs.pythonnet import *
        from ensae_teaching_cs.special import *
        from ensae_teaching_cs.mypython import *
        from ensae_teaching_cs.td_1a import *
        from ensae_teaching_cs.td_2a import *
        from ensae_teaching_cs.tests import *

    elif "build_pres" in sys.argv or "build_pres_2A" in sys.argv or \
            "build_pres_3A" in sys.argv:
        # we generate the documentation for the presentation

        def get_executables_path():
            """
            returns the paths to Python, Python Scripts

            @return     a list of paths
            """
            res = [os.path.split(sys.executable)[0]]
            res += [os.path.join(res[-1], "Scripts")]
            if sys.platform.startswith("win"):
                ver = "c:\\Python%d%d" % (
                    sys.version_info.major, sys.version_info.minor)
                res += [ver]
                res += [os.path.join(res[-1], "Scripts")]
            return res

        suffix = ""
        suffix = "_2A" if "build_pres_2A" in sys.argv else suffix
        suffix = "_3A" if "build_pres_3A" in sys.argv else suffix

        #  run the documentation generation
        if sys.platform.startswith("win"):
            temp = os.environ["PATH"]
            pyts = get_executables_path()
            script = ";".join(pyts)
            temp = script + ";" + temp
            os.environ["PATH"] = temp
            pa = os.getcwd()
            thispath = os.path.normpath(os.path.split(__file__)[0])
            docpath = os.path.normpath(
                os.path.join(thispath, "_doc", "presentation" + suffix))
            os.chdir(docpath)

        lay = "html"
        build = "build"
        over = ""
        sconf = ""

        import_pyquickhelper()
        from pyquickhelper.helpgen import process_sphinx_cmd
        cmd_file = os.path.abspath(process_sphinx_cmd.__file__)
        cmd = '"{4}" "{5}" -b {1} -d {0}/doctrees{2}{3} source {0}/{1}'.format(
            build, lay, over, sconf, sys.executable, cmd_file)
        from pyquickhelper.loghelper import run_cmd
        out, err = run_cmd(cmd, wait=True, fLOG=print)
        print(out)
        print(err)

        if sys.platform.startswith("win"):
            os.chdir(pa)

    elif "build_pres_1Ap" in sys.argv:
        # we generate the documentation for the presentation

        def get_executables_path():
            """
            returns the paths to Python, Python Scripts

            @return     a list of paths
            """
            res = [os.path.split(sys.executable)[0]]
            res += [os.path.join(res[-1], "Scripts")]
            if sys.platform.startswith("win"):
                ver = "c:\\Python%d%d" % (
                    sys.version_info.major, sys.version_info.minor)
                res += [ver]
                res += [os.path.join(res[-1], "Scripts")]
            return res

        for year in [2015, 2016]:
            #  run the documentation generation
            if sys.platform.startswith("win"):
                temp = os.environ["PATH"]
                pyts = get_executables_path()
                script = ";".join(pyts)
                temp = script + ";" + temp
                os.environ["PATH"] = temp
                pa = os.getcwd()
                thispath = os.path.normpath(os.path.split(__file__)[0])
                docpath = os.path.normpath(
                    os.path.join(
                        thispath,
                        "_doc",
                        "presentation_projets",
                        "a%d" % year))
                os.chdir(docpath)
            else:
                raise NotImplementedError()

            lay = "html"
            build = "build"
            over = ""
            sconf = ""

            import_pyquickhelper()
            from pyquickhelper.helpgen import process_sphinx_cmd
            cmd_file = os.path.abspath(process_sphinx_cmd.__file__)
            cmd = '"{4}" "{5}" -b {1} -d {0}/doctrees{2}{3} source {0}/{1}'.format(
                build, lay, over, sconf, sys.executable, cmd_file)
            from pyquickhelper.loghelper import run_cmd
            out, err = run_cmd(cmd, wait=True, fLOG=print)
            print(out)
            print(err)

            if sys.platform.startswith("win"):
                os.chdir(pa)

    else:

        setup(
            name=project_var_name,
            version='%s%s' % (sversion, subversion),
            author='Xavier Dupré',
            author_email='xavier.dupre@gmail.com',
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
                "pyquickhelper", "pyensae", "pymyinstall", "pymmails",
                "scikit-learn", "pyrsslocal", "pandas", "numpy",
                "matplotlib", "jupyter", "mlstatpy"],
            # avoids downloading cvxopt (its installation is never easy)
            # extra_requires=["cvxopt"],
        )
