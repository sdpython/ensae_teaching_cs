# -*- coding: utf-8 -*-
"""
@file
@brief Contains the main function to published my blog (http://www.xavierdupre.fr/blog).
executed:
"""
import re
import os
import xml.dom.minidom
from pyquickhelper.loghelper import fLOG
from .modifypost import load_and_modify_xml_dom
from .filefunction import find_all_blogs_function


def removeAccent(s):
    return re.sub("([^~+'.0-9,ea-zA-Z&; -])", "", s)


def removeAccent_debug(s):
    return re.sub("([^~+'.çôéàèâû0-9,ea-zA-Z&; -])", "", s)


def removeHtmlAccent(s):
    s = s.replace("é", "&eacute;") \
         .replace("à", "&agrave;") \
         .replace("â", "&acirc;") \
         .replace("ê", "&ecirc;") \
         .replace("ô", "&ocirc;") \
         .replace("è", "&egrave;") \
         .replace("ç", "&ccedil;") \
         .replace("û", "&ucirc;")
    return s


def FixIssuesWithAccent(text):
    """
    voir http://migo.sixbit.org/more/html-entities.html
    http://www.thesauruslex.com/typo/eng/enghtml.htm
    @code
    é = Ã© = &eacute;
    è = Ã¨ = &egrave;
    à = Ã  = &agrave;
    ï = Ã¯ = &iuml;
    ô = Ã´ = &ocirc;
    ç = Ã§ = &ccedil;
    ê = Ãª = &ecirc;
    ù = Ã¹ = &ugrave;
    æ = Ã¦ = &aelig;
    œ = Å = &oelig;
    ë = Ã« = &euml;
    ü = Ã¼ = &uuml;
    â = Ã¢ = &acirc;
    € = â¬ = &euro;
    © = Â© = &copy;
    ¤ = Â¤ = &curren;
    @endcode
    """
    o = text

    correspondance = [
        ("ã©", "é"),
        ("Ã´", "ô"),
        ("Ã¢", "â"),
        ("Ã®", "î"),
        ("Ã¨", "è"),
        ("Ãª", "ê"),
        ("Ã¢", "â"),
        ("Ã§", "ç"),
        ("Ã ", "à "),
        ("\xE9", "é"),
        ("\xE0", "à"),
        ("\xA0", "à"),
        ("\xE8", "è"),
        ("\xA8", "è"),
        ("\xF4", "ô"),
        ("\xB4", "ô"),
        ("\xFB", "û"),
        ("\xC3\xAA", "ê"),
        ("\xC3\xAE", "î"),
        ("\xAE", "î"),
        ("\xEE", "î"),
        ("\xEA", "ê"),
        ("\xAA", "ê"),
        ("Ã", "à"),
    ]

    for k, v in correspondance:
        text = text.replace("\xC3" + k, v).replace("\xE3" + k, v)
        text = text.replace(k, v)

    if len(removeAccent_debug(text)) != len(text) and len(text) < 50:
        fLOG("FixIssuesWithAccent", o.encode("utf8"), text.encode("utf8"))
        fLOG("FixIssuesWithAccent", o, text)
        raise ValueError("unable to deal with " +
                         str([text, [text], removeAccent_debug(text), text.encode("utf8")]))
    return text


def modify_all_blogs_list_in_place(folder=".",
                                   mainpage=os.path.join(
                                       "blog", "xd_blog.html"),
                                   outmainpage=os.path.join("blog", "xd_blog.html")):
    file = find_all_blogs_function(folder)
    file = [os.path.split(_)[-1].replace(".html", "") for _ in file]
    f = open(mainpage, "r", encoding="utf8")
    cont = f.read()
    f.close()
    trois = cont.split("//////////////////////////////////////////")
    assert len(trois) == 3
    file.sort(reverse=True)
    trois[1] = "\n" + ",\n".join(["\"%s\"" % _ for _ in file]) + "\n"
    cont = "//////////////////////////////////////////".join(trois)
    f = open(outmainpage, "w", encoding="utf8")
    f.write(cont)
    f.close()


