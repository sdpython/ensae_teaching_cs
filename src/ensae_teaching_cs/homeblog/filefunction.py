"""
@file
@brief Helpers for files
"""
import os
import glob
import re


def liste_fichier_repertoire(folder, filter):
    file, fold = [], []
    res = glob.glob(folder + "/" + filter)
    rep = glob.glob(folder + "/*")
    for r in rep:
        if r not in res and os.path.isdir(r):
            res.append(r)
    for r in res:
        path = r
        if os.path.isfile(path):
            file.append(path)
        else:
            fold.append(path)
            fi, fo = liste_fichier_repertoire(path, filter)
            file.extend(fi)
            fold.extend(fo)
    return file, fold


def isTemporaryFolder(path):
    iter = 0
    a, b = os.path.split(path)
    while len(a) > 0 and a != ".":
        if b.startswith("temp"):
            return True
        if b.startswith("cloudera-quickstart-demo"):
            return False
        la = a
        a, b = os.path.split(a)
        if a == la:
            break
        iter += 1
        if iter > 30:
            raise RuntimeError(
                "unable to continue, too many subfolders: " + path + "\na,b: " + a + "," + b)
    if b.startswith("temp"):
        return True
    return False


def find_all_blogs_function(folder=".", exclude=None, allow_temp=False):
    if len(folder) == 0:
        raise ValueError("folder is empty, it should be at least '.'")
    file = liste_fichier_repertoire(folder, "*.html")[0]
    exp = re.compile("[0-9-]{10}[.]html")
    file = [_ for _ in file if exp.search(os.path.split(_)[-1])]
    file = [
        _ for _ in file if "dprivate" not in _ and (allow_temp or not isTemporaryFolder(_))]
    if exclude is not None:
        file = [_ for _ in file if not exclude(_)]
    return file
