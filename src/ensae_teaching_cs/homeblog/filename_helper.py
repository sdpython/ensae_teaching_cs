"""
@file
@brief Helpers around file names.
"""
import os
import re
from pyquickhelper.loghelper import noLOG
from pyquickhelper.filehelper import explore_folder


def get_file_per_folder(folder, deep=1):
    """
    extract all folders in a folder and then all files in these folders

    @param      folder      folder
    @param      deep        number of folders to considers before the filename
    @return                 dictionary
    """
    files = explore_folder(folder)[1]
    res = {}
    for f in files:
        spl = f.replace("\\", "/").split("/")
        if deep == 1:
            te = spl[-2]
            fi = spl[-1]
            if te not in res:
                res[te] = []
            res[te].append(fi)
        elif deep == 2:
            te = spl[-3:-1]
            fi = spl[-1]
            if te not in res:
                res[te] = []
            res[te].append(fi)
        else:
            raise RuntimeError("deep should be 1 or 2")
    return res


def normalize_name_and_numbers(files):
    """
    tries to match names and number in a file

    @param  files   list of files
    @return         list of tuple (number, normalized name, extension, suggested name, original name)
    """
    exp = re.compile(
        "([0-9a-z;() ]+([-][a-z ]+)?) ?[-] ?([0-9]{2,3})[ .v_CF[]")
    exp2 = re.compile("([0-9a-z;() ]+) episode ([0-9]{2,3})[ .v_CF[]")
    exp3 = re.compile("([a-z0-9 ]+[.][0-9]+) ?[-] ?([0-9]{2,3})[ .v_CF[]")
    res = []
    for fi in files:
        name = fi.lower().replace("_", " ").replace("!", " ")
        ext = os.path.splitext(fi)[-1]

        solution = None
        for ex, ind in [(exp, 2), (exp2, 1), (exp3, 1)]:
            num = ex.search(name)
            if num:
                grs = num.groups()
                nam = grs[0].strip()
                num = grs[ind]
                words = nam.split()
                for i in range(len(words)):
                    words[i] = words[i][0].upper() + words[i][1:]
                nam = " ".join(words)
                sugg = f"{nam} - {num}{ext}"
                if solution is None or len(nam) > len(solution[1]):
                    solution = (num, nam, ext, sugg, fi)
        if solution is not None:
            res.append(solution)

    res.sort()
    return res


def normalize_folder(folder, fLOG=noLOG):
    """
    normalize the filename of a whole folder and subfolders

    @param          folder      folder
    @return                     list of tuple (number, normalized name, extension, suggested name, original name)
    """
    alls = []
    files = get_file_per_folder(folder)
    for d in sorted(files):
        norm = normalize_name_and_numbers(files[d])
        for r in norm:
            if r[-2] != r[-1]:
                pat = os.path.join(folder, d, r[-1])
                nee = os.path.join(folder, d, r[-2])
                fLOG("rename", pat, " in ", nee)
                neelast = os.path.split(nee)[-1]
                if neelast[0] < 'A' or neelast[0] > 'Z':
                    raise RuntimeError(f"Bad name for {neelast} ({nee}).")
                os.rename(pat, nee)
        alls.extend(norm)
    return alls


def music_statistics(folder):
    """
    provides statistics on a folder

    @param      folder      folder
    @return                 dictionary { "folder": {  "last": ..., "missing": } }
    """
    res = {}
    files = get_file_per_folder(folder)
    for d in sorted(files):
        norm = normalize_name_and_numbers(files[d])
        for r in norm:
            if d not in res:
                res[d] = []
            res[d].append(int(r[0]))

    comp = {}
    for k, v in res.items():
        mi, ma = min(v), max(v)
        ke = {_: 1 for _ in v}
        li = [0 for i in range(ma + 1)]
        for _ in ke:
            li[_] = 1
        missing = [i for i, _ in enumerate(li) if _ == 0 and i >= mi]
        comp[k] = {"min": mi, "max": ma, "missing": missing}
    return comp
