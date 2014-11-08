"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.ensae_teaching_cs.td_1a.session3 import DecodeVigenereLongueurCle, DecodeVigenereCle, DecodeVigenere, CodeVigenere, CasseVigenere


class TestSession3 (unittest.TestCase):

    def test_vigenere(self) :
        fLOG (__file__, self._testMethodName, OutputPrint= __name__ == "__main__")

        fold = os.path.join(os.path.split(__file__)[0], "data")

        # on lit Victor Hugo
        with open (os.path.join(fold, "hugo_dernier_jour_condamne.txt"),"r") as f:
            message = f.read ()  # lit tout d'une seule traite

        # on limite la taille du fichier
        message = message [5000:7000]

        # on enleve les signes de ponctuation et on met en majuscule
        message = message.replace ("\n", "")
        message = message.replace ("\r", "")
        message = message.replace ("\t", "")
        message = message.replace (" ", "")
        message = message.replace (",", "")
        message = message.replace (";", "")
        message = message.replace (":", "")
        message = message.replace (".", "")
        message = message.replace ("'", "")
        message = message.replace ("\"", "")
        message = message.replace ("-", "")
        message = message.replace ("!", "")
        message = message.replace ("?", "")
        message = message.replace ("(", "")
        message = message.replace (")", "")
        message = message.upper ()

        # on code
        fLOG("on code, longueur du message ", len (message))
        cle     = "VIGENERES"
        code    = CodeVigenere (message, cle)
        memoire = cle
        cle     = None   # on oublie la cle

        # on determine la longueur de la cle
        l           = DecodeVigenereLongueurCle (code)
        # on determine la cle en suppose que la lettre E est la plus frequente
        # ne marche pas pour les textes anglais
        cle_code    = DecodeVigenereCle (code, l)
        # decode le texte
        decode      = DecodeVigenere (code, cle_code)

        assert "VIGENERES" == cle_code

        casse = CasseVigenere(code)
        assert len(code) == len(casse)
        assert casse.startswith("IDERLACAUSEDUNCONDAMNEQUELCONQUEEXECUTEUNJOURQUELCO")

        fLOG("------------------ vraie")
        fLOG(memoire)
        fLOG("------------------ cle trouve par Babbage")
        fLOG("longueur ", l, " cle : ", cle_code)
        if memoire == cle_code : fLOG("bonne cle")
        else : fLOG("mauvaise cle")
        fLOG("------------------ message")
        fLOG(message [:200])
        fLOG("------------------ message code")
        fLOG(code [:200])
        fLOG("------------------ message decode")
        fLOG(decode [:200])
        fLOG("------------------")
        if decode == message : fLOG("message bien retranscrit")
        else :
            for i in xrange (0, len (decode)) :
                if message[i] != decode [i] :
                    fLOG(i, message[i], decode[i])
            fLOG("message mal retranscrit")


if __name__ == "__main__"  :
    unittest.main ()