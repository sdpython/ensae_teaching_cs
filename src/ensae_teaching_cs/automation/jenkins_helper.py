"""
@file
@brief Set up a jenkins server with all the necessary job
"""
import os
import sys

from pyquickhelper import noLOG


engines_default = dict(anaconda2="c:\\Anaconda",
                       anaconda3="c:\\Anaconda3",
                       py35="c:\\Python35_x64",
                       default="c:\\Python34_x64",
                       winpython="c:\\APythonENSAE\\python")


def setup_jenkins_server(js,
                         github="sdpython",
                         modules=[  # update anaconda
                                    ("standalone [conda_update] [anaconda3]",
                                     "H H(0-1) * * 0"),
                                    "standalone [conda_update] [anaconda2] [27]",
                                    "standalone [local_pypi]",
                                    #"standalone [install]",
                                    #"standalone [update]",
                                    #"standalone [install] [py35]",
                                    #"standalone [update] [py35]",
                                    #"standalone [install] [winpython]",
                                    #"standalone [update] [winpython]",
                             # pyquickhelper and others,
                             ("pyquickhelper", "H H(2-3) * * 0"),
                             ("pysqllike", None, dict(success_only=True)),
                             ["python3_module_template", ],
                             "pyquickhelper [27] [anaconda2]",
                             ["pyquickhelper [winpython]",
                                        "python3_module_template [27] [anaconda2]",
                                        "pyquickhelper [anaconda3]", ],
                             "python3_module_template [anaconda3]",
                             "pysqllike [anaconda3]",
                             "pymmails [anaconda3]",
                             ["pymyinstall", "pyensae"],
                             ["pymmails", "pyrsslocal", ],
                             ["pyensae [anaconda3]", "pyensae [winpython]",
                                        "pyrsslocal [anaconda3]",
                                        "pyrsslocal [winpython]"],
                             ["pymyinstall [27] [anaconda2]",
                                 "pymyinstall [LONG]"],
                             # update, do not move, it depends on pyquickhelper
                             ("pymyinstall [update_modules]",
                                        "H H(0-1) * * 5"),
                             "pymyinstall [update_modules] [winpython]",
                             "pymyinstall [update_modules] [py35]",
                             "pymyinstall [update_modules] [anaconda2]",
                             "pymyinstall [update_modules] [anaconda3]",
                             # py35
                             ("pyquickhelper [py35]", "H H(2-3) * * 1"),
                             ["pysqllike [py35]", "pymmails [py35]",
                                        "python3_module_template [py35]", "pymyinstall [py35]"],
                             "pyensae [py35]",
                             "pyrsslocal [py35]",
                             # actuariat
                             [("actuariat_python", "H H(4-5) * * 0")
                              ],
                             [("actuariat_python [winpython]", None, dict(success_only=True)),
                                        "actuariat_python [anaconda3]", "actuariat_python [py35]"],
                             "actuariat_python [LONG]",
                             ["actuariat_python [LONG] [winpython]",
                                        "actuariat_python [LONG] [anaconda3]", "actuariat_python [LONG] [py35]"],
                             # code_beatrix
                             ("code_beatrix", "H H(4-5) * * 0"),
                             [("code_beatrix [winpython]", None, dict(success_only=True)),
                                        "code_beatrix [anaconda3]", "code_beatrix [py35]"],
                             # teachings
                             ("ensae_teaching_cs",
                                        "H H(5-6) * * 0"),   # 1.5h
                             # 1.5h
                             ("ensae_teaching_cs [winpython]", None, dict(
                                 success_only=True)),
                             "ensae_teaching_cs [anaconda3]",   # 1.5h
                             "ensae_teaching_cs [py35]",        # 1.5h
                             ["ensae_teaching_cs [SKIP]",        # 1h
                                        "ensae_teaching_cs [LONG]",        # 1h
                                        # 1h
                                        "ensae_teaching_cs [LONG] [winpython]",
                                        # 1h
                                        "ensae_teaching_cs [SKIP] [winpython]",
                                        # 1h
                                        "ensae_teaching_cs [LONG] [anaconda3]",
                                        # 1h
                                        "ensae_teaching_cs [SKIP] [anaconda3]",
                                        # 1h
                                        "ensae_teaching_cs [LONG] [py35]",
                                        # 1h
                                        "ensae_teaching_cs [SKIP] [py35]",
                              ],
                             # 3h
                             ("ensae_teaching_cs [custom_left]",
                                        "H H(10-11) * * 3"),
                             # 3h
                             "ensae_teaching_cs [winpython] [custom_left]",
                             # 3h
                             "ensae_teaching_cs [anaconda3] [custom_left]",
                             # 3h
                             "ensae_teaching_cs [py35] [custom_left]",
                             # documentation
                             ("pyquickhelper [doc]", "H H(3-4) * * 1"),
                             ["pymyinstall [doc]", "pysqllike [doc]", "pymmails [doc]",
                                        "pyrsslocal [doc]", "pyensae [doc]"],
                             ["actuariat_python [doc]", "code_beatrix [doc]"],
                             "ensae_teaching_cs [doc]",
                             # setup
                             ("pyquickhelper [setup]", "H H(6-7) * * 1"),
                             ["pymyinstall [setup]", "pysqllike [setup]", "pymmails [setup]",
                                        "pyrsslocal [setup]", "pyensae [setup]"],
                             ["actuariat_python [setup]",
                                 "code_beatrix [setup]"],
                             "ensae_teaching_cs [setup]",
                         ],
                         overwrite=False,
                         location=None,
                         no_dep=False,
                         prefix="",
                         fLOG=noLOG,
                         dependencies={'pymyinstall': ['pyquickhelper'],
                                       'pyensae': ['pyquickhelper'],
                                       'python3_module_template': ['pyquickhelper'],
                                       'ensae_teaching_cs': ['pyquickhelper', 'pyensae', 'pyrsslocal', 'pymmails'],
                                       'actuariat_python': ['pyquickhelper', 'pyensae', 'pyrsslocal', 'pymmails'],
                                       'code_beatrix': ['pyquickhelper', 'pyensae', 'pyrsslocal', 'pymmails'],
                                       }):
    """
    Set up many jobs on Jenkins

    @param      js                      (JenkinsExt) jenkins server (specially if you need credentials)
    @param      github                  github account if it does not start with *http://*,
                                        the link to git repository of the project otherwise
    @param      modules                 modules for which to generate the
    @param      get_jenkins_script      see `get_jenkins_script <http://www.xavierdupre.fr/app/pyquickhelper/helpsphinx/pyquickhelper/jenkinshelper/jenkins_server.html?highlight=get_jenkins_script#pyquickhelper.jenkinshelper.jenkins_server.JenkinsExt.get_jenkins_script>`_
                                        (default value if this parameter is None)
    @param      overwrite               do not create the job if it already exists
    @param      location                None for default or a local folder
    @param      no_dep                  if True, do not add dependencies
    @param      prefix                  add a prefix to the name
    @param      dependencies            some modules depend on others also being tested,
                                        this parameter gives the list
    @param      fLOG                    logging function
    @return                             list of created jobs

    *modules* is a list defined as follows:

        * each element can be a string or a tuple (string, schedule time) or a list
        * if it is a list, it contains a list of elements defined as previously
        * the job at position i is not scheduled, it will start after the last
          job at position i-1 whether or not it fails

    Example ::

         modules=[ # update anaconda
                    ("standalone [conda_update]", "H H(8-9) * * 0"),
                    "standalone [conda_update27]",
                    "standalone [local_pypi]",
                    # pyquickhelper and others,
                   ("pyquickhelper", "H H(10-11) * * 0"),
                    "pymyinstall",
                  ["pyquickhelper [anaconda3]", "pyquickhelper [winpython]",
                      "pyquickhelper [27] [anaconda2]"],
                  ["pyensae", ],
                  ["pymmails", "pysqllike", "pyrsslocal", "pymyinstall [27] [anaconda2]",
                   "python3_module_template", "pyensae [anaconda3]", "pyensae [winpython]"],
                  ["pymmails [anaconda3]", "pysqllike [anaconda3]", "pyrsslocal [anaconda3]",
                   "python3_module_template [anaconda3]", "python3_module_template [27] [anaconda2]",
                   "pymyinstall [LONG]"],
                  # actuariat
                  [("actuariat_python", "H H(12-13) * * 0")],
                  ["actuariat_python [winpython]",
                   "actuariat_python [anaconda3]"],
                  # code_beatrix
                  ("code_beatrix", "H H(14-15) * * 0"),
                  ["code_beatrix [winpython]",
                   "code_beatrix [anaconda3]"],
                  # teachings
                  ("ensae_teaching_cs", "H H(15-16) * * 0"),
                  ["ensae_teaching_cs [winpython]",
                   "ensae_teaching_cs [anaconda3]"],
                  "ensae_teaching_cs [notebooks]",
                  ["ensae_teaching_cs [winpython] [notebooks]",
                   "ensae_teaching_cs [anaconda3] [notebooks]", ],
                  ],
                  # documentation
                  ("pyquickhelper [doc]","H H(3-4) * * 1"),
                  ["pymyinstall [doc]", "pysqllike [doc]", "pymmails [doc]",
                  "pyrsslocal [doc]", "pyensae [doc]"],
                  ["actuariat_python [doc]", "code_beatrix [doc]"],
                  "ensae_teachings_cs [doc]",


    Example::

        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt

        js = JenkinsExt('http://machine:8080/', "user", "password")

        if True:
            js.setup_jenkins_server(github="sdpython",
                                modules=modules,
                                fLOG=print,
                                overwrite = True,
                                location = r"c:\\jenkins\\pymy")


    For WinPython, version 3.4.3+ is mandatory to get the latest version of IPython (3).

    Another example::

        import sys
        sys.path.append(r"C:\<path>\ensae_teaching_cs\src")
        sys.path.append(r"C:\<path>\pyquickhelper\src")
        sys.path.append(r"C:\<path>\pyensae\src")
        sys.path.append(r"C:\<path>\pyrsslocal\src")
        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt
        js = JenkinsExt("http://<machine>:8080/", <user>, <password>)
        setup_jenkins_server(js,
                location=r"c:\jenkins\pymy",
                overwrite=True,
                fLOG=print)
    """
    r = js.setup_jenkins_server(github=github,
                                modules=modules,
                                get_jenkins_script=None,
                                overwrite=overwrite,
                                location=location,
                                no_dep=no_dep,
                                prefix=prefix,
                                dependencies=dependencies)
    return r
