"""
@file
@brief Svg, Latex
"""
import os
import re
import urllib
import urllib.parse
import urllib.request
from pyquickhelper.loghelper import fLOG
from .latex2html import convert_short_latex_into_png


def load_file(filename):
    try:
        f = open(filename, "r", encoding="utf8")
        text = f.read()
        f.close()
        return text
    except Exception as e:  # pragma: no cover
        fLOG("e,", __name__, ": issue with ", filename)
        raise e


def get_url_latex(exp, gif):
    exp = exp.replace("\n", " ").strip("\n ").replace("\r", "")
    url = "http://latex.codecogs.com/gif.latex?" if gif else \
          "http://latex.codecogs.com/svg.latex?"
    exp = exp.replace("+", "AZERTY").replace("&lt;", "<").replace("&gt;", ">")
    exp = exp.replace("&amp;", "%26").replace("%", "%25")
    exp = urllib.parse.quote_plus(exp)
    exp = exp.replace("+", "%20").replace("AZERTY", "+")
    url += exp
    return url


def get_svg_or_gif(url):
    u = urllib.request.urlopen(url)
    text = u.read()
    u.close()
    return text


def get_latex_contraction(formula):
    exp = re.compile("([^a-zA-Z0-9])")
    res = exp.sub("", formula)
    return res


def text_replace_div_gif(text, htmltext, alt, gif, prefix, inline, size):
    filename = os.path.split(gif)[-1]
    filename = prefix + "/" + filename
    if not inline:
        rep = "<!--\n%s\n-->\n" % htmltext.replace('"latex"', '"latex_help"')
        alt = alt.replace("\n", " ")
        px = "%dpx" % (size[0] / 2)
        rep += '<p class="latexcenter">\n<img src="%s" alt="%s" title="%s" width="%s" />\n</p>\n' % (
            filename, alt, alt, px)
    else:
        rep = "<!--\n%s\n-->\n" % htmltext.replace(
            '"latex_inline"', '"latex_help_inline"')
        alt = alt.replace("\n", " ")
        px = "%dpx" % (size[0] / 2)
        rep += f' <img src="{filename}" alt="{alt}" title="{alt}" width="{px}" /> '
    text = text.replace(htmltext, rep)
    return text


def extract_div(prefix, prefiximage, text, logfunction, temp_folder):
    exp = re.compile("(<div +lang=\\\"latex(_inline)?\\\">((.|\\n)+?)</div>)")
    res = exp.findall(text)
    images = []
    for a, inline, b, _ in res:
        logfunction("    ------------ converting (div), prefix ", prefix)
        logfunction("    latex: " + b.strip("\n ").replace("\n", " "))
        cont = get_latex_contraction(b)
        image = prefix + cont + ".gif"
        if not os.path.exists(image):
            # using a local installation of miktex
            image, size = convert_short_latex_into_png(
                b, temp_folder=temp_folder, fLOG=logfunction, final_name=image)
            images.append(image)
        else:
            from PIL import Image
            im = Image.open(image)
            size = im.size
        logfunction("    replacing: " + image)
        text = text_replace_div_gif(
            text, a, b, image, prefiximage, len(inline) > 0, size)

    return len(res), text, images


def text_replace_span_gif(text, htmltext, alt, gif, prefix):
    filename = os.path.split(gif)[-1]
    filename = prefix + "/" + filename
    rep = "<!-- %s -->" % htmltext.replace('"latex"', '"latex_help"')
    alt = alt.replace("\n", " ")
    rep += f'<img src="{filename}" alt="{alt}" title="{alt}" />'
    text = text.replace(htmltext, rep)
    return text


def extract_span(prefix, prefiximage, text, logfunction):
    exp = re.compile("(<span +lang=\\\"latex\\\">((.|\\n)+?)</span>)")
    res = exp.findall(text)
    for a, b, _ in res:
        logfunction("    ------------ converting (span) ")
        logfunction("    latex: " + b.strip("\n ").replace("\n", " "))
        cont = get_latex_contraction(b)
        image = prefix + cont + ".gif"
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        logfunction("    replacing: " + image)
        text = text_replace_span_gif(text, a, b, image, prefiximage)

    return text


def replace_file(file, outfile, prefix, giflatex, logfunction, temp_folder):
    logfunction("    replacing formulas in html for file ", file)
    text = load_file(file)
    keep_text = text
    prefix += file.replace("/", "_").replace("\\",
                                             "_").replace(":", "_") + "__"
    _, text, images = extract_div(
        prefix, giflatex, text, logfunction, temp_folder)
    text = extract_span(prefix, giflatex, text, logfunction)
    if text != keep_text:
        logfunction("found formulas in ", file, " nb images ", len(images))
        f = open(outfile, "w", encoding="utf8")
        f.write(text)
        f.close()
    else:
        fLOG("i, no detected changes for ", file)
    return outfile, images


def print_function(*s):
    fLOG("i,", *s)
    return s
