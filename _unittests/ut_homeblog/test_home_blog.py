"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

try:
    import pyensae as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.filehelper import explore_folder
from pyquickhelper.pycode import get_temp_folder
from src.ensae_teaching_cs.homeblog import file_build_rss, CopyFileForFtp, modify_all_posts
from src.ensae_teaching_cs.homeblog import file_all_keywords, build_process_all_pages


class TestHomeBlog(unittest.TestCase):

    def test_homeblog(self):
        fLOG(__file__, self._testMethodName,
             OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_home_blog")
        blog = os.path.abspath(os.path.normpath(
            os.path.join(temp, "..", "blog")))

        filessite = explore_folder(blog)[1]
        filessite = [_.replace("\\", "/") for _ in filessite]
        if len(filessite) == 0:
            raise Exception("no file found")

        cpf = CopyFileForFtp("copyDates.txt", specificTrigger=True)
        cpf.copy_file_ext(os.path.join(temp, ".."), "py", temp, doFTP=False)
        cpf.copy_file_ext(os.path.join(blog, "javascript"),
                          "js", os.path.join(temp, "javascript"))
        cpf.copy_file_ext(os.path.join(blog, "javascript"),
                          "css", os.path.join(temp, "javascript"))

        files, modified = modify_all_posts(blog, blog, exclude=lambda f: False)
        self.assertTrue(len(files) > 0)
        res = file_build_rss(blog, os.path.join(temp, "xdbrss.xml"),
                             months_delay=100)
        rss = res[0]
        self.assertTrue(os.path.exists(rss))
        res = file_all_keywords(blog,
                                mainpage=os.path.join(blog, "xd_blog.html"),
                                outmainpage=os.path.join(blog, "xd_blog.html"),
                                exclude=lambda f: "improbable" in f, allow_temp=True)
        self.assertTrue(len(res) > 0)
        add = build_process_all_pages(res, frequence_keywords=2, siteFolder=temp,
                                      xd_blog_template_nojs=os.path.join(blog, "xd_blog_template_nojs.html"))
        fLOG(add)
        cpf.add_if_modified(__file__)

        if len(cpf.modifiedFile) > 0:

            # checking that username is not in the file
            modif = 0
            nbch = 0
            usernames = [os.environ.get(
                "USERNAME", os.environ.get("HOSTNAME", "")).lower()]
            for file, reason in sorted(cpf.modifiedFile):
                ext = os.path.splitext(file)[-1]

                if os.stat(file).st_size < 2**25 and ext.lower() not in \
                        [".mp3", ".zip", ".gif", ".dll", ".exe", ".msi",
                         ".eot", ".ttf", ".woff", ".mp4",
                         ".xlsx", ".7z", ".avi", ".xlsm",
                         ".gz", ".inv", ".pdf", ".png", ".jpg", ".jpeg"]:
                    content = None
                    contentu = None
                    encoding = None
                    try:
                        with open(file, "r") as f:
                            contentu = f.read()
                            content = contentu.lower()
                            encoding = None
                    except UnicodeDecodeError:
                        try:
                            with open(file, "r", encoding="utf8") as f:
                                contentu = f.read()
                                content = contentu.lower()
                                encoding = "utf8"
                        except Exception:
                            pass
                    except PermissionError:
                        fLOG("permission error for ", file)

                    if content is None:
                        fLOG("unable to check alias in ", file)
                    else:
                        # replacements
                        for username in usernames:
                            for substr, reps in [("c-3a-5c" + username, "c-3a-5cxxx")]:
                                if substr in contentu:
                                    contentu = contentu.replace(substr, reps)
                                    modif += 1

                        content = contentu.lower()
                        if modif > 0:
                            fLOG("modify", file)
                            if encoding is None:
                                with open(file, "w") as f:
                                    f.write(contentu)
                            else:
                                with open(file, "w", encoding=encoding) as f:
                                    f.write(contentu)

                        nbch += 1

            fLOG("number of checked files:", nbch)

            issues = []
            processed = []

            def sizef(name):
                ext = os.path.splitext(name)[-1]
                if ext in [".html", ".js", ".png", ".css", ".ico", ".py", ".ipynb"]:
                    return 0
                else:
                    return os.stat(name).st_size

            allfiles = [(sizef(file), file, reason)
                        for file, reason in cpf.modifiedFile]
            allfiles.sort()
            nbproc = 0

            for siz, file, reason in allfiles:

                processed.append(file)
                cpf.update_copied_file(file)
                cpf.save_dates(checkfile=processed)

                nbproc += 1
                if nbproc % 20 == 0 or siz > 2**25:
                    fLOG("******* processed", nbproc, "/",
                         len(cpf.modifiedFile), " size", siz)

        # final checking
        self.assertTrue(len(issues) == 0)
        self.assertTrue(os.path.join(temp, "2017-01-08_nojs.html"))
        self.assertTrue(os.path.join(temp, "javascript", "doxy.css"))


if __name__ == "__main__":
    unittest.main()
