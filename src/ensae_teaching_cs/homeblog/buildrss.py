# coding:utf-8
"""
@file
@brief About RSS
"""
import datetime
import os
import re
from pyquickhelper.loghelper import fLOG
from .filefunction import find_all_blogs_function


modelForARSSFeed = """<rss version="2.0">
                        <channel>
                            <title>XD blog</title>
                            <link>http://www.xavierdupre.fr/blog/xd_blog_nojs.html</link>
                            <description>new posts from XD blog</description>
                            """.replace("                        ", "")

modelForARSSRow = """
        <item>
            <title>%s</title>
            <link>http://www.xavierdupre.fr/blog/%s_nojs.html</link>
            <guid isPermaLink="true">http://www.xavierdupre.fr/blog/%s_nojs.html</guid>
            <description>%s</description>
            <pubDate>%s</pubDate>
        </item>"""

modelForARSSChannel = """\n</channel>\n</rss>\n"""


def file_build_rss(folder=".", outfile="blog/xdbrss.xml", now=datetime.datetime.now(),
                   model_feed=modelForARSSFeed, model_row=modelForARSSRow,
                   model_channel=modelForARSSChannel, months_delay=6):
    """
    Build a RSS file, the function keeps the blog post (HTML format) from the last month.
    If a post contains one the two following string:

    ::

        <!-- SUMMARY BEGINS -->
        <!-- SUMMARY ENDS -->

    The summary will only contains the part included in those two comments.


    @param  folder          folder where the blog post can be found
    @param  outfile         final file to produce
    @param  now             date to use as a final date, only blog post between one month now and now will be kept
    @param  model_feed      see model_channel
    @param  model_row       see model_row
    @param  model_channel   the part related to a post in the rss stream is composed
                            by the concatenation of the three stream:

                            ::

                                model_feed
                                model_row
                                model_channel

                            You should see the default value to see how you can replace them.
    @param  months_delay    keep mails written a couple of months ago: *month_delay* months
    @return                 2-uple: outfile and the list of kept blog post (the last month)
    """

    now -= datetime.timedelta(days=months_delay * 30)
    fLOG("now - month ", now)
    file = find_all_blogs_function(folder)
    nbfile = len(file)
    exp = re.compile('<meta +name=\\"description\\" +content=\\"(.*?)\\" */>')
    expt = re.compile('<title>(.*?)</title>')

    keepfiles = []
    rss = []
    for f in file:
        temp = os.path.split(f)[-1].lower().replace(".html", "")
        day = datetime.datetime(int(temp[:4]), int(temp[5:7]), int(temp[8:10]))
        if day > now:
            keepfiles.append(f)

            ff = open(f, "r", encoding="utf8")
            t = ff.read().replace("\n", " ").replace("\r", " ")
            ff.close()
            check_encoding(f)

            summary = exp.search(t)
            title = expt.search(t)

            if not title:
                raise ValueError("unable to find title in " + f)
            fLOG("getting summary for ", f)

            title = title.groups()[0]
            summary = None if summary is None else summary.groups()[0]
            adddots = False

            if summary is None or len(summary) == 0:
                if "<!-- SUMMARY BEGINS -->" in t and "<!-- SUMMARY ENDS -->" in t:
                    p0 = t.find("<!-- SUMMARY BEGINS -->")
                    p1 = t.find("<!-- SUMMARY ENDS -->")
                    summary = t[
                        p0 + len("<!-- SUMMARY BEGINS -->"):p1].strip(" \n\r\t")
                    summary = summary.replace("<", "&lt;")
                    summary = summary.replace(">", "&gt;")
                    adddots = True

                if summary is None or len(summary) == 0:
                    p0 = t.find("<body>")
                    p1 = t.find("</body>")
                    summary = t[p0 + len("<body>"):p1].strip(" \n\r\t")
                    summary = summary.replace("<", "&lt;")
                    summary = summary.replace(">", "&gt;")

                if summary is None or len(summary) == 0:
                    raise ValueError("summary is empty for blog " + f)

            summary = re.sub(r"\s+", " ", summary)
            rss.append((day, f, summary, temp, title))

    rows = ["<?xml version=\"1.0\" encoding=\"utf-8\"?>"]
    rows.append(modelForARSSFeed)
    if len(rss) == 0:
        raise Exception(
            "No found file in '{0}' (raw count {1}).".format(folder, nbfile))

    rss.sort(reverse=True)
    for day, f, summary, short, title in rss:
        if adddots and not summary.endswith("..."):
            summary += " suite..." if not summary.endswith(
                ".") else " suite..."

        row = modelForARSSRow % (title, short, short, summary, str(day))
        rows.append(row)

    rows.append(modelForARSSChannel)
    content = "\n".join(rows)
    rssf = open(outfile, "w", encoding='utf-8')
    rssf.write(content)
    rssf.close()

    return outfile, keepfiles


def check_encoding(file):
    """
    check the encoding of a file (ASCII here),
    read the file, it does not return anything
    @param      file        file to check
    """
    f = open(file, "r")
    try:
        f.read()
    except Exception as e:
        size = os.stat(file).st_size
        raise Exception(
            "issue with file (size {1})\n  File \"{0}\", line 1".format(file, size)) from e
    f.close()
