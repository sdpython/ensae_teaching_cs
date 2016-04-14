"""
@file
@brief Convert a short latex script into an image
"""
import os
import shutil
import sys
from PIL import Image
from pyquickhelper.loghelper import run_cmd


def convert_short_latex_into_png(latex, temp_folder=".", fLOG=print,
                                 miktex=r"C:\Program Files\MiKTeX 2.9\miktex\bin\x64",
                                 final_name=None):
    """
    Convert a short latex script into an image.

    @param      latex           latex equation
    @param      temp_folder     temp_folder  (where temporary files will be placed)
    @param      fLOG            logging function
    @param      miktex          miktex location
    @param      final_name      if not None, copy the image at this location using this name
    @return                     a location to the image (it should be copied), and its size

    You should not call the function twice at the same in the same folder.

    @warning The function ends the program if there was a failure. Something is missing on the command line.
    """
    if not os.path.exists(miktex):
        raise FileNotFoundError("unable to find miktex")

    if sys.platform.startswith("win"):
        htlatex = os.path.join(miktex, "htlatex.exe")
        if not os.path.exists(htlatex):
            raise FileNotFoundError("unable to find htlatex")
    else:
        htlatex = os.path.join(miktex, "htlatex")

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    eq = os.path.join(temp_folder, "eq.tex")
    with open(eq, "w") as f:
        f.write(r"""\documentclass[12pt]{article}
                \pagestyle{empty}
                \begin{document}
                $$
                %s
                $$
                \end{document}""".replace("                ", "") % latex.strip("\n\r "))

    cmd = '"' + htlatex + '" eq.tex "html, graphics-300" "" "" "--interaction=nonstopmode"'
    cwd = os.getcwd()
    os.chdir(temp_folder)
    out, err = run_cmd(cmd, wait=True)
    os.chdir(cwd)

    if "FAILED" in err:
        raise Exception(
            "it failed\n-----\n{0}\n----------\n{1}".format(out, err))
    img = os.path.join(temp_folder, "eq0x.png")
    if not os.path.exists(img):
        with open(os.path.join(temp_folder, "eq.log"), "r") as f:
            log = f.read()
        raise FileNotFoundError("the compilation did not work\n" + log)

    if final_name is not None:
        # size reduction
        im = Image.open(img)
        shutil.copy(img, final_name)
        return final_name, im.size
    else:
        im = Image.open(img)
        return img, im.size
