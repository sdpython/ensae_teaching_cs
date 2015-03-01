# -*- coding: utf-8 -*-
#  Copyright (C) 2014 ---------------
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions
#  are met:
#
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#
#  3. All advertising materials mentioning features or use of this
#     software must display the following acknowledgment:
#     "This product includes software developed by
#      Xavier Dupré <xavier.dupre AT gmail.com>"
#
#  4. Redistributions of any form whatsoever must retain the following
#     acknowledgment:
#     "This product includes software developed by
#      Xavier Dupré <xavier.dupre AT gmail.com>."
#
#  THIS SOFTWARE IS PROVIDED BY Xavier Dupré ``AS IS'' AND ANY
#  EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL Roman V. Kiseliov OR
#  ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
#  HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
#  STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
#  OF THE POSSIBILITY OF SUCH DAMAGE.

import sys,os
from distutils.core import setup
from setuptools import find_packages

if os.path.exists("version.txt") :
    with open("version.txt", "r") as f : lines = f.readlines()
    subversion = lines[0].strip("\r\n ")
else :
    subversion = 1

project_var_name    = "ensae_teaching_cs"
sversion            = "0.6"
versionPython       = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path                = "Lib/site-packages/" + project_var_name
readme              = 'README.rst'


KEYWORDS = \
project_var_name + ', ENSAE, sqllite, database, teachings'

DESCRIPTION = \
"""Module which contains materials for teaching puroposes, also includes pythonnet."""

CLASSIFIERS = \
[
'Programming Language :: Python :: 3',
'Intended Audience :: Developers',
'Topic :: Scientific/Engineering',
'Topic :: Education',
'License :: OSI Approved :: BSD License',
'Development Status :: 5 - Production/Stable'
]


if "bdist_wininst" not in sys.argv :
    EXT_MODULES = [
                    #Extension(project_var_name + '.subproject.sample_module',
                    #    ['src/' + project_var_name + '/subproject/sample_module.cpp'],
                    #    include_dirs = ['src/' + project_var_name + '/subproject']),
                ]
else :
    EXT_MODULES = [ ]

packages     = find_packages('src', exclude='src')
package_dir  = { k: "src/" + k.replace(".","/") for k in packages }
package_data = { project_var_name + ".pythonnet.py33"   : ["*.pyd","*.txt","*.dll"],
                 project_var_name + ".pythonnet.py33x64": ["*.pyd","*.txt","*.dll"],
                 project_var_name + ".pythonnet.py34"   : ["*.pyd","*.txt","*.dll"],
                 project_var_name + ".pythonnet.py34x64": ["*.pyd","*.txt","*.dll"],
                 project_var_name + ".pythonnet.csdll": ["*.dll"],
                 }

if os.path.exists(readme):
    try:
        with open(readme, "r", encoding='utf-8') as f : long_description = f.read()
        long_description = long_description.replace("\ufeff","")
    except :
        try:
            with open(readme, "r") as f : long_description = f.read()
        except:
            long_description = ""
else:
    long_description = ""

if "--verbose" in sys.argv :
    print ("---------------------------------")
    print ("package_dir =",package_dir)
    print ("packages    =",packages)
    print ("package_data=",package_data)
    print ("current     =", os.path.abspath(os.getcwd()))
    print ("---------------------------------")

def import_pyquickhelper():
    try:
        import pyquickhelper
    except ImportError:
        sys.path.append ( os.path.normpath (os.path.abspath(os.path.join("..", "pyquickhelper", "src" ))))
        try:
            import pyquickhelper
        except ImportError as e :
            raise ImportError("module pyquickhelper is needed to build the documentation ({0})".format(sys.executable)) from e
    return pyquickhelper

if "clean_space" in sys.argv:
    pyquickhelper = import_pyquickhelper()

    fold = os.path.dirname(__file__)
    fold = os.path.abspath(fold)
    rem  = pyquickhelper.remove_extra_spaces_folder(fold, extensions=[".py","rst",".bat",".sh"])
    print("number of impacted files", len(rem))

elif "clean_pyd" in sys.argv:
    pyquickhelper = import_pyquickhelper()
    pyquickhelper.clean_exts(exts=[".so", ".o"])

elif "build_sphinx_one" in sys.argv:
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
            generate_help_sphinx(project_name, module_name=project_var_name)
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
                generate_help_sphinx(project_name, module_name=project_var_name)
            except ImportError as e:
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
    else :

        if not os.path.exists("_doc/sphinxdoc/source"):
            raise FileNotFoundError("you must get the source from GitHub to build the documentation")

        from pyquickhelper import fLOG, generate_help_sphinx

        fLOG (OutputPrint = True)
        project_name = os.path.split(os.path.split(os.path.abspath(__file__))[0])[-1]

        if sys.platform.startswith("win"):
            generate_help_sphinx(project_name, module_name = project_var_name)
            generate_help_sphinx(project_name,
                    nbformats=['ipynb', 'html', 'python', 'rst', 'docx','pdf'],
                    layout = [ "pdf",
                              "html",
                              ("html", "build2", {"html_theme":"basicstrap"}, "source/conf2"),
                              ("html", "build3", {"html_theme":"bootstrap"}, "source/conf3"),
                              ],
                    module_name = project_var_name)
        else:
            # unable to test latex conversion due to adjustbox.sty missing package
            generate_help_sphinx(project_name,
                    nbformats=['ipynb', 'html', 'python', 'rst'],
                    layout = [ "pdf",
                              "html",
                              ("html", "build2", {"html_theme":"basicstrap"}, "source/conf2"),
                              ("html", "build3", {"html_theme":"bootstrap"}, "source/conf3"),
                              ],
                    module_name = project_var_name)

