"""
@file
@brief backup the list of modules
"""
import os
from pyquickhelper.filehelper import TransferFTP


def ftp_list_modules(ftp_site="CS_FTPSITE",
                     login="CS_FTPLOGIN",
                     password="CS_FTPPASSWORD",
                     ftp_location="/www/htdocs/enseignement/setup",
                     http_location="http://www.xavierdupre.fr/enseignement/setup",
                     filename="index_modules_list.html"):
    """
    Update the list of backuped modules assuming they are stored on a FTP website.
    It gets the list of wheels in a folder and creates a HTML pages.
    It then uploads the final pages

    @param  ftp_site        site ftp (or environment variable which contains it)
    @param  login           login (or environment variable which contains it)
    @param  password        password (or environment variable which contains it)
    @param  ftp_location    location on the website
    @param  http_location   same location but on http protocol
    @return                 list of modules
    """
    ftp_site = os.environ.get(ftp_site, ftp_site)
    login = os.environ.get(login, login)
    password = os.environ.get(password, password)
    ftp_site = os.environ.get(ftp_site, ftp_site)

    ftp = TransferFTP(ftp_site, login, password)
    res = ftp.ls(ftp_location)

    rows = ["<html><body><h1>storage for unit test</h1>\n<ul>"]
    ret = []
    for i, v in enumerate(sorted(_["name"] for _ in res)):
        if v in ('.', '..'):
            continue
        ret.append(v)
        line = '<li>{1} - <a href="{2}/{0}">{0}</a></li>'.format(
            v, i, http_location)
        rows.append(line)
    rows.append("</ul></body></html>")

    content = "\n".join(rows)
    bstr = content.encode('ascii')
    ftp.transfer(bstr, ftp_location + "/", filename)

    ftp.close()

    return ret
