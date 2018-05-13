"""
@brief      test log(time=22s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper.flog import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from pyensae.datasource import download_data


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


class TestSkipExampleTheanoLogReg(unittest.TestCase):

    def test_cpu_gpu(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires theano
            return

        from theano import function, config, shared
        import theano.tensor as T
        import numpy
        import time

        vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
        iters = 1000

        rng = numpy.random.RandomState(22)
        x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
        f = function([], T.exp(x))
        fLOG(f.maker.fgraph.toposort())
        t0 = time.time()
        for i in range(iters):
            r = f()
        t1 = time.time()
        fLOG("Looping %d times took %f seconds" % (iters, t1 - t0))
        fLOG("Result is %s" % (r,))
        if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
            fLOG('Used the cpu')
        else:
            fLOG('Used the gpu')

    def test_theano_logreg(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires theano
            return

        from theano import config
        fLOG(config)
        from src.ensae_teaching_cs.examples.theano_logreg import theano_sgd_optimization_mnist, theano_predict
        temp = get_temp_folder(__file__, "temp__theano_logreg")
        dataset = "mnist.pkl.gz"
        if not os.path.exists(dataset):
            download_data(
                dataset, website="http://deeplearning.net/data/mnist/")
        model = os.path.join(temp, "log_reg_theano.bin")
        theano_sgd_optimization_mnist(
            dataset=dataset, saved_model=model, n_epochs=2, fLOG=fLOG)
        pred = theano_predict(model, dataset, 10)
        fLOG(pred)
        fLOG(type(pred))
        self.assertEqual(len(pred), 10)


if __name__ == "__main__":
    unittest.main()
