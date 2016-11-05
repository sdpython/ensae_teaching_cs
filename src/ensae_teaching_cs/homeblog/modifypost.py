"""
@file
@brief Helpers which modify a post.
"""
import xml.dom.minidom
import os
from pyquickhelper.loghelper import fLOG
from .filefunction import find_all_blogs_function
from .postclassification import privateKeyClassificationMandatory, classify_post


def _write_data(writer, data, section):
    """
    Writes datachars to writer and deals with < >
    @param      writer      stream or file
    @param      data        string to write
    @param      section     depending of this name,
                            some special characters are processed or not (pre or !pre)
    """
    if data:
        if section == "pre":
            data = data.replace("&", "&amp;") \
                       .replace("<", "&lt;") \
                       .replace(">", "&gt;")
        elif section == "script":
            pass
        else:
            if section is None:
                raise ValueError("section name is empty")
            data = data.replace("&", "&amp;") \
                       .replace("<", "&lt;") \
                       .replace("\"", "&quot;") \
                       .replace(">", "&gt;")
        writer.write(data)


def Text_writexml(self, writer, indent="", addindent="", newl=""):
    section = self.localName
    if section is None:
        section = self.sectionNameSpecial
    if section is None:
        raise ValueError("section name is empty")
    _write_data(writer, "%s%s%s" % (indent, self.data, newl), section)


def Element_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
    writer.write(indent + "<" + self.tagName)

    attrs = self._get_attributes()
    a_names = sorted(attrs.keys())

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        _write_data(writer, attrs[a_name].value, "")
        writer.write("\"")
    if self.childNodes:
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.localName is None:
                node.sectionNameSpecial = self.localName
            node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))


xml.dom.minidom._write_data = _write_data
xml.dom.minidom.Text.writexml = Text_writexml
xml.dom.minidom.Element.writexml = Element_writexml


def information_from_xml(fullFileContent, file):
    text = fullFileContent

    # read xml
    try:
        dom = xml.dom.minidom.parseString(text)
    except Exception as e:
        fLOG("issue with file ", file)
        ee = str(e)
        ee = ee[ee.find("line"):]
        print("  File \"%s\", %s syntax error" % (file, ee))
        raise e

    # get attributes
    attr = {}
    link = []
    head = dom.documentElement.getElementsByTagName("head")[0]
    for no in head.childNodes:
        if no.localName == "META":
            raise ValueError("upper META")
        if no.localName == "meta" and "name" in no.attributes:
            name = no.attributes["name"].value
            content = no.attributes["content"].value
            attr[name] = content

        if no.localName == "title":
            attr["title"] = no.toxml()
        if no.localName == "link":
            link.append(no.attributes["href"].value)

    if len(attr) == 0:
        raise ValueError("document " + file + " has no attribute")

    content = dom.documentElement.getElementsByTagName("body")[0].toxml()

    return dom, attr, link, head, content


def modify_header_attributes(dom, headerattr):
    """
    the function do not modify links
    """
    head = dom.documentElement.getElementsByTagName("head")[0]
    for no in head.childNodes:
        if no.localName == "META":
            raise ValueError("upper META")
        if no.localName == "meta" and "name" in no.attributes:
            name = no.attributes["name"].value
            if name in headerattr:
                content = headerattr[name]
                if not isinstance(content, str):
                    raise TypeError(
                        "content should be a string not " + str(type(content)))
                no.attributes["content"].value = content

        for key in ["title"]:
            if no.localName == key and key in headerattr:
                content = headerattr["title"]
                if not isinstance(content, str):
                    raise TypeError(
                        "content should be a string not " + str(type(content)))
                no.value = content


def load_and_modify_xml_dom(file, outfile, check_keywords=True):
    f = open(file, "r", encoding="utf8")
    text = f.read()
    f.close()

    memo = text

    # cleaning malformations

    text = text.replace('<meta http-equiv="Content-Type" content="text/html; charset=utf-8">',
                        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')

    text = text.replace('''<LINK REL="stylesheet" TYPE="text/css" HREF='../pMenu.css'>''',
                        '''<LINK REL="stylesheet" TYPE="text/css" HREF='../pMenu.css' />''')

    text = text.replace("<HTML>", "<html>")
    text = text.replace("<HEAD>", "<head>")
    text = text.replace("</HEAD>", "</head>")
    text = text.replace('"../pMenu.css"', '"pMenu.css"')
    text = text.replace("'../pMenu.css'", '"pMenu.css"')
    text = text.replace(" HREF=", " href=")
    text = text.replace("<LINK REL=", "<link rel=")
    text = text.replace("<LINK TYPE=", "<link type=")

    dom, attr, link, head, content = information_from_xml(text, file)

    if "title" not in attr:
        raise ValueError("no title in " + file)
    if "pMenu.css" not in link:
        raise ValueError("no pMenu.css in " + file)

    if "date" not in attr:
        date = os.path.split(file)[-1]
        date = date[:10]
        attr["date"] = date
        ele = dom.createElement("meta")
        ele.attributes["name"] = "date"
        ele.attributes["content"] = date
        head.appendChild(ele)

    # change keywords
    keywords = [_.strip() for _ in attr["keywords"].split(",")]
    mod_keywords = classify_post(keywords, content)

    if check_keywords:
        inter = [_ for _ in privateKeyClassificationMandatory
                 if _ in mod_keywords]
        if len(inter) == 0:
            raise Exception("the post should be at least technical or recreative:\n  File: \"" + str(file) + "\ntitle: " + attr[
                            "title"] + "\nkeywords: " + str(keywords) + "\nmandatory\n" + str(privateKeyClassificationMandatory) + "\"")

    attr["keywords"] = ", ".join(mod_keywords)

    # modify header
    modify_header_attributes(dom, attr)

    # from xml to text
    if outfile is not None:

        text = dom.documentElement.toxml()
        text = text.replace('type="text/javascript"/>',
                            'type="text/javascript"></script>')
        header = '<?xml version="1.0" encoding="utf-8"?>'
        text = header + "\n" + text

        resfile = None
        if os.path.exists(outfile):
            f = open(outfile, "r", encoding="utf8")
            oldtext = f.read()
            f.close()
        else:
            oldtext = ""

        if oldtext != memo:
            # text is different, update it
            direct = os.path.split(outfile)[0]
            if not os.path.exists(direct):
                os.makedirs(direct)

            fLOG("updating ", file)
            f = open(outfile, "w", encoding="utf8")
            f.write(text)
            f.close()
            resfile = outfile

        return dom, resfile
    else:
        return dom


def modify_all_posts(folder=".",
                     outfolder=None,
                     exclude=None):
    """
    modifies, checks the syntax of every post
    @param      folder      folder (also process subfolders)
    @param      outfolder   new location (the modified post is copied somewhere else),
                            if None, replace the file
    @param      exclude     if not None, function which avoids some file the function
                            returns a True value, example:

                            ::

                                lambda f : "_old" in f

    @return                 files, modified where:
                                * files is the list of files processed
                                * modified is the list of modified files
    """
    if outfolder is None:
        outfolder = folder
    folder = os.path.abspath(folder)
    outfolder = os.path.abspath(outfolder)
    files = find_all_blogs_function(folder, exclude)
    modified = []

    for file in files:
        outfile = file.replace(folder, outfolder)
        fLOG("  loading file ", file, ' to ', outfile)
        dom, outfile = load_and_modify_xml_dom(file, outfile)
        if outfile is not None:
            modified.append(outfile)

    return files, modified
