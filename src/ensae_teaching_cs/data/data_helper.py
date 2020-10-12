"""
@file
@brief Helpers to get data including in the module itself.
"""
import os
from pyquickhelper.filehelper import unzip_files


def any_local_file(name, subfolder, local=True, cache_folder=".",
                   filename=True, unzip=False, encoding=None):
    """
    Returns a local data file, reads its content or returns its content.

    @param          name            file to download
    @param          subfolder       sub folder
    @param          local           local data or web
    @param          cache_folder    where to cache the data if downloaded a second time
    @param          filename        return the filename (True) or the content (False)
    @param          unzip           unzip as well
    @param          encoding        encoding
    @return                         text content (str)
    """
    if local:
        this = os.path.abspath(os.path.dirname(__file__))
        this = os.path.join(this, subfolder, name)
        if not os.path.exists(this):
            raise FileNotFoundError(this)
    else:
        import pyensae.datasource
        if not unzip and name.endswith(".zip"):
            raise ValueError(
                "The file will be unzipped anyway: {0}".format(name))
        this = pyensae.datasource.download_data(name, whereTo=cache_folder)
        unzip = False
    if unzip:
        this = unzip_files(this, where_to=cache_folder)
    if filename:
        return this
    else:
        if isinstance(this, list):
            if len(this) > 1:
                raise ValueError(
                    "more than one file for: {0}\n{1}".format(name, this))
            else:
                this = this[0]
        if os.path.splitext(this)[-1] in (".zip", ".gz", ".tar", ".7z"):
            raise ValueError("Cannot read file as text: {0}".format(this))
        with open(this, "r", encoding=encoding) as f:
            return f.read()
