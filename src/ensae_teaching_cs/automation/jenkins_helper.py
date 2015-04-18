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
                                  ["pymyinstall [anaconda] [update]","pymyinstall [anaconda2] [update27]"],
                                  ["pyquickhelper [anaconda]", "pyquickhelper [27] [anaconda2]"],
                                  ["pyensae","pymyinstall [all]"],
                                  ["pymmails", "pysqllike", "pyrsslocal", "pymyinstall [27] [anaconda2]",
                                   "python3_module_template", "pyensae [anaconda]"],
                                  ["pymmails [anaconda]", "pysqllike [anaconda]", "pyrsslocal [anaconda]",
                                   "python3_module_template [anaconda]"],
                                  ["actuariat_python", "python3_module_template [27] [anaconda]"],
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
                                   "ensae_teaching_cs [anaconda] [notebooks]"],
                                  ],
                         pythonexe=os.path.dirname(sys.executable),
                         winpython=r"C:\WinPython-64bit-3.4.2.4FlavorRfull\python-3.4.2.amd64",
                         anaconda=r"c:\Anaconda3",
                         anaconda2=r"c:\Anaconda2",
                         overwrite=False,
                         location=None,
                         no_dep=False,
                         prefix="",
                         fLOG=noLOG):
    """
    Set up all the jobs to build these teachings

    @param      js_url      url or jenkins server (specially if you need credentials)
    @param      github      github account
    @param      modules     modules for which to generate the
    @param      pythonexe   location of Python (unused)
    @param      winpython   location of WinPython (or None to skip)
    @param      anaconda    location of Anaconda (or None to skip)
    @param      overwrite   do not create the job if it already exists
    @param      location    None for default or a local folder
    @param      no_dep      if True, do not add dependencies
    @param      prefix      add a prefix to the name
    @param      fLOG        logging function
    @return                 list of created jobs

    Example::

        from ensae_teaching_cs.automation.jenkins_helper import setup_jenkins_server, JenkinsExt

        js = JenkinsExt('http://machine:8080/', "user", "password")

        if True:
            setup_jenkins_server(   js,
                                anaconda=r"C:\\Anaconda3",
                                winpython=r"C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                                fLOG=print,
                                overwrite = True,
                                location = r"c:\\jenkins\\pymy")

        if True:
            setup_jenkins_server(js,
                                anaconda=r"C:\\Anaconda3",
                                winpython=r"C:\\WinPython-64bit-3.4.2.3\\python-3.4.2.amd64",
                                fLOG=print,
                                overwrite = True,
                                location = r"c:\\jenkins\\pymy_nodep",
                                no_dep=True,
                                prefix = "_nodep_")
    """

    if isinstance(js_url, str):
        js = JenkinsExt(js_url)
    else:
        js = js_url

    if "https://" not in github:
        github = "https://github.com/" + github + "/"

    dep = []
    created = []
    for jobs in modules:

        if not isinstance(jobs, list):
            jobs = [jobs]

        new_dep = []
        for job in jobs:
            mod = job.split()[0]
            name = get_jenkins_job_name(job)
            jname = prefix + name

            try:
                j = js.get_job_config(jname)
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
                    js.create_job_template(jname,
                                           git_repo=github + "%s/" % mod,
                                           upstreams=[] if no_dep else dep[-1:],
                                           script=script,
                                           location=loc)
            elif j is not None:
                new_dep.append(name)

        dep = new_dep

    return created