elif "unittests" in sys.argv:

    if not os.path.exists("_unittests"):
        raise FileNotFoundError("you must get the source from GitHub to run the unittests")

    run_unit = os.path.join("_unittests", "run_unittests.py")
    if not os.path.exists(run_unit):
        raise FileNotFoundError("the folder should contain run_unittests.py")

    def skip_function(name,code):
        if "notebook test" in code: return True
        if "test notebook" in code: return True
        return False

    pyquickhelper = import_pyquickhelper()
    pyquickhelper.main_wrapper_tests(run_unit, add_coverage=True, skip_function = skip_function)

elif "unittests_all" in sys.argv:

    if not os.path.exists("_unittests"):
        raise FileNotFoundError("you must get the source from GitHub to run the unittests")

    run_unit = os.path.join("_unittests", "run_unittests.py")
    if not os.path.exists(run_unit):
        raise FileNotFoundError("the folder should contain run_unittests.py")

    pyquickhelper = import_pyquickhelper()
    pyquickhelper.main_wrapper_tests(run_unit, add_coverage=True)

elif "build_pres" in sys.argv or "build_pres_2A" in sys.argv \
     or "build_pres_3A" in sys.argv :
    # we generate the documentation for the presentation

    def get_executables_path() :
        """
        returns the paths to Python, Python Scripts

        @return     a list of paths
        """
        res  = [ os.path.split(sys.executable)[0] ]
        res += [ os.path.join(res[-1], "Scripts") ]
        if sys.platform.startswith("win") :
            ver = "c:\\Python%d%d" % (sys.version_info.major, sys.version_info.minor)
            res += [ver ]
            res += [ os.path.join(res[-1], "Scripts") ]
        return res

    suffix = ""
    suffix = "_2A" if "build_pres_2A" in sys.argv else suffix
    suffix = "_3A" if "build_pres_3A" in sys.argv else suffix

    #  run the documentation generation
    if sys.platform.startswith("win"):
        temp = os.environ ["PATH"]
        pyts = get_executables_path()
        script = ";".join(pyts)
        temp = script + ";" + temp
        os.environ["PATH"] = temp
        pa = os.getcwd ()
        thispath = os.path.normpath(os.path.split(__file__)[0])
        docpath  = os.path.normpath(os.path.join(thispath, "_doc","presentation" + suffix))
        os.chdir (docpath)

    lay     = "html"
    build   = "build"
    over    = ""
    sconf   = ""
    cmd     = "sphinx-build -b {1} -d {0}/doctrees{2}{3} source {0}/{1}".format(build, lay, over, sconf)
    os.system(cmd)

    if sys.platform.startswith("win"):
        os.chdir (pa)

elif "build_pres_1Ap" in sys.argv  :
    # we generate the documentation for the presentation

    def get_executables_path() :
        """
        returns the paths to Python, Python Scripts

        @return     a list of paths
        """
        res  = [ os.path.split(sys.executable)[0] ]
        res += [ os.path.join(res[-1], "Scripts") ]
        if sys.platform.startswith("win") :
            ver = "c:\\Python%d%d" % (sys.version_info.major, sys.version_info.minor)
            res += [ver ]
            res += [ os.path.join(res[-1], "Scripts") ]
        return res

    #  run the documentation generation
    if sys.platform.startswith("win"):
        temp = os.environ ["PATH"]
        pyts = get_executables_path()
        script = ";".join(pyts)
        temp = script + ";" + temp
        os.environ["PATH"] = temp
        pa = os.getcwd ()
        thispath = os.path.normpath(os.path.split(__file__)[0])
        docpath  = os.path.normpath(os.path.join(thispath, "_doc","presentation_projets","a2015"))
        os.chdir (docpath)

    lay     = "html"
    build   = "build"
    over    = ""
    sconf   = ""
    cmd     = "sphinx-build -b {1} -d {0}/doctrees{2}{3} source {0}/{1}".format(build, lay, over, sconf)
    os.system(cmd)

    if sys.platform.startswith("win"):
        os.chdir (pa)

else :

    setup(
        name                    = project_var_name,
        version                 = '%s.%s' %(sversion, subversion) if "register" in sys.argv or "sdist" in sys.argv or "bdist_wheel" in sys.argv or "bdist_msi" in sys.argv or "install" in sys.argv  else 'py%s-%s.%s' % (versionPython, sversion, subversion),
        author                  = 'Xavier Dupré',
        author_email            = 'xavier.dupre AT gmail.com',
        url                     = "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html",
        download_url            = "https://github.com/sdpython/ensae_teaching_cs/",
        description             = DESCRIPTION,
        long_description        = long_description,
        keywords                = KEYWORDS,
        classifiers             = CLASSIFIERS,
        packages                = packages,
        package_dir             = package_dir,
        package_data            = package_data,
        #data_files              = data_files,
        install_requires        = [  "pyensae", "pyquickhelper", "pymyinstall" ],
        ext_modules             = EXT_MODULES,
        #include_package_data    = True,
        )