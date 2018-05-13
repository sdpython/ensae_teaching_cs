# -*- coding: utf-8 -*-
"""
@file
@brief  Copy files
"""
import os
import shutil
import datetime
from pyquickhelper.loghelper import fLOG
from .clean_python_script_before_exporting_outside import cleanFileFromtohtmlreplace
from .utils_file import checksum_md5
from .latex_svg_gif import replace_file


class FileToCopy:

    def __init__(self, filename, size, date, mdate, checksum):
        """constructor"""
        self.filename = filename
        self.size = size
        self.date = date
        self.mdate = mdate    # modification date
        self.checksum = checksum
        if date is not None and not isinstance(self.date, datetime.datetime):
            raise ValueError("mismatch for date (%s) and file %s" %
                             (str(type(date)), filename))
        if mdate is not None and not isinstance(self.mdate, datetime.datetime):
            raise ValueError("mismatch for mdate (%s) and file %s" %
                             (str(type(mdate)), filename))
        if not isinstance(size, int):
            raise ValueError("mismatch for size (%s) and file %s" %
                             (str(type(size)), filename))
        if checksum is not None and not isinstance(checksum, str):
            raise ValueError("mismatch for checksum (%s) and file %s" %
                             (str(type(checksum)), filename))
        if date is not None and mdate is not None:
            if mdate > date:
                raise ValueError(
                    "expecting mdate <= date for file " + filename)

    def __str__(self):
        return "File[name=%s, size=%d (%s), mdate=%s (%s), date=%s (%s), md5=%s (%s)]" % \
            (self.filename,
             self.size, str(type(self.size)),
             str(self.mdate), str(type(self.mdate)),
             str(self.date), str(type(self.date)),
             self.checksum, str(type(self.checksum)))

    def set_date(self, date):
        self.date = date
        if not isinstance(self.date, datetime.datetime):
            raise ValueError("mismatch for date (%s) and file %s" %
                             (str(type(date)), self.filename))

    def set_mdate(self, mdate):
        self.mdate = mdate
        if not isinstance(self.mdate, datetime.datetime):
            raise ValueError("mismatch for date (%s) and file %s" %
                             (str(type(mdate)), self.filename))

    def set_md5(self, checksum):
        self.checksum = checksum
        if not isinstance(checksum, str):
            raise ValueError("mismatch for checksum (%s) and file %s" %
                             (str(type(checksum)), self.filename))


