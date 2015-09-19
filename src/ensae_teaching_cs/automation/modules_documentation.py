"""
@file
@brief Customize a Windows Setup for these teachings
"""

import pandas

from pymyinstall.packaged import ensae_fullset
try:
    from pymyinstall.packaged import classifiers2string
except ImportError as e :
    import pymyinstall
    raise ImportError("unable to import classifiers2string from {}".format(pymyinstall.__file__)) from e
from pyquickhelper import df2rst


def rst_table_modules():
    """
    produces a table with all modules recommended to do machine learning

    @return         string
    """
    mod = ensae_fullset()
    mod.sort()
    df = pandas.DataFrame(_.as_dict(rst_link=True) for _ in mod)
    df = df[["usage", "rst_link", "kind", "version",
             "license", "purpose", "classifier"]]
    df["classifier"] = df.apply(lambda row: classifiers2string(row["classifier"]), axis=1)
    df.columns = ["usage", "name", "kind", "version",
                  "license", "purpose", "classifier"]
    return df2rst(df)
