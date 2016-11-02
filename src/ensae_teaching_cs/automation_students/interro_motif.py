#-*- coding: utf-8 -*-
"""
@file
@brief Retrieve python files and run them.
"""
import os
import sys
import hashlib
import pandas
import time
from pyquickhelper.loghelper import noLOG, run_cmd
from pyquickhelper.filehelper import explore_folder_iterfile
from pyquickhelper.filehelper.download_helper import get_url_content_timeout


def _get_code(mail):
    m = hashlib.md5()
    m.update(mail)
    b = m.digest()
    return int(b[0])


def execute_python_scripts(root, df, col_names=None, url=None, eol="/", fLOG=noLOG):
    """
    retrieve all python scripts and run them

    @param      root            main folder
    @param      df              dataframe
    @param      col_names       dictionary for columns:
                                folder, mail, program, out, err, index, url, cmp, url_content
    @param      eol             if not None, replaces end of lines by *eof*
    @param      fLOG            logging function
    @return                     dataframe
    """
    downloads = {}
    res = []
    for name, mail in zip(df[col_names.get("folder", "folder")], df[col_names.get("mail", "mail")]):
        row = {col_names.get("folder", "folder"): name}
        fLOG("[execute_python_script], look into '{0}'".format(name))
        subf = os.path.join(root, name)
        col_find = col_names.get("exists", "exists")
        if not os.path.exists(subf):
            subf = os.path.join(root, name.replace("-", "."))
        if not os.path.exists(subf):
            row[col_find] = False
        else:
            row[col_find] = True
            store = []
            for py in explore_folder_iterfile(subf, ".*[.]py$"):
                d = os.stat(py).st_mtime
                store.append((d, py))
            fLOG("     -", store)
            if len(store) == 0:
                for ii, mm in enumerate([mail.strip(), mail.lower().strip()]):
                    mailid = _get_code(mm.encode("utf-8"))
                    row[col_names.get("index%d" % ii, "index%d" % ii)] = mailid
                res.append(row)
                continue

            m = max(store)
            py = m[1]
            row[col_names.get("program", "program")] = os.path.split(py)[-1]
            cmd = '"{0}" "{1}"'.format(sys.executable, py)
            t1 = time.clock()
            try:
                out, err = run_cmd(cmd, wait=True)
                row[col_names.get("out", "out")] = out.replace(
                    "\r", "").replace("\t", "    ")
                row[col_names.get("err", "err")] = err
                if eol:
                    row[col_names.get("out", "out")] = row[
                        col_names.get("out", "out")].replace("\n", eol)
            except Exception as e:
                row[col_names.get("err", "err")] = str(e)
                out = None
            t2 = time.clock()
            row[col_names.get("execution_time", "execution_time")] = t2 - t1

            if url is not None:
                if out is None:
                    for ii, mm in enumerate([mail.strip(), mail.lower().strip()]):
                        mailid = _get_code(mm.encode("utf-8"))
                        row[col_names.get("index%d" %
                                          ii, "index%d" % ii)] = mailid
                else:
                    for ii, mm in enumerate([mail.strip(), mail.lower().strip()]):
                        mailid = _get_code(mm.encode("utf-8"))
                        row[col_names.get("index%d" %
                                          ii, "index%d" % ii)] = mailid
                        loc = url.format(mailid)
                        row[col_names.get("url%d" % ii, "url%d" % ii)] = loc
                        if loc not in downloads:
                            downloads[loc] = get_url_content_timeout(
                                loc).strip("\n\r\t ")
                        content = downloads[loc]
                        out = out.strip("\n\r\t ")
                        out = out.replace("\r", "").replace("\t", "    ")
                        content = content.replace(
                            "\r", "").replace("\t", "    ")
                        if eol:
                            out = out.replace("\n", eol)
                            content = content.replace("\n", eol)
                        row[col_names.get("cmp%d" % ii, "cmp%d" %
                                          ii)] = out == content
                        row[col_names.get("url_content%d" %
                                          ii, "url_content%d" % ii)] = content

        res.append(row)
    return pandas.DataFrame(res)
