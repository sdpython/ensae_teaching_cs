"""
@file
@brief Set up a jenkins server with all the necessary job
"""
import re
import warnings
import os
from pyquickhelper.loghelper import noLOG


def engines_default():
    """
    returns a dictionary with default values for Jenkins server

    @return     dictionary

    ..warning::

        Virtual environment with conda must be created on the same disk
        as the original interpreter. The other scenario is not supported.
    """
    res = dict(anaconda2="d:\\Anaconda",
               anaconda3="d:\\Anaconda3",
               py35="c:\\Python35_x64",
               py34="c:\\Python34_x64",
               py27="c:\\Python27",
               default="c:\\Python35_x64",
               winpython="c:\\APythonENSAE\\python")
    res["Python27"] = res["py27"]
    res["Python34"] = res["py34"]
    res["Python35"] = res["py35"]
    res["Anaconda2"] = res["anaconda2"]
    res["Anaconda3"] = res["anaconda3"]
    res["WinPython35"] = res["winpython"]
    return res


def default_jenkins_jobs(filter=None, neg_filter=None, root=None):
    """
    default list of Jenkins jobs

    @param      filter          keep a subset of jobs (regular expression)
    @param      neg_filter      remove a subset of jobs (regular expression)
    @param      root            where to find yml project
    @return                     list

    It produces a subset of the following list of jobs:

    .. runpython::

        import textwrap
        from ensae_teaching_cs.automation.jenkins_helper import default_jenkins_jobs
        modules = default_jenkins_jobs()
        text = str(modules)
        print(textwrap.wrap(text))

    """
    yml = []
    if root is not None:
        yml_python3_module_template = os.path.join(
            root, "python3_module_template", ".local.jenkins.win.yml")
        yml.append(yml_python3_module_template)
    for c in yml:
        if not os.path.exists(c):
            warnings.warn("unable to find '{0}'".format(c))

    if filter is not None or neg_filter is not None:
        reg = re.compile(filter if filter else ".*")
        neg_reg = re.compile(neg_filter if neg_filter else ".*")
        res = default_jenkins_jobs()
        new_res = []
        for row in res:
            if isinstance(row, str):
                if reg.search(row) and not neg_reg.search(row):
                    new_res.append(row)
            elif isinstance(row, tuple):
                if reg.search(row[0]) and not neg_reg.search(row[0]):
                    new_res.append(row)
            elif isinstance(row, list):
                # list
                sub = []
                for item in row:
                    if isinstance(item, str):
                        if reg.search(item) and not neg_reg.search(item):
                            sub.append(item)
                    elif isinstance(item, tuple):
                        if reg.search(item[0]) and not neg_reg.search(item[0]):
                            sub.append(item)
                    else:
                        raise TypeError("{0} - {1}".format(item, type(item)))
                if len(sub) > 0:
                    new_res.append(sub)
            else:
                raise TypeError("{0} - {1}".format(row, type(row)))
        return new_res
    else:
        res = []
        res.extend(('yml', c, 'H H(0-1) * * %d' % (i % 7))
                   for i, c in enumerate(yml))
        res += [("standalone [conda_update] [anaconda3]",
                 "H H(0-1) * * 0"),
                "standalone [conda_update] [anaconda2] [27]",
                "standalone [local_pypi]",
                #"standalone [install]",
                #"standalone [update]",
                #"standalone [install] [py34]",
                #"standalone [update] [py34]",
                #"standalone [install] [winpython]",
                #"standalone [update] [winpython]",
                # pyquickhelper and others,
                ("pyquickhelper", "H H(2-3) * * 0"),
                ("pysqllike <-- pyquickhelper",
                    None, dict(success_only=True)),
                ["pymyinstall <-- pyquickhelper",
                 "pymmails <-- pyquickhelper"],
                "pyensae <-- pyquickhelper, pymyinstall",
                "pyrsslocal <-- pyquickhelper, pyensae",
                # Python 27
                ("pyquickhelper [py27] [27]", "H H(2-3) * * 1"),
                ["pymyinstall [py27] [27] <-- pyquickhelper"],
                # WinPython
                ("pyquickhelper [winpython]", "H H(5-6) * * 1"),
                ["pysqllike [winpython] <-- pyquickhelper",
                    "pymmails [winpython] <-- pyquickhelper",
                    "pymyinstall [winpython] <-- pyquickhelper"],
                "pyensae [winpython] <-- pyquickhelper, pymyinstall",
                "pyrsslocal [winpython] <-- pyquickhelper, pyensae",
                # Anaconda 3
                ("pyquickhelper [anaconda3]", "H H(2-3) * * 1"),
                ["pysqllike [anaconda3] <-- pyquickhelper",
                    "pymmails [anaconda3] <-- pyquickhelper",
                    "pymyinstall [anaconda3] <-- pyquickhelper"],
                "pyensae [anaconda3] <-- pyquickhelper, pymyinstall",
                "pyrsslocal [anaconda3] <-- pyquickhelper, pyensae",
                # Anaconda 2
                ("pyquickhelper [anaconda2] [27]", "H H(2-3) * * 1"),
                ["pymyinstall [anaconda2] [27] <-- pyquickhelper"],
                # update
                ("pymyinstall [update_modules]", "H H(0-1) * * 5"),
                "pymyinstall [update_modules] [winpython]",
                "pymyinstall [update_modules] [py34]",
                "pymyinstall [update_modules] [py27]",
                "pymyinstall [update_modules] [anaconda2]",
                "pymyinstall [update_modules] [anaconda3]",
                # py35
                ("pyquickhelper [py34]", "H H(2-3) * * 2"),
                ["pysqllike [py34] <-- pyquickhelper",
                    "pymmails [py34] <-- pyquickhelper",
                    "pymyinstall [py34] <-- pyquickhelper"],
                "pyensae [py34] <-- pyquickhelper, pymyinstall",
                "pyrsslocal [py34] <-- pyquickhelper, pyensae",
                # actuariat
                ("actuariat_python <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
                [("actuariat_python [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", None, dict(success_only=True)),
                    "actuariat_python [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                    "actuariat_python [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                # code_beatrix
                ("code_beatrix <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 0"),
                ("code_beatrix [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(success_only=True)),
                ["code_beatrix [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                    "code_beatrix [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                # jupytalk
                ("jupytalk <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "H H(4-5) * * 1"),
                ("jupytalk [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(success_only=True)),
                ["jupytalk [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                    "jupytalk [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                # mlstatpy
                ("mlstatpy <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "H H(4-5) * * 2"),
                ("mlstatpy [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(success_only=True)),
                ["mlstatpy [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                    "mlstatpy [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                # teachings
                # 1.5h
                ("ensae_teaching_cs <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(5-6) * * 0"),
                ("ensae_teaching_cs [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(success_only=True)),
                # 1.5h
                ["ensae_teaching_cs [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "ensae_teaching_cs [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
                # ensae_projects
                ("ensae_projects <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall", "H H(4-5) * * 3"),
                ("ensae_projects [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(success_only=True)),
                ["ensae_projects [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "ensae_projects [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
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
                ["mlstatpy [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "jupytalk [doc] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall"],
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
                # LONG
                ("pymyinstall [LONG] <-- pyquickhelper",
                 "H(0,30) 02 01 * *"),
                "pymyinstall [LONG] [py34] <-- pyquickhelper",
                "mlstatpy [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                "mlstatpy [LONG] [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                "mlstatpy [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                "mlstatpy [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                ("actuariat_python [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("actuariat_python [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("actuariat_python [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("actuariat_python [LONG] [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [LONG] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [LONG] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [LONG] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [LONG] [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                # SKIP
                ("ensae_projects [SKIP] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "H(0,30) 05 01 * *", dict(timeout=4800)),
                ("ensae_projects [SKIP] [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [SKIP] [anaconda3] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [SKIP] [py34] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [SKIP] [winpython] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [SKIP] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                # LEFT
                # 3h
                ("ensae_teaching_cs [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 "H(0,30) 02 10 * *", dict(timeout=4800)),
                ("ensae_teaching_cs [winpython] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [anaconda3] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ("ensae_teaching_cs [py34] [custom_left] <-- pyquickhelper, pyensae, pymmails, pyrsslocal, pymyinstall",
                 None, dict(timeout=4800)),
                ]
        return res


def setup_jenkins_server(js,
                         github="sdpython",
                         modules=default_jenkins_jobs(),
                         overwrite=False,
                         location=None,
                         prefix="",
                         fLOG=noLOG):
    """
    Set up many jobs on Jenkins

    @param      js                      (JenkinsExt) jenkins server (specially if you need credentials)
    @param      github                  github account if it does not start with *http://*,
                                        the link to git repository of the project otherwise
    @param      modules                 modules for which to generate the Jenkins job (see @see fn default_jenkins_jobs)
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

    Example::

        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt

        js = JenkinsExt('http://machine:8080/', "user", "password")

        if True:
            js.setup_jenkins_server(github="sdpython",
                                modules=modules,
                                fLOG=print,
                                overwrite = True,
                                location = r"d:\\jenkins\\pymy")


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
