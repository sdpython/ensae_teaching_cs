"""
@brief      test log(time=3s)
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
from pyquickhelper.pycode import is_travis_or_appveyor


class TestSkipExampleTorch(unittest.TestCase):

    def test_torch(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # it requires latex
            return

        import numpy as np
        import torch
        import torch.nn as nn
        import torch.nn.functional as F
        import torch.optim as optim
        from torch.autograd import Variable
        from sklearn.datasets import load_iris

        X, Y = load_iris(return_X_y=True)
        X = X.astype("float32")
        X.shape, Y.shape

        ftrain = np.arange(X.shape[0]) % 4 != 0
        Xtrain, Ytrain = X[ftrain, :], Y[ftrain]
        Xtest, Ytest = X[~ftrain, :], Y[~ftrain]
        Xtrain.shape, Ytrain.shape, Xtest.shape, Ytest.shape

        N_EPOCHS = 1

        class Net(nn.Module):
            def __init__(self):
                super(Net, self).__init__()
                self.fc1 = nn.Linear(4, 3)

            def forward(self, x):
                x = self.fc1(x)
                return F.log_softmax(x)

        model = Net()
        optimizer = optim.Adam(model.parameters())
        loss_fn = nn.NLLLoss()

        Xtrain_ = Variable(torch.from_numpy(Xtrain))
        Xtest_ = Variable(torch.from_numpy(Xtest))
        Ytrain_ = Variable(torch.from_numpy(Ytrain.astype(np.int64)))
        Ytest_ = Variable(torch.from_numpy(Ytest.astype(np.int64)))
        perfs = []
        for t in range(1, N_EPOCHS + 1):
            # Before the backward pass, use the optimizer object to zero all of the
            # gradients for the variables it will update (which are the learnable weights
            # of the model)
            optimizer.zero_grad()

            # Forward pass: compute predicted y by passing x to the model.
            # got          (int, torch.FloatTensor, !torch.DoubleTensor!, torch.FloatTensor, bool, NoneType, torch.FloatTensor, int),
            # but expected (int, torch.FloatTensor, torch.LongTensor, torch.FloatTensor, bool, None, torch.FloatTensor, int)
            Ypred = model(Xtrain_)

            # Compute and print loss.
            loss = loss_fn(Ypred, Ytrain_)

            # Backward pass: compute gradient of the loss with respect to model
            # parameters
            loss.backward()

            # Calling the step function on an Optimizer makes an update to its
            # parameters
            optimizer.step()

            Ypred_test = model(Xtest_)
            loss_test = loss_fn(Ypred_test, Ytest_)
            # get the index of the max log-probability
            pred = Ypred_test.data.max(1, keepdim=True)[1]
            accuracy = pred.eq(Ytest_.data.view_as(pred)
                               ).cpu().sum() / Ytest.size
            perfs.append([t, loss.data[0], loss_test.data[0], accuracy])


if __name__ == "__main__":
    unittest.main()
