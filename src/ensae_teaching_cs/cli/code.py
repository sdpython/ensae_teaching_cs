"""
@file
@brief Starts an app locally to test it.
"""
from ..helpers import enumerate_inspect_source_code


def inspect_source_code(folder, file_pattern=".*[.]((py)|(ipynb))$",
                        line_patterns="from sklearn[_0-9a-zA-Z.]* import ([_a-zA-Z0-9]+);;import sklearn[.]([_a-z]+)",
                        neg_pattern=".*(([-]checkpoint)|(_todo)|(_temp)).*",
                        fullname=False, fLOG=print):
    """
    Counts groups extracted from source file. We assume all selected files
    can be opened as text files encoded in :epkg:`utf-8` character set.
    Prints the results on the standard output. First line is a header.

    :param folder: folder to dig into
    :param file_pattern: files to consider
    :param neg_pattern: negative patterns for filenames
    :param line_patterns: patterns to look into, separated by ``;;``
    :param fullname: if True, include the subfolder while checking the regex
    :param fLOG: logging function
    :return: list of dictionaries
    """
    cols = None
    for obs in enumerate_inspect_source_code(folder, file_pattern=file_pattern,
                                             neg_pattern=neg_pattern,
                                             line_patterns=line_patterns,
                                             fullname=fullname):
        if cols is None:
            cols = list(sorted(obs))
            fLOG(",".join(cols))
        values = [str(obs[k]) for k in cols]
        fLOG(",".join(values))
