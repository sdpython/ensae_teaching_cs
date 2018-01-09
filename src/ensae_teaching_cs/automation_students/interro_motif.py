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
from ..td_1a.edit_distance import edit_distance


def _get_code(mail):
    m = hashlib.md5()
    m.update(mail)
    b = m.digest()
    return int(b[0])


def execute_python_scripts(root, df, col_names=None, url=None, eol="/", fLOG=noLOG, gen_mail=None):
    """
    Retrieves all :epkg:`python` scripts and run them.

    @param      root            main folder
    @param      df              dataframe
    @param      col_names       dictionary for columns:
                                folder, mail, program, out, err, url, cmp, url_content, key, time
    @param      eol             if not None, replaces end of lines by *eof*
    @param      gen_mail        generator of mails
    @param      fLOG            logging function
    @return                     dataframe
    """
    if gen_mail is None:
        def iter_mail(mail):
            yield mail
            yield mail.lower()
        gen_mail = iter_mail

    def post_process(out, eol):
        out = out.strip("\r\t\n").rstrip().replace(
            "\r", "").replace("\t", "    ")
        if eol:
            out = out.replace("\n", eol)
        return out

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
            res.append(row)
        else:
            row[col_find] = True
            store = []
            for py in explore_folder_iterfile(subf, ".*[.]py$"):
                store.append(py)
            fLOG("     -", len(store), "programs found")

            col_out = col_names.get("out", "out")
            col_err = col_names.get("err", "err")
            col_prog = col_names.get("program", "program")
            col_time = col_names.get("time", "time")
            col_key = col_names.get("key", "key")
            col_size = col_names.get("size", "size")
            col_url = col_names.get("url", "url")
            col_ind = col_names.get("pattern_id", "pattern_id")

            if len(store) == 0:
                for mm in sorted(gen_mail(mail.strip())):
                    mailid = _get_code(mm.encode("utf-8"))
                    r = row.copy()
                    loc = url.format(mailid)
                    ind = {col_key: mm, col_ind: mailid, col_url: loc}
                    r.update(ind)
                    res.append(r)
                continue

            # test all programs
            outs = []
            for py in sorted(store):
                cmd = '"{0}" "{1}"'.format(sys.executable, py)
                t1 = time.clock()
                try:
                    out, err = run_cmd(cmd, wait=True)
                except Exception as e:
                    out = None
                    err = str(e)
                out = post_process(out, eol)
                t2 = time.clock()
                outs.append({col_out: out, col_err: post_process(err, eol),
                             col_prog: os.path.split(py)[-1], col_time: t2 - t1,
                             col_size: os.stat(py).st_size})

            if url is None:
                for o in outs:
                    r = row.copy()
                    r.update(o)
                    res.append(r)
            elif url is not None:
                col_cmp = col_names.get("cmp", "cmp")
                col_in = col_names.get(
                    "sortie_dans_motif", "sortie_dans_motif")
                col_in2 = col_names.get(
                    "motif_dans_sortie", "motif_dans_sortie")
                col_dist = col_names.get("dist", "dist")
                col_content = col_names.get("content", "content")

                if out is None:
                    for ii, mm in gen_mail(mail.strip()):
                        mailid = _get_code(mm.encode("utf-8"))
                        ind = {col_ind: mailid}
                        for o in outs:
                            r = row.copy()
                            r.update(o)
                            r.update(ind)
                            res.append(r)
                else:
                    for mm in sorted(gen_mail(mail.strip())):
                        mailid = _get_code(mm.encode("utf-8"))
                        loc = url.format(mailid)
                        ind = {col_key: mm, col_ind: mailid, col_url: loc}

                        if loc not in downloads:
                            downloads[loc] = get_url_content_timeout(
                                loc).strip("\n\r\t ")
                        content = post_process(downloads[loc], eol)
                        ind[col_content] = content

                        for o in outs:
                            r = row.copy()
                            r.update(o)
                            r.update(ind)
                            out = r[col_out]
                            r[col_cmp] = out == content or out.strip(
                            ) == content.strip()
                            r[col_in] = out in content
                            r[col_in2] = content in out
                            r[col_dist] = (edit_distance(out, content)[0]) if (
                                len(content) > len(out) // 2) else abs(len(content) - len(out))
                            res.append(r)
    return pandas.DataFrame(res)
