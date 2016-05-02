"""
@brief      test log(time=6s)
"""


import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

try:
    from pyPdf import PdfFileReader
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyPdf")))
    if path not in sys.path:
        sys.path.append(path)
    from pyPdf import PdfFileReader


from pyquickhelper.loghelper import fLOG
from src.ensae_teaching_cs.helpers.pypdf_helper import pdf_read_content


class TestModulesPdfReader(unittest.TestCase):

    def test_read_pdf(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        pdffile = os.path.join(os.path.split(__file__)[
                               0], "data", "1305.0445.pdf")
        assert os.path.exists(pdffile)

        with open(pdffile, "rb") as f:
            input1 = PdfFileReader(f)
            title = input1.getDocumentInfo().title
            traw = input1.getDocumentInfo().title_raw
            npage = input1.getNumPages()
            fLOG("title", title, "*", traw)
            fLOG("nb pages", npage)

            page = input1.getPage(0)
            cont = page.getContents()
            fLOG("cont", cont)
            for obj in page:
                fLOG("obj", obj, "*", obj.title())
            annots = page.raw_get("/Annots")
            for a in annots:
                fLOG("annot", a, dir(a))
            for i in page.items():
                fLOG("item", i)
            text = page.extractText()
            fLOG("text---", text)
            assert " " in text
            assert "\n" in text
            if "algorithms: their inability" not in text:
                raise Exception(text)

    def test_read_function(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        pdffile = os.path.join(os.path.split(__file__)[
                               0], "data", "1305.0445.pdf")
        assert os.path.exists(pdffile)

        text = pdf_read_content(pdffile)
        assert " " in text
        assert "\n" in text
        if "algorithms:theirinability" not in text.replace(" ", ""):
            raise Exception(text)
        if "their inability" not in text:
            raise Exception(text)

if __name__ == "__main__":
    unittest.main()
