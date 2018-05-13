"""
@file
@brief Too old to remember what it is needed
"""

import re


def cleanFileFromtohtmlreplace(content):

    if "#" + "## tohtmlreplace BEGIN ###" in content:
        exps = "(#" + "## tohtmlreplace BEGIN ###((.|\n)*?)"
        exps += "#" + "## tohtmlreplace ELSE ###((.|\n)*?)"
        exps += "#" + "## tohtmlreplace END ###"
        exps += ")"
        exp = re.compile(exps)
        res = exp.findall(content)
        if len(res) == 0:
            raise ValueError("unable to understand the format\n" + exps)

        for rs in res:
            torep = rs[0]
            byrep = rs[1]
            content = content.replace(torep, byrep)

    return content
