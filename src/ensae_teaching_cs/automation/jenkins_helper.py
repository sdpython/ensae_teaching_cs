"""
@file
@brief Set up a jenkins server with all the necessary job
"""
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
                             ("pysqllike <-- pyquickhelper",
                                        None, dict(success_only=True)),
                             ["python3_module_template <-- pyquickhelper",
                                 "pyquickhelper [27] [anaconda2]"],
                             ["pyquickhelper [winpython]",
                                 "python3_module_template [27] [anaconda2] <-- pyquickhelper", ],
                             "pymyinstall <-- pyquickhelper",
                             "pyensae <-- pyquickhelper, pymyinstall",
                             ["pymmails <-- pyquickhelper",
                                 "pyrsslocal <-- pyquickhelper, pyensae"],
                             ["pymyinstall [27] [anaconda2] <-- pyquickhelper",
                                 "pymyinstall [LONG] <-- pyquickhelper"],
                             # update, do not move, it depends on pyquickhelper
                             ("pyquickhelper [anaconda3]", "H H(2-3) * * 1"),
                             ["pyquickhelper [winpython]", "pysqllike [anaconda3] <-- pyquickhelper",
                                        "pysqllike [winpython] <-- pyquickhelper",
                                        "python3_module_template [anaconda3] <-- pyquickhelper",
                                        "python3_module_template [winpython] <-- pyquickhelper",
                                        "pymmails [anaconda3] <-- pyquickhelper",
                                        "pymmails [winpython] <-- pyquickhelper",
                                        "pymyinstall [anaconda3] <-- pyquickhelper",
                                        "pymyinstall [winpython] <-- pyquickhelper"],
                             ["pyensae [anaconda3] <-- pyquickhelper, pymyinstall",
                                        "pyensae [winpython] <-- pyquickhelper, pymyinstall",
                                        "pyrsslocal [anaconda3] <-- pyquickhelper, pyensae",
                                        "pyrsslocal [winpython] <-- pyquickhelper"],
                             ("pymyinstall [update_modules]",
                                        "H H(0-1) * * 5"),
                             "pymyinstall [update_modules] [winpython]",
                             "pymyinstall [update_modules] [py35]",
                             "pymyinstall [update_modules] [anaconda2]",
                             "pymyinstall [update_modules] [anaconda3]",
                             # py35
                             ("pyquickhelper [py35]", "H H(2-3) * * 2"),
                             ["pysqllike [py35] <-- pyquickhelper",
                                        "pymmails [py35] <-- pyquickhelper",
                                        "python3_module_template [py35] <-- pyquickhelper",
                                        "pymyinstall [py35] <-- pyquickhelper"],
                             "pyensae [py35] <-- pyquickhelper, pymyinstall",
                             "pyrsslocal [py35] <-- pyquickhelper, pyensae",
                             # actuariat
                             ("actuariat_python <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
                             [("actuariat_python [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", None, dict(success_only=True)),
                                        "actuariat_python [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "actuariat_python [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             "actuariat_python [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             ["actuariat_python [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "actuariat_python [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "actuariat_python [LONG] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             # code_beatrix
                             ("code_beatrix <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
                             ("code_beatrix [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        None, dict(success_only=True)),
                             ["code_beatrix [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "code_beatrix [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             # teachings
                             # 1.5h
                             ("ensae_teaching_cs <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(5-6) * * 0"),
                             # 1.5h
                             ["ensae_teaching_cs [SKIP] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                 "ensae_teaching_cs [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],  # 1h ish
                             ["ensae_teaching_cs [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        # 1.5h
                                        "ensae_teaching_cs [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "ensae_teaching_cs [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             "ensae_teaching_cs [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             "ensae_teaching_cs [SKIP] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             "ensae_teaching_cs [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             "ensae_teaching_cs [SKIP] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             "ensae_teaching_cs [LONG] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             "ensae_teaching_cs [SKIP] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             # 3h
                             ("ensae_teaching_cs [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "H H(10-11) * * 3"),
                             # 3h
                             "ensae_teaching_cs [winpython] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             # 3h
                             "ensae_teaching_cs [anaconda3] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             # 3h
                             "ensae_teaching_cs [py35] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             # code_beatrix
                             ("ensae_projects <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall, actuariat_python, ensae_teaching_cs, code_beatrix", "H H(4-5) * * 3"),
                             ("ensae_projects [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall, actuariat_python, ensae_teaching_cs, code_beatrix",
                                        None, dict(success_only=True)),
                             ["ensae_projects [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall, actuariat_python, ensae_teaching_cs, code_beatrix",
                                        "ensae_projects [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall, actuariat_python, ensae_teaching_cs, code_beatrix"],
                             # documentation
                             ("pyquickhelper [doc] <-- pyquickhelper",
                                        "H H(3-4) * * 1"),
                             ["pymyinstall [doc] <-- pyquickhelper",
                                        "pysqllike [doc] <-- pyquickhelper",
                                        "pymmails [doc] <-- pyquickhelper",
                                        "pyrsslocal [doc] <-- pyquickhelper",
                                        "pyensae [doc] <-- pyquickhelper"],
                             ["actuariat_python [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                        "code_beatrix [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             "ensae_teaching_cs [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                             # setup
                             ("pyquickhelper [setup] <-- pyquickhelper",
                                        "H H(6-7) * * 1"),
                             ["pymyinstall [setup] <-- pyquickhelper",
                                        "pysqllike [setup] <-- pyquickhelper",
                                        "pymmails [setup] <-- pyquickhelper",
                                        "pyrsslocal [setup] <-- pyquickhelper, pyensae",
                                        "pyensae [setup] <-- pyquickhelper"],
                             ["actuariat_python [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                                 "code_beatrix [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                             "ensae_teaching_cs [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                         ],
                         overwrite=False,
                         location=None,
                         prefix="",
                         fLOG=noLOG):
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
    @param      prefix                  add a prefix to the name
    @param      fLOG                    logging function
    @return                             list of created jobs

    *modules* is a list defined as follows:

        * each element can be a string or a tuple (string, schedule time) or a list
        * if it is a list, it contains a list of elements defined as previously
        * the job at position i is not scheduled, it will start after the last
          job at position i-1 whether or not it fails

    Example ::

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
             ("pysqllike <-- pyquickhelper", None, dict(success_only=True)),
             ["python3_module_template <-- pyquickhelper",
                 "pyquickhelper [27] [anaconda2]"],
             ["pyquickhelper [winpython]",
                 "python3_module_template [27] [anaconda2] <-- pyquickhelper", ],
             ["pymyinstall <-- pyquickhelper", "pyensae <-- pyquickhelper"],
             ["pymmails <-- pyquickhelper", "pyrsslocal <-- pyquickhelper, pyensae"],
             ["pymyinstall [27] [anaconda2] <-- pyquickhelper", "pymyinstall [LONG] <-- pyquickhelper"],
             # update, do not move, it depends on pyquickhelper
             ("pyquickhelper [anaconda3]", "H H(2-3) * * 1"),
             ["pyquickhelper [winpython]", "pysqllike [anaconda3]",
                        "pysqllike [winpython] <-- pyquickhelper",
                        "python3_module_template [anaconda3] <-- pyquickhelper",
                        "python3_module_template [winpython] <-- pyquickhelper",
                        "pymmails [anaconda3] <-- pyquickhelper",
                        "pymmails [winpython] <-- pyquickhelper",
                        "pymyinstall [anaconda3] <-- pyquickhelper",
                        "pymyinstall [winpython] <-- pyquickhelper"],
             ["pyensae [anaconda3] <-- pyquickhelper",
                        "pyensae [winpython] <-- pyquickhelper",
                        "pyrsslocal [anaconda3] <-- pyquickhelper, pyensae",
                        "pyrsslocal [winpython] <-- pyquickhelper"],
             ("pymyinstall [update_modules]",
                        "H H(0-1) * * 5"),
             "pymyinstall [update_modules] [winpython]",
             "pymyinstall [update_modules] [py35]",
             "pymyinstall [update_modules] [anaconda2]",
             "pymyinstall [update_modules] [anaconda3]",
             # py35
             ("pyquickhelper [py35]", "H H(2-3) * * 2"),
             ["pysqllike [py35]",
                        "pymmails [py35] <-- pyquickhelper",
                        "python3_module_template [py35] <-- pyquickhelper",
                        "pymyinstall [py35] <-- pyquickhelper"],
             "pyensae [py35] <-- pyquickhelper",
             "pyrsslocal [py35] <-- pyquickhelper, pyensae",
             # actuariat
             ("actuariat_python <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
             [("actuariat_python [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", None, dict(success_only=True)),
                        "actuariat_python [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        "actuariat_python [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             "actuariat_python [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             ["actuariat_python [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        "actuariat_python [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        "actuariat_python [LONG] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             # code_beatrix
             ("code_beatrix <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
             ("code_beatrix [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        None, dict(success_only=True)),
             ["code_beatrix [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
              "code_beatrix [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             # teachings
             ("ensae_teaching_cs <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(5-6) * * 0"),   # 1.5h
             # 1.5h
             ["ensae_teaching_cs [SKIP] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "ensae_teaching_cs [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],  # 1h ish
             ["ensae_teaching_cs [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        # 1.5h
                        "ensae_teaching_cs [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        "ensae_teaching_cs [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             "ensae_teaching_cs [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             "ensae_teaching_cs [SKIP] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             "ensae_teaching_cs [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             "ensae_teaching_cs [SKIP] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             "ensae_teaching_cs [LONG] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             "ensae_teaching_cs [SKIP] [py35] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             # 3h
             ("ensae_teaching_cs [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                        "H H(10-11) * * 3"),
             # 3h
             "ensae_teaching_cs [winpython] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             # 3h
             "ensae_teaching_cs [anaconda3] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             # 3h
             "ensae_teaching_cs [py35] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             # documentation
             ("pyquickhelper [doc] <-- pyquickhelper", "H H(3-4) * * 1"),
             ["pymyinstall [doc]",
                        "pysqllike [doc] <-- pyquickhelper",
                        "pymmails [doc] <-- pyquickhelper",
                        "pyrsslocal [doc] <-- pyquickhelper",
                        "pyensae [doc] <-- pyquickhelper"],
             ["actuariat_python [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
              "code_beatrix [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             "ensae_teaching_cs [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
             # setup
             ("pyquickhelper [setup] <-- pyquickhelper", "H H(6-7) * * 1"),
             ["pymyinstall [setup]",
                        "pysqllike [setup] <-- pyquickhelper",
                        "pymmails [setup] <-- pyquickhelper",
                        "pyrsslocal [setup] <-- pyquickhelper, pyensae",
                        "pyensae [setup] <-- pyquickhelper"],
             ["actuariat_python [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "code_beatrix [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
             "ensae_teaching_cs [setup] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
         ],


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
        sys.path.append(r"C:\\<path>\\ensae_teaching_cs\\src")
        sys.path.append(r"C:\\<path>\\pyquickhelper\\src")
        sys.path.append(r"C:\\<path>\\pyensae\\src")
        sys.path.append(r"C:\\<path>\\pyrsslocal\\src")
        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt
        js = JenkinsExt("http://<machine>:8080/", <user>, <password>)
        setup_jenkins_server(js,
                location=r"c:\\jenkins\\pymy",
                overwrite=True,
                fLOG=print)
    """
    r = js.setup_jenkins_server(github=github,
                                modules=modules,
                                get_jenkins_script=None,
                                overwrite=overwrite,
                                location=location,
                                prefix=prefix)
    return r
