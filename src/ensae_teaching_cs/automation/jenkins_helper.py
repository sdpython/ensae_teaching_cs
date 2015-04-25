"""
@file
@brief Set up a jenkins server with all the necessary job
"""
import os
import sys

from pyquickhelper import noLOG
from pyquickhelper.jenkinshelper.jenkins_server import JenkinsExt, jenkins


def get_jenkins_job_name(job):
    """
    infer a name for the jenkins job

    @param      job     str
    @return             name
    """
    return job.replace(" ", "_").replace("[", "").replace("]", "")


def get_jenkins_script(job, pythonexe, winpython, anaconda, anaconda2):
    """
    build the jenkins script for a module and its options

    @param      job             module and options
    @param      pythonexe       unused
    @param      anaconda        location of anaconda
    @param      anaconda2       location of anaconda 2
    @param      winpython       location of winpython
    @return                     script
    """
    spl = job.split()
    if len(spl) == 1:
        return "build_setup_help_on_windows.bat"
    elif len(spl) == 0:
        raise ValueError("job is empty")

    elif len(spl) in [2, 3]:

        if "[all]" in spl:
            cmd = "bunittest_all.bat"
        elif "[notebooks]" in spl:
            cmd = "bunittest_notebooks.bat"
        elif "[update]" in spl:
            cmd = "update_anaconda.bat"
        elif "[update27]" in spl:
            cmd = "update_anaconda_27.bat"
        elif "[27]" in spl:
            cmd = "build_setup_help_on_windows_27.bat"
        else:
            cmd = "build_setup_help_on_windows.bat"

        if "[anaconda]" in spl:
            if anaconda is not None:
                cmd += " " + os.path.join(anaconda, "python")
        elif "[anaconda2]" in spl:
            if anaconda2 is not None:
                cmd += " " + os.path.join(anaconda2, "python")
        elif "[winpython]" in spl:
            if winpython is not None:
                cmd += " " + os.path.join(winpython, "python")

        return cmd

    else:
        raise ValueError("unable to interpret: " + job)


