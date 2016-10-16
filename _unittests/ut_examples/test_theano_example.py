"""
@brief      test log(time=10s)
@author     Xavier Dupre
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
    import pyquickhelper as skip____
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
    import pyquickhelper as skip____


try:
    import pyensae as skip_____
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae as skip_____


from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyensae.datasource import download_data


class TestExampleTheanoLogReg(unittest.TestCase):

    def test_theano_logreg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires latex
            return

        from src.ensae_teaching_cs.examples.theano_logreg import sgd_optimization_mnist, predict
        temp = get_temp_folder(__file__, "temp__theano_logreg")
        dataset = "mnist.pkl.gz"
        if not os.path.exists(dataset):
            download_data(
                dataset, website="http://deeplearning.net/data/mnist/")
        model = os.path.join(temp, "log_reg_theano.bin")
        sgd_optimization_mnist(
            dataset=dataset, saved_model=model, n_epochs=2, fLOG=fLOG)
        pred = predict(model, dataset, 10)
        fLOG(pred)
        fLOG(type(pred))
        self.assertEqual(len(pred), 10)


if __name__ == "__main__":
    unittest.main()
