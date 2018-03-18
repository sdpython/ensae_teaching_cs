import os
import sys

header = """
.. |pyecopng| image:: _static/pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. |pystatpng| image:: _static/pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist
"""

from pyquickhelper.texthelper import remove_diacritics

files = [_ for _ in os.listdir('.') if 'td_2a' in _]


def get_title(current):
    title = None
    for i, zoo in enumerate(current):
        if "++++" in zoo:
            title = current[i-1]
    if title is None:
        # print("-------------Issue-----------\n{0}".format("\n".join(current)))
        return None
    else:
        title = title.replace(" ", "_").replace(
            ",", "").replace("/", "").replace('-', '')
        title = title.replace('__', '_')
        title = remove_diacritics(title).lower()
    return title


for name in files:
    with open(name, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    parts = {}
    current = []
    for ii, line in enumerate(lines):
        if line.startswith("|py"):
            title = get_title(current)
            if title is None:
                continue
            if title in parts:
                parts[title].extend(current)
            else:
                parts[title] = current
            current = []
        current.append(line)

    if len(current) > 0:
        title = get_title(current)
        if title is None:
            continue
        if title in parts:
            parts[title].extend(current)
        else:
            parts[title] = current

    for k, v in parts.items():
        na, ext = os.path.splitext(name)
        print(na, k, ext)
        if ext is None or '.' not in ext:
            raise Exception(name)
        full = na + "_" + k + ext
        full = full.replace("td_2a", "td2a")
        with open(full, 'w', encoding='utf-8') as f:
            f.write('\n')
            f.write(header)
            f.write('\n')
            f.write('\n')
            f.write("\n".join(v))