def file_all_keywords(folder=".",
                      mainpage=os.path.join("blog", "xd_blog.html"),
                      outmainpage=os.path.join("blog", "xd_blog.html"),
                      exclude=None):
    keepfile = find_all_blogs_function(folder, exclude)
    hist = {}
    store_keywords = {}
    files = []

    for f in keepfile:
        dom = load_and_modify_xml_dom(f, None)
        meta = dom.documentElement.getElementsByTagName("meta")
        node = [_ for _ in meta if "name" in _.attributes and _.attributes[
            "name"].value == "keywords"]
        keywords = [_.strip() for _ in node[0].attributes[
            "content"].value.split(",")]
        keywords.sort()
        store_keywords[f] = keywords
        for k in keywords:
            k = k.strip()
            hist[k] = hist.get(k, 0) + 1
    res = [(v, k) for k, v in hist.items() if v > 1]
    res.sort(reverse=True)

    # tag
    f = open(mainpage, "r", encoding="utf8")
    cont = f.read()
    f.close()
    trois = cont.split("////////////###########")
    trois[1] = "\n" + ",\n".join(["[\"%s (%d)\",\"%s\"]" %
                                  (FixIssuesWithAccent(k), v, removeAccent(k)) for v, k in res]) + "\n"
    cont = "////////////###########".join(trois)

    # documents
    trois = cont.split("////////////---------------------")
    rows = []
    for k, v in res:
        files = []
        text = '"%s":' % removeAccent(v)
        for f in keepfile:
            keywords = store_keywords[f]
            if v in keywords:
                files.append(f)
        files = [os.path.split(_)[-1].replace(".html", "") for _ in files]
        files.sort(reverse=True)
        files = ['"%s"' % _ for _ in files]
        text += "[ %s ] " % ", ".join(files)
        rows.append(text)
    trois[1] = "\n" + ",\n".join([_ for _ in rows]) + "\n"

    cont = "////////////---------------------".join(trois)

    # rev keywords
    trois = cont.split("////////////+++++++++++++++++")
    rows = []
    for k, v in res:
        text = removeAccent(v)
        rows.append('"%s":"%s"' % (text, FixIssuesWithAccent(v)))
    trois[1] = "\n" + ",\n".join([_ for _ in rows]) + "\n"
    cont = "////////////+++++++++++++++++".join(trois)

    f = open(outmainpage, "w", encoding="utf8")
    f.write(cont)
    f.close()

    modify_all_blogs_list_in_place(folder, outmainpage, outmainpage)
    return store_keywords


def build_bloc_keywords(res, frequence_threshold, rootfile):
    """
    builds the keywords bloc

    @param      res                     ....
    @param      frequence_threshold     number of times a keyword needs to appear before getting the right bar
    """
    keywords = {}
    for a, b in res.items():
        for _ in b:
            keywords[_] = keywords.get(_, 0) + 1
    keywords = [(b, a) for a, b in keywords.items()]
    keywords.sort(reverse=True)
    text = []
    for a, b in keywords:
        if a >= frequence_threshold:
            s = '<p class="keywordtitle"><a href="%s_%s.html" target="_parent">%s</a> (%d)</p>' % \
                (rootfile, removeAccent(b), FixIssuesWithAccent(b), a)
            text.append(s)
    return "\n".join(text), keywords


def build_bloc_months(res, rootfile):
    """
    builds the months bloc (we assume the page name is YYYY-MM-DD-something-.html

    @param      res             list of blog per months
    @param      rootfile        files location
    """
    months = {}
    for a, b in res.items():
        month = os.path.split(a)[-1][:7]
        months[month] = months.get(month, 0) + 1
    months = [(a, str(b)) for a, b in months.items()]
    months.sort(reverse=True)
    text = []
    year = None
    for a, b in months:
        if year is not None and a[:4] != year:
            text.append('<p class="smallspace">.</p>')
        s = '<p class="monthtitle"><a href="%s_%s.html" target="_parent">%s</a> (%s)</p>' % \
            (rootfile, a, a, b)
        text.append(s)
        year = a[:4]
    months = [(b, a) for a, b in months]
    return "\n".join(text), months


def replace_xml_in_template_using_dom_dirty(dom, node, newvalue):
    xmltext = node.toxml()
    allxml = dom.documentElement.toxml()
    pos = allxml.find(xmltext)
    if pos == -1:
        raise ValueError("unable to replace")
    allxml = allxml.replace(xmltext, newvalue)
    res = xml.dom.minidom.parseString(allxml)
    return res


def get_node_div(template, cl):
    sidebar = template.documentElement.getElementsByTagName("div")
    sidebar = [_ for _ in sidebar if "class" in _.attributes]
    sidebar = [_ for _ in sidebar if _.attributes["class"].value == cl]
    if len(sidebar) != 1:
        raise ValueError("issue with HTML format: " +
                         cl + ", " + str(len(sidebar)))
    sidebar = sidebar[0]
    return sidebar


