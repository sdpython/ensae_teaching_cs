# -*- coding: utf-8 -*-
"""
@file
@brief  Retrive political speeches from Internet

"""

import re
import html.parser
import html.entities as htmlentitydefs
import warnings
from pyquickhelper.loghelper import get_url_content


def xmlParsingLongestDiv(text):
    """
    Extracts the longest div section.

    @param      text        text of HTML page
    @return                 text
    """
    class MyHTMLParser(html.parser.HTMLParser):
        """
        To get rid of paragraphs, and bolded text.
        """

        def __init__(self):
            html.parser.HTMLParser.__init__(self, convert_charrefs=True)
            self.mtag = []
            self.mvalue = []
            self.mall = []

        def handle_starttag(self, tag, attrs):
            if tag == "div":
                self.mtag.append(tag)
                self.mvalue.append([])
            elif len(self.mtag) > 0:
                self.mvalue[-1].append(" ")

        def handle_endtag(self, tag):
            if tag == "div":
                self.mall.append((self.mtag[-1], "".join(self.mvalue[-1])))
                self.mtag.pop()
                self.mvalue.pop()
            elif len(self.mtag) > 0:
                if tag == "p" or tag == "br":
                    self.mvalue[-1].append("\n")
                else:
                    self.mvalue[-1].append(" ")

        def handle_data(self, data):
            if len(self.mtag) > 0:
                self.mvalue[-1].append(data)

    parser = MyHTMLParser()
    text = text.replace(" -g8\" ", " ")
    parser.feed(text)

    best = ""
    for tag, value in parser.mall:
        if tag == "div" and len(value) > len(best):
            best = value

    endLine = "\n"
    res = best.replace(
        "<p>",
        "").replace(
        "</p>",
        endLine).replace(
            "\r",
            "").replace(
                "<br />",
                endLine).replace(
                    "<br>",
        endLine)
    exp = re.compile("[|]((.|\n){5,50}) ")
    nb = exp.findall(res)
    if (len(nb) == 0 or len(res) > 10000) and "if (window.xtparam!=null)" not in res:
        return res
    else:
        return ""


def html_unescape(text):
    """
    Removes :epkg:`HTML` or :epkg:`XML`
    character references and entities from a text string.
    keep ``&amp;``, ``&gt;``, ``&lt;`` in the source code.
    from `Fredrik Lundh <http://effbot.org/zone/re-sub.htm#unescape-html>`_

    @param      text        text
    @return                 cleaning text
    """
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            try:
                if text[:3] == "&#x":
                    return chr(int(text[3:-1], 16))
                else:
                    return chr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                if text[1:-1] == "amp":
                    text = "&amp;amp;"
                elif text[1:-1] == "gt":
                    text = "&amp;gt;"
                elif text[1:-1] == "lt":
                    text = "&amp;lt;"
                else:
                    text = chr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text  # leave as is
    return re.sub("&#?\\w+;", fixup, text)


def force_unicode(text):
    """
    Deals with unicodes.

    @param      text        text
    @return                 text
    """
    exp = re.compile("([0-9]+):")
    turn = 0
    while True:
        try:
            text = text.encode("ascii", errors="ignore")
            break
        except UnicodeDecodeError as e:
            pos = exp.findall(str(e))
            pos = int(pos[0])
            text = text.replace("Ã´", "o").replace(
                "Ã©", "e").replace("Ã", "a")
            text = text.replace(
                "  ",
                " ").replace(
                "â€™",
                "'").replace(
                "a§",
                "c")
            text = text.replace(
                "a¹",
                "u").replace(
                "a¨",
                "e").replace(
                "a‰",
                "E")
            text = text.replace(
                "a¢",
                "a").replace(
                "aª",
                "e").replace(
                "aƒÂ´",
                "o")
            text = text.replace(
                "aƒÂ©",
                "e").replace(
                "aƒÂ",
                "e").replace(
                "Â©",
                "e")
            text = text.replace(
                "a»",
                "u").replace(
                "â‚¬",
                "E").replace(
                "a®",
                "i")
            text = text.replace(
                '\xa0',
                " ").replace(
                "Å“",
                "oe").replace(
                "Â«",
                " ")
            text = text.replace(
                "Â»",
                " ").replace(
                "e¹ ",
                "ei").replace(
                "‚Â",
                " ")
            turn += 1
            if turn > 100:
                # too much
                return None
    return text


def remove_accent(text):
    """
    Replaces French accents by regular letters.

    @param  text        text
    @return             cleaned text
    """
    for c in ["aàâä", "eéèêë", "iîï", "oöô", "uùüû"]:
        for d in c[1:]:
            text = text.replace(c, d)
    return text


def get_elysee_speech_from_elysees(title, url="https://www.elysee.fr/"):
    """
    Retrieves the text from the :epkg:`Elysees`.

    @param      title       title of the document
    @param      url         website
    @return                 html page

    The function tries something like::

        url + title.replace(" ","-")
    """
    if title.startswith("http"):
        full = title
    else:
        if not url.endswith("/"):
            raise Exception("url should end with /: " + url)
        link = remove_accent(title.lower()).replace(
            " ", "-").replace("'", "-").replace('"', "")
        full = url + "/" + link + "/"
    try:
        text = get_url_content(full)
    except Exception as e:
        warnings.warn("Unable to retrieve '{0}' - {1}".format(full, e))
        return None
    return xmlParsingLongestDiv(text)


def enumerate_speeches_from_elysees(url="agenda", skip=0):
    """
    Enumerates speeches from the :epkg:`Elysees`.

    @param      url         subaddress, url source will be
                            ``'https://www.elysee.fr/' + url``
    @param      skip        skip the first *skip* one in the list
    @return                 enumerate dictionaries

    .. exref::
        :title: Récupérer des discours du président de la république
        :tag: Exercice

        ::

            for i, disc in enumerate(enumerate_speeches_from_elysees()):
                print(disc)

    Others links can be used such as
    ``https://www.elysee.fr/recherche?query=discours``.
    The website changed in 2018 and no longer support xml or json
    streams.
    """
    base = "https://www.elysee.fr/"
    if not url.startswith("http"):
        url = base + url
    xml = get_url_content(url)
    reg = re.compile(
        "href=\\\"(.+?/[0-9]{4}/[0-9]{2}/[0-9]{2}/.+?)\\\" class=")
    links = reg.findall(xml)
    for i, link in enumerate(links):
        if i < skip:
            continue
        if link.startswith("/"):
            link = base + link
        content = get_elysee_speech_from_elysees(link)
        if content is not None:
            yield dict(link=link, text=content)
    if len(links) == 0:
        raise ValueError("Unable to extract links from url='{0}'\npattern='{1}'\n-----\n{2}".format(
            url, reg, xml))
