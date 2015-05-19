# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "ensae_teaching_cs"
sversion = "0.6"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'

KEYWORDS = project_var_name + ', ENSAE, sqllite, database, teachings'
DESCRIPTION = """Module which contains materials for teaching puroposes, also includes pythonnet."""
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
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
                project_var_name + ".pythonnet.csdll": ["*.dll"],
                project_var_name + ".automation": ["*.xml"],
                project_var_name: ["rss_teachings.xml"],
                }


############
# functions
############


def is_local():
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
       "run27" in sys.argv or \
       "sdist" in sys.argv or \
       "setupdep" in sys.argv or \
       "test_local_pypi" in sys.argv or \
       "upload_docs" in sys.argv or \
       "write_version" in sys.argv or \
       "build_sphinx_one" in sys.argv or \
       "build_sphinx_catch" in sys.argv or \
       "unittests_all" in sys.argv or \
       "build_pres" in sys.argv or \
       "build_pres_2A" in sys.argv or \
       "build_pres_3A" in sys.argv or \
       "build_pres_1Ap" in sys.argv:
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
                        "pyquickhelper",
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

if is_local():
    def write_version():
        pyquickhelper = import_pyquickhelper()
        from pyquickhelper import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    if os.path.exists("version.txt"):
        with open("version.txt", "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
    else:
        raise FileNotFoundError("version.txt")
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""

if "--verbose" in sys.argv:
    verbose()

if is_local() and "build_sphinx" not in sys.argv and \
        "unittests" not in sys.argv:
    pyquickhelper = import_pyquickhelper()
    r = pyquickhelper.process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        unittest_modules=["pyquickhelper"],
        requirements=["pyquickhelper", "pyrsslocal", "pyensae", "pymmails"],
        blog_list=os.path.abspath(os.path.join("src", project_var_name, package_data[project_var_name][0])))

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

            if not exist dist\\html_pres mkdir dist\\html_pres
            if not exist dist\\html_pres_2A mkdir dist\\html_pres_2A
            if not exist dist\\html_pres_3A mkdir dist\\html_pres_3A
            if not exist dist\\html_pres_1Ap mkdir dist\\html_pres_1Ap

            xcopy /E /C /I /Y _doc\\presentation_projets\\a2015\\build\\html dist\\html_pres_1Ap
            if %errorlevel% neq 0 exit /b %errorlevel%
            xcopy /E /C /I /Y _doc\\presentation_2A\\build\\html dist\\html_pres_2A
            if %errorlevel% neq 0 exit /b %errorlevel%
            xcopy /E /C /I /Y _doc\\presentation_3A\\build\\html dist\\html_pres_3A
            if %errorlevel% neq 0 exit /b %errorlevel%
            xcopy /E /C /I /Y _doc\\presentation\\build\\html dist\\html_pres
            if %errorlevel% neq 0 exit /b %errorlevel%
            """.replace("            ", "")

        path_exe = os.path.dirname(sys.executable)
        from pyquickhelper.pycode.windows_scripts import windows_prefix
        with open("auto_setup_build_pres.bat", "w") as f:
            f.write(windows_prefix.replace("__PY34_X64__", path_exe))
            f.write("\n")
            f.write(pres)

        with open("auto_unittest_setup_help.bat", "r") as f:
            content = f.read()

        addition = """
                if not exist dist\\html2 mkdir dist\\html2
                xcopy /E /C /I /Y _doc\\sphinxdoc\\build2\\html dist\\html2
                if exist _doc\\sphinxdoc\\build2\\latex xcopy /E /C /I /Y _doc\\sphinxdoc\\build2\\latex\\*.pdf dist\\html2
                if %errorlevel% neq 0 exit /b %errorlevel%

                if not exist dist\\html3 mkdir dist\\html3
                xcopy /E /C /I /Y _doc\\sphinxdoc\\build3\\html dist\\html3
                if exist _doc\\sphinxdoc\\build3\\latex xcopy /E /C /I /Y _doc\\sphinxdoc\\build3\\latex\\*.pdf dist\\html3
                if %errorlevel% neq 0 exit /b %errorlevel%
                """.replace("                ", "")

        content += "\n" + addition + "\n" + pres

        with open("auto_unittest_setup_help.bat", "w") as f:
            f.write(content)

        with open("auto_setup_unittests_left.bat", "w") as f:
            f.write("auto_cmd_any_setup_command.bat custom_left default left")

else:
    r = False

if not r:

    def skip_function(name, code):
        if "notebook test" in code:
            return True
        if "test notebook" in code:
            return True
        return False

    def not_skip_function(name, code):
        return not skip_function(name, code)

    if "build_sphinx_one" in sys.argv:
        pyquickhelper = import_pyquickhelper()

        if "--help" in sys.argv:
            print(pyquickhelper.get_help_usage())
        else:

            if not os.path.exists("_doc/sphinxdoc/source"):
                raise FileNotFoundError(
                    "you must get the source from GitHub to build the documentation")

            from pyquickhelper import fLOG, generate_help_sphinx

            fLOG(OutputPrint=True)
            project_name = os.path.split(
                os.path.split(os.path.abspath(__file__))[0])[-1]

            if sys.platform.startswith("win"):
                generate_help_sphinx(
                    project_name, module_name=project_var_name)
            else:
                # unable to test latex conversion due to adjustbox.sty missing
                # package
                generate_help_sphinx(project_name, nbformats=["ipynb", "html", "python", "rst"],
                                     module_name=project_var_name)

    elif "build_sphinx_catch" in sys.argv:
        pyquickhelper = import_pyquickhelper()

        if "--help" in sys.argv:
            print(pyquickhelper.get_help_usage())
        else:

            if not os.path.exists("_doc/sphinxdoc/source"):
                raise FileNotFoundError(
                    "you must get the source from GitHub to build the documentation")

            from pyquickhelper import fLOG, generate_help_sphinx

            fLOG(OutputPrint=True)
            project_name = os.path.split(
                os.path.split(os.path.abspath(__file__))[0])[-1]

            if sys.platform.startswith("win"):
                try:
                    generate_help_sphinx(
                        project_name,
                        module_name=project_var_name)
                except ImportError as e:
                    print(
                        "################### IMPORT ERROR on build_sphinx_catch #######")
                    sys.exit(0)
            else:
                # unable to test latex conversion due to adjustbox.sty missing
                # package
                generate_help_sphinx(project_name, nbformats=["ipynb", "html", "python", "rst"],
                                     module_name=project_var_name)

    elif "build_sphinx" in sys.argv:
        pyquickhelper = import_pyquickhelper()

        if "--help" in sys.argv:
            print(pyquickhelper.get_help_usage())
        else:

            if not os.path.exists("_doc/sphinxdoc/source"):
                raise FileNotFoundError(
                    "you must get the source from GitHub to build the documentation")

            from pyquickhelper import fLOG, generate_help_sphinx

            fLOG(OutputPrint=True)
            project_name = os.path.split(
                os.path.split(os.path.abspath(__file__))[0])[-1]

            if sys.platform.startswith("win"):
                #generate_help_sphinx(project_name, module_name=project_var_name)
                generate_help_sphinx(project_name,
                                     nbformats=[
                                         'ipynb',
                                         'html',
                                         'python',
                                         'rst',
                                         'slides',
                                         'docx',
                                         'pdf'],
                                     layout=["pdf",
                                             "html",
                                             ("html",
                                              "build2",
                                              {"html_theme":
                                                  "sphinx_py3doc_enhanced_theme"},
                                              "source/conf2"),
                                             ("html",
                                              "build3",
                                              {"html_theme": "bootstrap"},
                                              "source/conf3"),
                                             ],
                                     module_name=project_var_name)
            else:
                # unable to test latex conversion due to adjustbox.sty missing
                # package
                generate_help_sphinx(project_name,
                                     nbformats=[
                                         'ipynb', 'html', 'python', 'rst', 'slides'],
                                     layout=["pdf",
                                             "html",
                                             ("html",
                                              "build2",
                                              {"html_theme":
                                                  "sphinx_py3doc_enhanced_theme"},
                                              "source/conf2"),
                                             ("html",
                                              "build3",
                                              {"html_theme": "bootstrap"},
                                              "source/conf3"),
                                             ],
                                     module_name=project_var_name)

    elif "unittests" in sys.argv:

        if not os.path.exists("_unittests"):
            raise FileNotFoundError(
                "you must get the source from GitHub to run the unittests")

        run_unit = os.path.join("_unittests", "run_unittests.py")
        if not os.path.exists(run_unit):
            raise FileNotFoundError(
                "the folder should contain run_unittests.py")

        pyquickhelper = import_pyquickhelper()
        pyquickhelper.main_wrapper_tests(
            run_unit,
            add_coverage=True,
            skip_function=skip_function)

    elif "custom_left" in sys.argv:

        if not os.path.exists("_unittests"):
            raise FileNotFoundError(
                "you must get the source from GitHub to run the unittests")

        run_unit = os.path.join("_unittests", "run_unittests.py")
        if not os.path.exists(run_unit):
            raise FileNotFoundError(
                "the folder should contain run_unittests.py")

        pyquickhelper = import_pyquickhelper()
        pyquickhelper.main_wrapper_tests(
            run_unit,
            add_coverage=True,
            skip_function=not_skip_function)

    elif "build_pres" in sys.argv or "build_pres_2A" in sys.argv \
         or "build_pres_3A" in sys.argv:
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
                os.path.join(
                    thispath,
                    "_doc",
                    "presentation" +
                    suffix))
            os.chdir(docpath)

        lay = "html"
        build = "build"
        over = ""
        sconf = ""
        cmd = "sphinx-build -b {1} -d {0}/doctrees{2}{3} source {0}/{1}".format(
            build,
            lay,
            over,
            sconf)
        os.system(cmd)

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
                    "a2015"))
            os.chdir(docpath)

        lay = "html"
        build = "build"
        over = ""
        sconf = ""
        cmd = "sphinx-build -b {1} -d {0}/doctrees{2}{3} source {0}/{1}".format(
            build,
            lay,
            over,
            sconf)
        os.system(cmd)

        if sys.platform.startswith("win"):
            os.chdir(pa)

    else:

        setup(
            name=project_var_name,
            version='%s%s' % (sversion, subversion),
            author='Xavier Dupré',
            author_email='xavier.dupre AT gmail.com',
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
                "pyensae", "pyquickhelper", "pymyinstall", "pymmails",
                "scikit-learn", "pyrsslocal", "pandas", "numpy",
                "cvxopt"],
        )
