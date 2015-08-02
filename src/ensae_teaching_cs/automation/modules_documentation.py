"""
@file
@brief Customize a Windows Setup for these teachings
"""

import os
import shutil
import pandas

from pymyinstall.packaged import ensae_fullset
from pyquickhelper import df2rst


def rst_table_modules():
    """
    produces a table with all modules recommended to do machine learning

    @return         string
    """
    mod = ensae_fullset()
    mod.sort()
    df = pandas.DataFrame(_.as_dict() for _ in mod)
    df = df[["usage", "name", "kind", "version", "purpose"]]
    return df2rst(df)
