"""
@file
@brief Set up a jenkins server with all the necessary job
"""
import os
import re
import sys
from pyquickhelper.loghelper import noLOG
from pyquickhelper.jenkinshelper import setup_jenkins_server_yml
from .teaching_modules import get_teaching_modules


def get_interpreter(platform=None):
    """
    Returns the default interpreter.

    @param      plaftorm        platform
    """
    if platform == sys.platform:
        return os.path.dirname(sys.executable)
    elif platform.startswith("win"):
        return "c:\\Python%d%d%d_x64" % sys.version_info[:3]
    else:
        return "/usr/local/bin"


def engines_default(prefix="c:\\", prefix_python="c:\\", prefix_conda="c:\\", platform=None):
    """
    Returns a dictionary with default values for a :epkg:`Jenkins` server.

    @param      prefix          prefix for Jenkins location
    @param      prefix_python   prefix for Python distribution
    @param      prefix_conda    prefix for Anaconda or Miniconda distribution
    @param      platform        platform to use
    @return     dictionary

    .. warning::

        Virtual environment with conda must be created on the same disk
        as the original interpreter. The other scenario is not supported.
    """
    if platform is None:
        platform = sys.platform
    if platform.startswith("win"):
        res = dict(anaconda2=os.path.join(prefix_conda, "Anaconda2"),
                   anaconda3=os.path.join(prefix_conda, "Anaconda3"),
                   default=get_interpreter(platform=platform),
                   py37=get_interpreter(platform=platform),
                   py36=os.path.join(prefix_python, "Python36_x64"),
                   py27=os.path.join(prefix_python, "Python27_x64"),
                   winpython36=os.path.join(
                       prefix_python, "WinPython36_x64", "python-3.6.3.amd64"),
                   Python37pyq=os.path.join(
                       prefix, "jenkins", "venv", "py37", "pyq", "Scripts"),
                   Python36pyq=os.path.join(prefix, "jenkins", "venv", "py36", "pyq", "Scripts"))
        res["Python27"] = res["py27"]
        res["Python36"] = res["py36"]
        res["Python37"] = res["py37"]
        res["Anaconda2"] = res["anaconda2"]
        res["Anaconda3"] = res["anaconda3"]
        res["WinPython36"] = res["winpython36"]
        return res
    else:
        key = "Python%d%d" % sys.version_info[:2]
        res = {key: get_interpreter(platform=platform)}
        res["py%d%d" % sys.version_info[:2]] = res[key]
        return res


def default_jenkins_jobs(filter=None, neg_filter=None, root=None, platform=None):
    """
    Default list of :epkg:`Jenkins` jobs.

    @param      filter          keep a subset of jobs (regular expression)
    @param      neg_filter      remove a subset of jobs (regular expression)
    @param      root            where to find yml project
    @param      platform        platform or None for the current one
    @return                     list

    It produces a subset of the following list of jobs:

    .. runpython::

        from ensae_teaching_cs.automation.jenkins_helper import default_jenkins_jobs
        modules = default_jenkins_jobs()
        text = [str(m) for m in modules]
        print("\\n".join(text))

    """
    if platform is None:
        platform = sys.platform
    plat = "win" if platform.startswith("win") else "lin"
    yml = []
    pattern = "https://raw.githubusercontent.com/sdpython/%s/master/.local.jenkins.{0}.yml".format(
        plat)
    modules = ["_automation"] + get_teaching_modules()
    for c in modules:
        yml.append(pattern % c)

    if filter is not None or neg_filter is not None:
        reg = re.compile(filter if filter else ".*")
        neg_reg = re.compile(neg_filter if neg_filter else "^$")
        res = default_jenkins_jobs(platform=platform)
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
        res += ["standalone [local_pypi] [py%d%d]" % sys.version_info[:2],
                ("pymyinstall [update_modules] [py%d%d]" % sys.version_info[:2],
                 "H H(0-1) * * 5")]
        return res


def setup_jenkins_server(js, github="sdpython", modules=None,
                         overwrite=False, location=None, prefix="",
                         delete_first=False, disable_schedule=False,
                         fLOG=noLOG):
    """
    Sets up many jobs on :epkg:`Jenkins`.

    @param      js                      (JenkinsExt) jenkins server (specially if you need credentials)
    @param      github                  github account if it does not start with *http://*,
                                        the link to git repository of the project otherwise
    @param      modules                 modules for which to generate the :epkg:`Jenkins` job
                                        (see @see fn default_jenkins_jobs which provides the default value
                                        if *modules* is None)
    @param      overwrite               do not create the job if it already exists
    @param      location                None for default or a local folder
    @param      prefix                  add a prefix to the name
    @param      delete_first            remove all jobs first
    @param      disable_schedule        disable schedule for all jobs
    @param      platform                platform or None for the current one
    @param      fLOG                    logging function
    @return                             list of created jobs

    *modules* is a list defined as follows:

    * each element can be a string or a tuple (string, schedule time) or a list
    * if it is a list, it contains a list of elements defined as previously
    * the job at position i is not scheduled, it will start after the last
      job at position i-1 whether or not it fails
    """
    platform = js.platform
    if modules is None:
        modules = default_jenkins_jobs(platform=platform)
    r = setup_jenkins_server_yml(js, github=github, modules=modules, get_jenkins_script=None,
                                 overwrite=overwrite, location=location, prefix=prefix,
                                 delete_first=delete_first, disable_schedule=disable_schedule)
    return r