def setup_jenkins_server(js_url,
                         github="sdpython",
                         modules=["pyquickhelper",
                                  ["pymyinstall", ],
                                  ["pymyinstall [anaconda] [update]",
                                      "pymyinstall [anaconda2] [update27]"],
                                  ["pyquickhelper [anaconda]", "pyquickhelper [winpython]",
                                      "pyquickhelper [27] [anaconda2]"],
                                  ["pyensae", ],
                                  ["pymmails", "pysqllike", "pyrsslocal", "pymyinstall [27] [anaconda2]",
                                   "python3_module_template", "pyensae [anaconda]", "pyensae [winpython]"],
                                  ["pymmails [anaconda]", "pysqllike [anaconda]", "pyrsslocal [anaconda]",
                                   "python3_module_template [anaconda]"],
                                  ["actuariat_python",
                                      "python3_module_template [27] [anaconda]"],
                                  ["actuariat_python [winpython]",
                                   "actuariat_python [anaconda]"],
                                  "code_beatrix",
                                  ["code_beatrix [winpython]",
                                   "code_beatrix [anaconda]"],
                                  "ensae_teaching_cs",
                                  ["ensae_teaching_cs [winpython]",
                                   "ensae_teaching_cs [anaconda]"],
                                  "ensae_teaching_cs [notebooks]",
                                  ["ensae_teaching_cs [winpython] [notebooks]",
                                   "ensae_teaching_cs [anaconda] [notebooks]", "pymyinstall [all]"],
                                  ],
                         pythonexe=os.path.dirname(sys.executable),
                         winpython=r"C:\WinPython-64bit-3.4.3.2FlavorRfull\python-3.4.3.amd64",
                         anaconda=r"c:\Anaconda3",
                         anaconda2=r"c:\Anaconda2",
                         overwrite=False,
                         location=None,
                         no_dep=False,
                         prefix="",
                         fLOG=noLOG,
                         dependencies={'pymyinstall': ['pyquickhelper'],
                                       'pyensae': ['pyquickhelper'],
                                       'ensae_teaching_cs': ['pyquickhelper', 'pyensae', 'pyrsslocal', 'pymmails']
                                       }):
    """
    Set up all the jobs to build these teachings

    @param      js_url          url or jenkins server (specially if you need credentials)
    @param      github          github account
    @param      modules         modules for which to generate the
    @param      pythonexe       location of Python (unused)
    @param      winpython       location of WinPython (or None to skip)
    @param      anaconda        location of Anaconda (or None to skip)
    @param      overwrite       do not create the job if it already exists
    @param      location        None for default or a local folder
    @param      no_dep          if True, do not add dependencies
    @param      prefix          add a prefix to the name
    @param      dependencies    some modules depend on others also being tested,
                                this parameter gives the list
    @param      fLOG            logging function
    @return                     list of created jobs

    Example::

        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt

        js = JenkinsExt('http://machine:8080/', "user", "password")

        if True:
            setup_jenkins_server(   js,
                                anaconda=r"C:\\Anaconda3",
                                anaconda2=r"C:\\Anaconda2",
                                winpython=r"C:\WinPython-64bit-3.4.3.2FlavorRfull\python-3.4.3.amd64",
                                fLOG=print,
                                overwrite = True,
                                location = r"c:\\jenkins\\pymy")

        if True:
            setup_jenkins_server(js,
                                anaconda=r"C:\\Anaconda3",
                                anaconda2=r"C:\\Anaconda2",
                                winpython=r"C:\WinPython-64bit-3.4.3.2FlavorRfull\python-3.4.3.amd64",
                                fLOG=print,
                                overwrite = True,
                                location = r"c:\\jenkins\\pymy_nodep",
                                no_dep=True,
                                prefix = "_nodep_")

    For WinPython, version 3.4.3+ is mandatory to get the latest version of IPython (3).

    Another example::

        import sys
        sys.path.append(r"C:\<path>\ensae_teaching_cs\src")
        sys.path.append(r"C:\<path>\pyquickhelper\src")
        sys.path.append(r"C:\<path>\pyensae\src")
        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt
        js = JenkinsExt("http://<machine>:8080/", <user>, <password>)
        setup_jenkins_server(js,
                location=r"c:\jenkins\pymy",
                overwrite=True,
                fLOG=print)
    """

    if isinstance(js_url, str):
        js = JenkinsExt(js_url)
    else:
        js = js_url

    if "https://" not in github:
        github = "https://github.com/" + github + "/"

    dep = []
    created = []
    locations = []
    for jobs in modules:

        if not isinstance(jobs, list):
            jobs = [jobs]

        new_dep = []
        for job in jobs:
            mod = job.split()[0]
            name = get_jenkins_job_name(job)
            jname = prefix + name

            try:
                j = js.get_job_config(jname) if not js._mock else None
            except jenkins.NotFoundException:
                j = None

            if overwrite or j is None:

                if j is not None:
                    fLOG("delete job", jname)
                    js.delete_job(jname)

                script = get_jenkins_script(
                    job, pythonexe, winpython, anaconda, anaconda2)
                if script is not None:
                    new_dep.append(name)
                    created.append(name)
                    fLOG("create job", jname)
                    loc = None if location is None else os.path.join(
                        location, jname)

                    deps = get_dependencies_path(
                        job, locations, dependencies.get(mod, None))

                    js.create_job_template(jname,
                                           git_repo=github + "%s/" % mod,
                                           upstreams=[] if no_dep else dep[-1:],
                                           script=script,
                                           location=loc,
                                           dependencies=deps)

                    locations.append((job, loc))
                else:
                    loc = None if location is None else os.path.join(
                        location, jname)
                    locations.append((job, loc))
                    fLOG("skipping", job, "location", loc)
            elif j is not None:
                new_dep.append(name)

        dep = new_dep

    return created


def get_dependencies_path(job, locations, dependencies):
    """
    return the depeencies to add to the job based on the name and the past locations

    @param      job             job description
    @param      locations       list of 2-uple ( job description, location )
    @param      dependencies    None or list of dependencies
    @return                     dictionary { module, location }
    """
    if dependencies is None:
        return {}

    py27 = "[27]" in job
    name = job.split()[0]

    res = {}
    for dep in dependencies:
        for j, loc in locations:
            n = j.split()[0]
            p27 = "[27]" in j

            if n == dep and p27 == py27:
                if p27:
                    res[dep] = os.path.join(loc, "src")
                else:
                    res[dep] = os.path.join(loc, "dist_module27", "src")
                break

    if len(dependencies) != len(res):
        raise Exception("lower number of dependencies, requested:\n{0}\nFOUND:\n{1}\nLOCATIONS:\n{2}".format(", ".join(dependencies),
                                                                                                             "\n".join(
                                                                                                                 "{0} : {1}".format(k, v) for k, v in sorted(res.items())),
                                                                                                             "\n".join("{0} : {1}".format(k, v) for k, v in locations)))

    return res
