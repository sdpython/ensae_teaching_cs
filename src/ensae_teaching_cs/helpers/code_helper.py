"""
@file
@brief Helpers about code.
"""
import os
import re
from pyquickhelper.filehelper import explore_folder_iterfile


def enumerate_inspect_source_code(folder, file_pattern=".*[.]((py)|(ipynb))$",
                                  neg_pattern=".*(([-]checkpoint)|(_todo)|(_temp)).*",
                                  line_patterns="from sklearn[_0-9a-zA-Z.]* import ([_a-zA-Z0-9]+);;import sklearn[.]([_a-z]+)",
                                  fullname=False):
    """
    Counts groups extracted from source file. We assume all selected files
    can be opened as text files encoded in :epkg:`utf-8` character set.

    @param      folder          folder to dig into
    @param      file_pattern    files to consider
    @param      neg_pattern     negative patterns for filenames
    @param      line_patterns   patterns to look into, separated by ``;;``
    @param      fullname        if True, include the subfolder while checking the regex
    @return                     list of dictionaries
    """
    regs = [re.compile(reg) for reg in line_patterns.split(';;')]
    nb = 0
    for name in explore_folder_iterfile(folder, pattern=file_pattern,
                                        neg_pattern=neg_pattern, fullname=fullname):
        nb += 1
        try:
            with open(name, "r", encoding="utf-8", errors='ignore') as f:
                for li, line in enumerate(f):
                    for pi, reg in enumerate(regs):
                        r = reg.search(line)
                        if r:
                            for g in r.groups():
                                obs = dict(group=g, name=name, line=li)
                                obs['patid'] = pi
                                yield obs
        except UnicodeDecodeError as e:
            raise FileNotFoundError(
                "Unable to process '{0}' due to '{1}'.".format(name, e))
    if nb == 0:
        found = os.listdir(folder)
        founds = "\n".join(found) if found else "EMPTY"
        raise FileNotFoundError(
            "No file found in folder '{0}' with pattern '{1}' (neg='{2}')\n--IN--\n{3}".format(folder, file_pattern, neg_pattern, founds))
