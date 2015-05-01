# -*- coding: utf-8 -*-
"""
@file
@brief  Retrive political speeches from Internet

"""

import sys
import re
import json
import io
import html.parser
import html.entities as htmlentitydefs
from pyquickhelper import get_url_content


endLine = "\r\n"


def xmlParsingLongestDiv(text):
    """
    extract the longest div section

    @param      text        text of HTML page
    @return                 text
    """
    class MyHTMLParser(html.parser.HTMLParser):

        """
        to get rid of paragraphs, and bolded text
        """

        def __init__(self):
            if sys.version_info.major >= 4 or (sys.version_info.minor >= 4 and \
                sys.version_info.major >= 3):
                html.parser.HTMLParser.__init__(self, convert_charrefs=True)
            else:
                html.parser.HTMLParser.__init__(self)
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
                global endLine
                if tag == "p" or tag == "br":
                    self.mvalue[-1].append(endLine)
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

    global endLine
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
    if (len(nb) == 0 or len(res) >
            10000) and "if (window.xtparam!=null)" not in res:
        return res
    else:
        return ""


def html_unescape(text):
    """
    Removes HTML or XML character references and entities from a text string.
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
    return re.sub("&#?\w+;", fixup, text)


def force_unicode(text):
    """
    deal with unicodes

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
            text = text.replace("Ã´", "o").replace("Ã©", "e").replace("Ã", "a")
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


def retrieve_speeches_json(
        url="http://www.elysee.fr/chronologie/download/json"):
    """
    retrieve the speeches from the Elysées

    @param      url     url
    @return             list of documents
    """
    text = get_url_content(url)
    stream = io.StringIO(text)
    js = json.load(stream)
    return js


def remove_accent(text):
    """
    replaces French accents by regular letters

    @param  text        text
    @return             cleaned text
    """
    for c in ["aàâä", "eéèêë", "iîï", "oöô", "uùüû"]:
        for d in c[1:]:
            text = text.replace(c, d)
    return text


def get_elysee_speech_from_elysees(
        title, url="http://www.elysee.fr/chronologie/article/"):
    """
    retrieve the text from Elysées

    @param      title       title of the document
    @param      url         weebiste
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
        return None
        raise Exception(
            "unable to fetch content from: " +
            title +
            "\n" +
            full) from e
    return xmlParsingLongestDiv(text)


def enumerate_speeches_from_elysees(skip=0, use_json=False):
    """
    enumerates speeches Elysees Speeches

    @param      skip        skip the first one in the list
    @param      use_json    or json format or xml (json format is incomplete)
    @return                 enumerate dictionaries

    @example(Récupérer des discours du président de la république)

    @code
    for i,disc in enumerate(enumerate_speeches_from_elysees()):
        print(disc)
    @endcode

    @endexample

    """
    if use_json:
        url = "http://www.elysee.fr/chronologie/download/json"
        js = retrieve_speeches_json(url)
        for i, event in enumerate(js):
            if i < skip:
                continue
            items = event.get("items", None)
            title = event.get("title", None)
            if items is not None and title is not None and len(title) > 0:
                load = False
                for it in items:
                    if it is None:
                        continue
                    if not isinstance(it, dict):
                        continue
                    tit = it.get("title", "")
                    if tit is not None and "title" in it and "discours" in tit:
                        load = True
                        break
                if load:
                    content = get_elysee_speech_from_elysees(title)
                    if content is not None:
                        yield dict(text=content,
                                   title=title,
                                   date=event.get("date", None),
                                   description=event.get("description", None))
    else:
        url = "http://www.elysee.fr/chronologie/download/xml"
        xml = get_url_content(url)
        reg = re.compile("(http://.*?/article/.*?/)")
        links = reg.findall(xml)
        for i, link in enumerate(links):
            content = get_elysee_speech_from_elysees(link)
            if content is not None:
                yield dict(link=link, text=content)
