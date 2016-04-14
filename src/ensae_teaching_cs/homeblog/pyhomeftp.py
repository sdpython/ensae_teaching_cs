"""
@file
@brief provides some functionalities to upload file to a website

.. deprecated:: 0.8
"""
from ftplib import FTP
import os
from pyquickhelper.loghelper import fLOG


class pyhomeFTP (FTP):
    """
    Old version to upload file on a FTP web site
    """
    errorNoDirectory = "Can't change directory"

    def __init__(self, site, login, password):
        """
        constructor
        """
        FTP.__init__(self, site, login, password)

    def privatelogin(self):
        fLOG("connecting")
        FTP.login(self)

    def RunCommand(self, command, *args):
        try:
            t = command(self, *args)
            if command == FTP.pwd or command == FTP.dir:
                return t
            elif command != FTP.cwd:
                fLOG("    ** run ", str(command), str(args))
            return True
        except Exception as e:
            if pyhomeFTP.errorNoDirectory in str(e):
                raise e
            fLOG(e)
            fLOG("    ** run exc ", str(command), str(args))
            self.privatelogin()
            command(self, *args)
            fLOG("    ** run ", str(command), str(args))
            return False

    def printlist(self):
        return self.RunCommand(FTP.retrlines, 'LIST')

    def close(self):
        fLOG("disconnecting")
        FTP.disconnect(self)

    def mkd(self, path):
        return self.RunCommand(FTP.mkd, path)

    def cwd(self, path, create=False):
        try:
            self.RunCommand(FTP.cwd, path)
        except Exception as e:
            if create and pyhomeFTP.errorNoDirectory in str(e):
                fLOG("** creating directory ", path)
                self.mkd(path)
                self.cwd(path, create)
            else:
                raise e

    def pwd(self):
        return self.RunCommand(FTP.pwd)

    def dir(self, path='.'):
        return self.RunCommand(FTP.dir, path)

    def transfer(self, file, to, debug=False):
        """
        transfers a file
        @param      file        file
        @param      to          destination
        @param      debug       if True, displays more information
        @return                 status
        """
        path = to.split("/")
        path = [_ for _ in path if len(_) > 0]
        temp = os.path.split(file)[-1]
        fLOG("-- upload ", temp, "to", to)
        if debug:
            fLOG("    -- path", path)
            fLOG("    -- pwd", self.pwd())
        for p in path:
            if debug:
                fLOG("    -- cwd", p)
            self.cwd(p, True)
        if debug:
            fLOG("    -- transferring", file)
        with open(file, "rb") as f:
            r = self.RunCommand(FTP.storbinary, 'STOR ' + temp, f)
        for p in path:
            if debug:
                fLOG("    -- cwd", "..")
            self.cwd("..")
        return r