class CopyFileForFtp:
    """
    this classes maintains a list of files
    and does some verifications in order to check if a file
    was modified or not (if yes, then it will be updated to the website)
    """
    @staticmethod
    def convert_st_date_to_datetime(t):
        if isinstance(t, str):
            if "." in t:
                return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f")
            else:
                return datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
        else:
            return datetime.datetime.fromtimestamp(t)

    def __init__(self, file,
                 logfunction=fLOG,
                 bloggiflatex="blog/giflatex/",
                 giflatex="giflatex",
                 giflatextemp="giflatex/temp",
                 specificTrigger=False):
        """constructor"""

        self.copyFiles = {}
        self.fileKeep = file
        self.LOG = logfunction
        self.bloggiflatex = bloggiflatex
        self.giflatex = giflatex
        self.giflatextemp = giflatextemp
        self.specificTrigger = specificTrigger

        if os.path.exists(self.fileKeep):
            f = open(self.fileKeep, "r")
            for _ in f.readlines():
                spl = _.strip("\r\n ").split("\t")
                try:
                    if len(spl) >= 2:
                        a, b = spl[:2]
                        obj = FileToCopy(a, int(b), None, None, None)
                        if len(spl) > 2 and len(spl[2]) > 0:
                            obj.set_date(
                                CopyFileForFtp.convert_st_date_to_datetime(spl[2]))
                        if len(spl) > 3 and len(spl[3]) > 0:
                            obj.set_mdate(
                                CopyFileForFtp.convert_st_date_to_datetime(spl[3]))
                        if len(spl) > 4 and len(spl[4]) > 0:
                            obj.set_md5(spl[4])
                        self.copyFiles[a] = obj
                    else:
                        raise ValueError(
                            "expecting a filename and a date on this line: " + _)
                except Exception as e:
                    fLOG("issue with line", _, spl)
                    raise e

            f.close()

        # contains all file to update
        self.modifiedFile = []

    def save_dates(self, checkfile=None):
        """
        save the status of the copy
        @param      checkfile       check the status for file checkfile
        """
        if checkfile is None:
            checkfile = []
        rows = []
        for k in sorted(self.copyFiles):
            obj = self.copyFiles[k]
            da = "" if obj.date is None else str(obj.date)
            mda = "" if obj.mdate is None else str(obj.mdate)
            sum5 = "" if obj.checksum is None else str(obj.checksum)

            if k in checkfile and len(da) == 0:
                raise ValueError(
                    "there should be a date for file " + k + "\n" + str(obj))
            if k in checkfile and len(mda) == 0:
                raise ValueError(
                    "there should be a mdate for file " + k + "\n" + str(obj))
            if k in checkfile and len(sum5) <= 10:
                raise ValueError(
                    "there should be a checksum( for file " + k + "\n" + str(obj))

            values = [k, str(obj.size), da, mda, sum5]
            sval = "%s\n" % "\t".join(values)
            if "\tNone" in sval:
                raise AssertionError(
                    "this case should happen " + sval + "\n" + str(obj))

            rows.append(sval)

        f = open(self.fileKeep, "w")
        for r in rows:
            f.write(r)
        f.close()

    def has_been_modified_and_reason(self, file):
        """
        returns True, reason if a file was modified or False,None if not
        @param      file        filename
        @return                 True,reason or False,None
        """
        res = True
        reason = None

        if file not in self.copyFiles:
            reason = "new"
            res = True
        else:
            obj = self.copyFiles[file]
            st = os.stat(file)
            if st.st_size != obj.size:
                reason = "size %s != old size %s" % (
                    str(st.st_size), str(obj.size))
                res = True
            else:
                l_ = obj.mdate
                _m = st.st_mtime
                d = CopyFileForFtp.convert_st_date_to_datetime(_m)
                if d != l_:
                    # les dates sont différentes mais les fichiers peuvent être
                    # différents
                    if obj.checksum is not None:
                        ch = checksum_md5(file)
                        if ch != obj.checksum:
                            reason = "date/md5 %s != old date %s  md5 %s != %s" % (
                                str(l_), str(d), obj.checksum, ch)
                            res = True
                        else:
                            res = False
                    else:
                        # on ne peut pas savoir, dans le doute, on s'abstient
                        res = False
                else:
                    # mda.... mais pas sûr (la date n'a pas changé)
                    res = False

        if res:
            self.modifiedFile.append((file, reason))
        return res, reason

    def add_if_modified(self, file):
        """
        add a file to self.modifiedList if it was modified
        @param      file    filename
        @return             True or False
        """
        res, reason = self.has_been_modified_and_reason(file)
        if res:
            memo = [_ for _ in self.modifiedFile if _[0] == file]
            if len(memo) == 0:
                # not already added
                self.modifiedFile.append((file, reason))
        return res

    def update_copied_file(self, file):
        """
        update the file in copyFiles (before saving), update all field
        @param      file        filename
        @return                 file object
        """
        st = os.stat(file)
        size = st.st_size
        mdate = CopyFileForFtp.convert_st_date_to_datetime(st.st_mtime)
        date = datetime.datetime.now()
        md = checksum_md5(file)
        obj = FileToCopy(file, size, date, mdate, md)
        self.copyFiles[file] = obj
        return obj

    def copy_file(self, file, to, doFTP=True, doClean=False, to_is_a_file=False):
        """
        Processes a file copy.
        @param      file            file to copy
        @param      to              destination (folder)
        @param      doFTP           if True, does some latex modifications (creates an image)
        @param      doClean         if True, does some cleaning before the copy
                                    (for script in pyhome having section such as the one in tableformula.py)
        @param      to_is_a_file    it means to is a file, not a folder
        """
        if doClean and doFTP:
            raise AssertionError(
                "this case is not meant to happen, doClean and doFTP, set up at the same time")
        if len(to) == 0:
            raise ValueError("an empty folder is not allowed for parameter to")

        folder = to
        if not os.path.exists(folder):
            ffff, last = os.path.split(to)
            if to_is_a_file:
                folder = ffff
            elif "." in last:
                raise ValueError("are you sure to is not a file :" + to + "?")

            if not os.path.exists(folder):
                self.LOG("creating folder ", folder)
                os.makedirs(folder)

        if doFTP:
            if file not in self.copyFiles or \
               os.stat(file).st_size != self.copyFiles[file].size:

                # some exception for latex
                if self.specificTrigger and "2013-02-04" not in file and \
                        file.endswith(".html") and "-" in file:
                    fLOG("   latex exception for: ", file)
                    replace_file(file, file, self.bloggiflatex,
                                 self.giflatex, self.LOG, self.giflatextemp)

                if not os.path.exists(to):
                    self.LOG("creating directory ", to)
                    os.mkdir(to)

                self.LOG("copy of ", file, " \t to ", to)
                reason = "new" if file not in self.copyFiles else \
                    ("new size %s != old size %s" % (str(os.stat(file).st_size),
                                                     str(self.copyFiles[file].size)))

                try:
                    shutil.copy(file, to)
                    self.modifiedFile.append((file, reason))
                    return to

                except Exception as e:
                    self.LOG("issue with ", file, " copy to ", to)
                    self.LOG("message d'erreur ", e)
            return to
        else:
            try:
                shutil.copy(file, to)
                if not os.path.isfile(to):
                    to = os.path.join(to, os.path.split(file)[-1])
                fLOG("copy ", file, " as ", to)
            except Exception as e:
                self.LOG("issue with ", file, " copy to ", to)
                self.LOG("message d'erreur ", e)

            if doClean:
                f = open(to, "r")
                content = f.read()
                f.close()

                newcontent = cleanFileFromtohtmlreplace(content)

                if newcontent != content:
                    fLOG("    cleaning python script ", to)
                    f = open(to, "w")
                    f.write(newcontent)
                    f.close()

            return to

    def copy_file_ext(self, file, exte, to, doFTP=True, doClean=False):
        """
        @see me copy_file
        """
        if not os.path.exists(file):
            raise FileNotFoundError(file)
        fi = os.listdir(file)
        for f in fi:
            if not os.path.isfile(file + "/" + f):
                continue
            ext = os.path.splitext(f)[1]
            if exte is None or ext[1:] == exte:
                self.copy_file(file + "/" + f, to, doFTP, doClean)

    def copy_file_contains(self, file, pattern, to, doFTP=True, doClean=False):
        """
        @see me copy_file
        """
        fi = os.listdir(file)
        for f in fi:
            if not os.path.isfile(file + "/" + f):
                continue
            if pattern in f:
                self.copy_file(file + "/" + f, to, doFTP, doClean)
