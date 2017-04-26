"""
@file
@brief globals functions to manipulate PDF files
"""

try:
    from pyPdf import PdfFileReader
except ImportError as e:
    raise ImportError("If this import fails, you should use the version from github/sdpython:\n" +
                      "pip install https://github.com/sdpython/pyPdf/archive/trunk.zip") from e


def pdf_read_content(filename):
    """
    extracts the text from a PDF file

    @param      filename            (str) filename
    @return                         content (string)

    The module was modified to introduce spaces. The method is not
    very robust because it does not take into account the size of characters.
    But the method PageObject.extractText can be modified to deal with
    by introducing statistics or a better knowledge of PDF format.

    The best way to introduce spaces and end of line is to study
    the distribution of distances between consecutive characters assuming
    we would fine a couple of modes:

    * one for characters on the same line and from the same word,
    * one for characters on the same line but separated by a space,
    * one for characters on two different lines. This method
      was not implemented yet.

    If a line ends by "-", it is assumed a word was split. It is replaced by "---".

    This function only works with  `sdpython/pyPdf <https://github.com/sdpython/pyPdf>`_.
    The module was modified to work better with spaces.
    Every line ending by ``'---'`` is a split word.
    """
    texts = []
    with open(filename, "rb") as f:
        input1 = PdfFileReader(f)
        npage = input1.getNumPages()
        for ip in range(npage):
            page = input1.getPage(ip)
            text = page.extractText()
            texts.append(text)
    return "\n\n".join(texts)
