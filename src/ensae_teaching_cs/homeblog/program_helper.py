"""
@file
@brief Various function about programs such as guessing the language of a code
"""
import re


def guess_language_code(code):
    """
    Guess the language of a piece of code.
    The result can be: js, xml, html, cpp, py, sql, vba, css

    @param      code        code
    @return                 type of language or None if None if not found, score (in [0,1], 1 is good)

    The algorithm is to compare two languages bamong each others on keywords they don't have in common
    """
    code = code.replace(" ", "  ").replace(
        "\r", "").replace("\n", "  ").replace("\t", "    ")
    stripcode = code.strip()
    if stripcode.startswith("<html>") or \
            stripcode.startswith("<xml") or \
            stripcode.startswith("<!DOCTYPE html>"):
        return ('xml', 1.0)
    exp1 = re.compile("[^a-z]([a-z]{2,8})[^a-z0-9]")
    exp2 = re.compile("(</?[a-z]{2,8}( |>))")
    keywords = {"py": set("format with len from numpy enumerate as and or ord range try except raise for while if else elif with self assert " +
                          "for in if not import del from map random sys append except in range elif float str def raise except none".split()),
                "sql": set("on outer full as count and or desc asc from select group by order where join inner".split()),
                "xml": set("<body> <xml> </body> <script> <script </script> <head> </head> <meta> <meta </meta>".split()),
                "css": set("border font background size".split()),
                "vb": set("error for sub function while wend then to end next dim set".split()),
                "cpp": set("ord try catch throw try for while if else push for foreach delete vector map if catch void double string new throw null".split()),
                "js": set("try catch throw for while if else push for in if catch var throw new function null".split()),
                }
    comments = {"py": re.compile("#[^#]"),
                "sql": re.compile("--[^-]"),
                "css": re.compile("//[/]"),
                "vb": re.compile("'' "),
                "xml": re.compile("<!--[^-]"),
                }
    comments["cpp"] = comments["js"] = comments["css"]

    mat = {}
    for k, v in keywords.items():
        for k2, v2 in keywords.items():
            if k == k2:
                continue
            inter = v.intersection(v2)
            vd = v - inter
            v2d = v2 - inter
            mat[k, k2] = (vd, v2d)
            if comments[k] != comments[k2]:
                mat[k, k2] += (comments[k], comments[k2])

    token = exp1.findall(code) + exp2.findall(code)

    counts = {}
    for k, v in mat.items():
        c = [0, 0, 0, 0, [], [], None, None]
        for t in token:
            if t in v[0]:
                c[0] += 1
                c[4].append(t)
            if t in v[1]:
                c[1] += 1
                c[5].append(t)
            if len(v) > 2:
                co1 = v[2].findall(code)
                co2 = v[3].findall(code)
                c[6] = co1
                c[7] = co2
                c[2], c[3] = len(co1), len(co2)
        counts[k] = c

    #~ for k in sorted(counts) :
        #~ print (k,counts[k])
        #~ if sum(counts[k][:4]) == 0 :
        #~ print (k, mat[k])
        #~ print (token)

    # we find a language which wins every battle
    better = {}
    for k, c in counts.items():
        if c[0] + c[2] >= c[1] + c[3]:
            better[k[0]] = better.get(k[0], 0) + 1

    #print (better)

    li = [(v, k) for k, v in better.items()]
    li.sort()
    if len(li) > 0:
        if li[-1][0] == len(keywords) - 1 and (len(li) == 1 or li[-2][0] < len(keywords) - 1):
            ans = li[-1][1]
            sh = [(v, k) for k, v in counts.items() if k[0] == ans]
            co = [((v[0] + v[2]) / sum(v[:4]), k) for v, k in sh]
            co.sort()
            #print (co)
            return (ans, co[0][0])
        else:
            return None
    else:
        return None
