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


def find_python(pattern="Python[0-9]{3}_x64", root="/"):
    """
    Finds a path containing :epkg:`Python` from the root.
    Takes the highest one.

    @param      pattern     pattern to find
    @param      root        folder when to look for Python
    @return                 path found
    """
    if sys.platform.startswith("win"):
        root = root.replace("/", "\\")
    reg = re.compile(pattern)
    possible = os.listdir(root)
    possible.sort(reverse=True)
    for pos in possible:
        if reg.search(pos):
            return os.path.join(root, pos)
    raise FileNotFoundError(
        "Unable to find a path with the regular expression '{0}'".format(pattern))


def engines_default(prefix="c:\\", prefix_python="c:\\", prefix_conda="c:\\"):
    """
    Returns a dictionary with default values for a :epkg:`Jenkins` server.

    @param      prefix          prefix for Jenkins location
    @param      prefix_python   prefix for Python distribution
    @param      prefix_conda    prefix for Anaconda or Miniconda distribution
    @return     dictionary

    .. warning::

        Virtual environment with conda must be created on the same disk
        as the original interpreter. The other scenario is not supported.
    """
    res = dict(anaconda2=os.path.join(prefix_conda, "Anaconda2"),
               anaconda3=os.path.join(prefix_conda, "Anaconda3"),
               py37=os.path.join(prefix_python, find_python()),
               py36=os.path.join(prefix_python, "Python36_x64"),
               py27=os.path.join(prefix_python, "Python27_x64"),
               default=os.path.join(prefix_python, find_python()),
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


def default_jenkins_jobs(filter=None, neg_filter=None, root=None):
    """
    Default list of :epkg:`Jenkins` jobs.

    @param      filter          keep a subset of jobs (regular expression)
    @param      neg_filter      remove a subset of jobs (regular expression)
    @param      root            where to find yml project
    @return                     list

    It produces a subset of the following list of jobs:

    .. runpython::

        from ensae_teaching_cs.automation.jenkins_helper import default_jenkins_jobs
        modules = default_jenkins_jobs()
        text = [str(m) for m in modules]
        print("\\n".join(text))

    """
    plat = "win" if sys.platform.startswith("win") else "lin"
    yml = []
    pattern = "https://raw.githubusercontent.com/sdpython/%s/master/.local.jenkins.{0}.yml".format(plat)
    modules = ["_automation"] + get_teaching_modules()
    for c in modules:
        yml.append(pattern % c)

    if filter is not None or neg_filter is not None:
        reg = re.compile(filter if filter else ".*")
        neg_reg = re.compile(neg_filter if neg_filter else "^$")
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
        res += [("standalone [conda_update] [anaconda3]", "H H(0-1) * * 0"),
                "standalone [conda_update] [anaconda2] [27]",
                "standalone [local_pypi]",
                # update
                ("pymyinstall [update_modules] [py37]", "H H(0-1) * * 5"),
                "pymyinstall [update_modules] [py36]",
                "pymyinstall [update_modules] [anaconda3]",
                ]
        return res


def setup_jenkins_server(js, github="sdpython", modules=None,
                         overwrite=False, location=None, prefix="",
                         delete_first=False, disable_schedule=False, fLOG=noLOG):
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
    @param      fLOG                    logging function
    @return                             list of created jobs

    *modules* is a list defined as follows:

    * each element can be a string or a tuple (string, schedule time) or a list
    * if it is a list, it contains a list of elements defined as previously
    * the job at position i is not scheduled, it will start after the last
      job at position i-1 whether or not it fails
    """
    if modules is None:
        modules = default_jenkins_jobs()
    r = setup_jenkins_server_yml(js, github=github, modules=modules, get_jenkins_script=None,
                                 overwrite=overwrite, location=location, prefix=prefix,
                                 delete_first=delete_first, disable_schedule=disable_schedule)
    return r