def generate_html_article(res,
                          templateFile,
                          toFolder,
                          overwrite=False,
                          aggregatedFile=None,
                          maxAggregrate=15,
                          keywordsText=None,
                          otherLayer=None):

    fileToReturn = []

    if not os.path.exists(toFolder):
        raise FileNotFoundError("not found " + toFolder)

    # group files or not
    toprocess = []
    if aggregatedFile is not None:
        counter = 0
        stackFile = []

        for file in sorted(res, reverse=True):
            stackFile.append(file)
            if len(stackFile) == maxAggregrate:
                fileOutName = "%s_%04d.html" % (aggregatedFile.replace(".html", ""), counter) if counter > 0 \
                    else aggregatedFile
                fileOutName = os.path.join(toFolder, fileOutName)
                stackFile.sort(reverse=True)
                toprocess.append((stackFile, fileOutName))
                counter += len(stackFile)
                stackFile = []

        if len(stackFile) > 0:
            fileOutName = "%s_%04d.html" % (aggregatedFile.replace(".html", ""), counter) if counter > 0 \
                else aggregatedFile
            fileOutName = os.path.join(toFolder, fileOutName)
            stackFile.sort(reverse=True)
            toprocess.append((stackFile, fileOutName))
    else:
        # we process all files, each of them gives a file
        for file in sorted(res, reverse=True):
            filename = os.path.split(file)[-1].replace(".html", "_nojs.html")
            filename = os.path.join(toFolder, filename)
            toprocess.append(([file], filename))

    # updating the sidebar
    template = load_and_modify_xml_dom(templateFile, None, False)
    templateText = template.documentElement.toxml()
    title_to_rep = template.documentElement.getElementsByTagName("title")[
        0].toxml()

    # all files to process are now in the list
    for indexProcess, couple in enumerate(toprocess):
        files, filename = couple
        stackContent = []
        scripthtml = ""
        replacetitle = None

        for file in files:
            dom = load_and_modify_xml_dom(file, None)
            date = os.path.split(file)[-1][:10]

            title = dom.documentElement.getElementsByTagName("title")[
                0].toxml()
            if "XD blog" in title:
                raise ValueError("a blog contains a bad title: " + file)
            if len(files) == 1:
                # in that case, we want to change the page title
                replacetitle = title

            title = title.replace("title>", "h2>")
            link = '<a href="%s_nojs.html"><b>%s</b></a>' % (date, date)
            title = title.replace("<h2>", "<h2>" + link + " ")

            scripts = dom.documentElement.getElementsByTagName("script")
            if len(scripts) > 1:
                scr = [""] + [_.toxml() for _ in scripts]
                scripthtml += "\n".join(scr)

            b = dom.documentElement.getElementsByTagName("body")[0]
            body = b.toxml()

            body = body[6:]
            body = body[:-7]

            if len(files) > 1 and '<!-- CUT PAGE HERE -->' in body:
                # here we deal with shortcuts except if we process a single
                # document
                body = body.split('<!-- CUT PAGE HERE -->')[0]
                body += "<br />" + \
                    '<a href="%s_nojs.html">%s</a>' % (date, "more...")

            if len(body.strip()) == 0:
                raise ValueError("empty body for " + file)
            stackContent.append(title + "\n" + body)
            keywords = res[file]

        # we
        uniqueKeys = [_ for _ in set(keywords) if not _.startswith("~")]
        uniqueKeys.sort()
        keystext = ", ".join(uniqueKeys)

        nextPage = ""
        if indexProcess > 0:
            nextPage += '<a href="%s"><i>&lt;--</i></a> ' % (
                os.path.split(toprocess[indexProcess - 1][1])[-1])
        if indexProcess < len(toprocess) - 1:
            nextPage += '<a href="%s"><i>--&gt;</i></a> ' % (
                os.path.split(toprocess[indexProcess + 1][1])[-1])

        if keywordsText is not None:
            keystext = keywordsText

        # inside

        post = templateText.replace(
            "<!-- article here -->", "\n".join(stackContent))
        post = post.replace(
            '<a href="xd_blog_nojs_DDD.html"><i>suite</i></a>', nextPage)
        post = post.replace("<!-- javascript here -->", scripthtml)
        post = post.replace("<!-- article keywords -->", keystext)
        post = post.replace("### KEYWORDS ###", keystext)
        post = post.replace("### keywords ###", keystext)

        if False:
            olayer = '<p class="keywordtitle"><a href="xd_blog.html?date=%s">Other Layer</a></p>' % date \
                if otherLayer is None else \
                '<p class="keywordtitle"><a href="%s">Other Layer</a></p>' % otherLayer
            post = post.replace("<!-- other layer -->", olayer)
            # it does not work (pages too big)

        post = '<?xml version="1.0" encoding="utf-8"?>\n' + post
        post = post.replace('type="text/javascript"/>',
                            'type="text/javascript"></script>')

        post = FixIssuesWithAccent(post)

        if replacetitle is not None:
            # there was only one document, we replace it
            post = post.replace(title_to_rep, replacetitle)

        # we save the results

        if os.path.exists(filename):
            try:
                f = open(filename, "r", encoding="utf8")
                hist = f.read()
                f.close()
            except UnicodeDecodeError as e:
                fLOG("issue with file ", filename)
                content = open(filename, "r").read()
                fLOG(content[170:])
                raise e
        else:
            hist = ""

        if post != hist or overwrite:
            if "\xC3" in post:
                #raise Exception("forbidden character ")
                pass
            if not overwrite:
                fLOG("  writing ", filename)
            if "### keywords ###" in post.lower():
                raise Exception(
                    "unable to release that document with this string ### KEYWORDS ###,\nkeywords should be " + str(keystext))
            f = open(filename, "w", encoding="utf8")
            f.write(post)
            f.close()
            fileToReturn.append(filename)

    return fileToReturn


