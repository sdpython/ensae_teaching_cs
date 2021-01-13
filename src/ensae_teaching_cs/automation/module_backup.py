"""
@file
@brief backup the list of modules
"""
from pyquickhelper.loghelper import get_password
from pyquickhelper.filehelper import TransferFTP


def ftp_list_modules(ftp_location="/home/ftpuser/ftp/web/enseignement/setup",
                     http_location="http://www.xavierdupre.fr/enseignement/setup",
                     filename="index_modules_list.html",
                     ftps='SFTP'):
    """
    Updates the list of backuped modules assuming they are stored on a FTP website.
    It gets the list of wheels in a folder and creates a HTML pages.
    It then uploads the final pages.

    @param  ftp_location    location on the website
    @param  http_location   same location but on http protocol
    @param  filename        name of the file to produce
    @return                 list of modules

    The module uses *keyring* to retrieve the credentials.
    You can set them up with:

    ::

        from pyquickhelper.loghelper import get_password
        get_password("ftp_list_modules", "ensae_teaching_cs2,site", "...")
        get_password("ftp_list_modules", "ensae_teaching_cs2,login", "...")
        get_password("ftp_list_modules", "ensae_teaching_cs2,password", "...")
    """
    ftp_site = get_password(
        "ftp_list_modules", "ensae_teaching_cs2,site")
    login = get_password(
        "ftp_list_modules", "ensae_teaching_cs2,login")
    password = get_password(
        "ftp_list_modules", "ensae_teaching_cs2,password")

    if not ftp_site:
        raise ValueError("ftp_site is empty, some missing keyring?")
    if not login:
        raise ValueError("login is empty")
    if not password:
        raise ValueError("password is empty")

    ftp = TransferFTP(ftp_site, login, password, ftps=ftps)
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