def build_process_all_pages(res,
                            keywordsHTML="frame_keywords.html",
                            siteFolder="../site/blog",
                            xd_blog_template_nojs=os.path.join(
                                "blog", "xd_blog_template_nojs.html"),
                            xd_blog_nojs="xd_blog_nojs.html",
                            frequence_keywords=3,
                            monthsHTML="frame_months.html"
                            ):
    """
    @param      res                         output from function file_all_keywords
    @param      keywordsHTML                html template for the keywords
    @param      siteFolder                  folder the blog (the one to be published)
    @param      xd_blog_template_nojs       template for blog (static text, less javascript)
    @param      xd_blog_nojs                main page (static text, less javascript)
    @param      frequence_keywords          there won't be any page for a keyword whose frequency is below that threshold
    @param      monthsHTML                  html template for the months
    @return                                 all created pages
    """

    add = []

    fLOG("processing keywords")
    htmlkey, keywords = build_bloc_keywords(
        res, frequence_keywords, "xd_blog_key")
    if keywordsHTML is not None:
        file = os.path.join(siteFolder, keywordsHTML)
        fLOG("writing ", file)
        f = open(file, "w", encoding="utf8")
        f.write("""<?xml version="1.0" encoding="utf-8"?>\n""")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write(
            """<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>\n""")
        f.write("""<link href="pMenu.css" rel="stylesheet" type="text/css"/>\n""")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("""<div class="sidebarfull">\n""")
        f.write("""<p class="keywordtitle"><b>Keywords</b></p>\n""")
        f.write(htmlkey)
        f.write("\n</div>\n")
        f.write("\n</body></html>\n")
        f.close()
        add.append(file)

    fLOG("processing months")
    htmlkeym, monthsp = build_bloc_months(res, "xd_blog_month")
    if monthsHTML is not None:
        file = os.path.join(siteFolder, monthsHTML)
        fLOG("writing ", file)
        f = open(file, "w", encoding="utf8")
        f.write("""<?xml version="1.0" encoding="utf-8"?>\n""")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write(
            """<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>\n""")
        f.write("""<link href="pMenu.css" rel="stylesheet" type="text/css"/>\n""")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("""<div class="sidebarfullleft">\n<hr />\n""")
        f.write("""<p class="monthtitle"><b>Months</b></p>\n""")
        f.write(htmlkeym)
        f.write("\n</div>\n")
        f.write("\n</body></html>\n")
        f.close()
        add.append(file)

    # build keyword pages
    fLOG("building aggregated page for keywords")
    add += generate_html_article(
        res,
        xd_blog_template_nojs,
        siteFolder,
        True,
        xd_blog_nojs,
        keywordsText="",
        otherLayer="xd_blog.html")

    # process all pages for each keyword)
    for a, b in keywords:
        fLOG("building page for keyword", FixIssuesWithAccent(b))
        bb = removeAccent(b)
        tempres = {}
        for k, v in res.items():
            if b in v:
                tempres[k] = ""
        add += generate_html_article(
            tempres,
            xd_blog_template_nojs,
            siteFolder,
            True,
            "xd_blog_key_%s.html" % bb,
            keywordsText=FixIssuesWithAccent(b),
            otherLayer="xd_blog.html?tag=%s" % FixIssuesWithAccent(b))

    # build months pages
    fLOG("building aggregated page for months")
    add += generate_html_article(
        res,
        xd_blog_template_nojs,
        siteFolder,
        True,
        xd_blog_nojs,
        keywordsText="",
        otherLayer="xd_blog.html")

    # process all pages for each months)
    for a, b in monthsp:
        fLOG("building page for months", b)
        bb = removeAccent(b)
        tempres = {}
        for k, v in res.items():
            if os.path.split(k)[-1].startswith(b):
                tempres[k] = ""
        add += generate_html_article(
            tempres,
            xd_blog_template_nojs,
            siteFolder,
            True,
            "xd_blog_month_%s.html" % bb,
            keywordsText=FixIssuesWithAccent(b),
            otherLayer="xd_blog.html?tag=%s" % FixIssuesWithAccent(b))

    # build all pages (one per blog)
    fLOG("building all pages")
    add += generate_html_article(
        res,
        xd_blog_template_nojs,
        siteFolder,
        overwrite=True,
        otherLayer=None)
    return add
