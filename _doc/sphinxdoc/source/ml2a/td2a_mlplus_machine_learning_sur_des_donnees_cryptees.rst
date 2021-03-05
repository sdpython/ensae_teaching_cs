
.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-td2a-ml-crypted:

Machine Learning sur des données cryptées
+++++++++++++++++++++++++++++++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/_gs2a_crypt

*Lectures*

* `Fully Homomorphic Encryption over the Integers <https://eprint.iacr.org/2009/616.pdf>`_
* `Homomorphic Encryption from Learning with Errors: Conceptually-Simpler, Asymptotically-Faster, Attribute-Based <https://eprint.iacr.org/2013/340.pdf>`_
* `Differentially Private Online Learning <http://www.jmlr.org/proceedings/papers/v23/jain12/jain12.pdf>`_
* `A Differentially Private Stochastic Gradient Descent Algorithm for Multiparty Classification <http://www.jmlr.org/proceedings/papers/v22/rajkumar12/rajkumar12.pdf>`_
* `Machine Learning Classification over Encrypted Data <https://eprint.iacr.org/2014/331.pdf>`_
* `CryptoNets: Applying Neural Networks to Encrypted Data with High Throughput and Accuracy <http://jmlr.org/proceedings/papers/v48/gilad-bachrach16.pdf>`_
* `Compressed Sensing <https://en.wikipedia.org/wiki/Compressed_sensing>`_
* `ML Confidential: Machine Learning on Encrypted Data <https://www.microsoft.com/en-us/research/publication/ml-confidential-machine-learning-on-encrypted-data-2/>`_
* `Encrypted statistical machine learning: new privacy preserving methods <https://arxiv.org/abs/1508.06845>`_
* `Fast and Secure Linear Regression and Biometric Authentication with Security Update <https://pdfs.semanticscholar.org/73f0/aa4e1b47b55f0f3d8464f61750e559067c56.pdf>`_
* `NuCypher KMS: Decentralized key management system <https://arxiv.org/abs/1707.06140>`_
* `Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts <https://eprint.iacr.org/2015/675.pdf>`_
* `Privacy-Preserving Classification on Deep Neural Network <https://eprint.iacr.org/2017/035.pdf>`_
* `Awesome Homomorphic Encryption <https://github.com/jonaschn/awesome-he>`_
* `Cryptotree : fast and accurate predictions on encrypted structured data
  <https://arxiv.org/pdf/2006.08299.pdf>`_

*Lectures - alternatives*

* `Semi-supervised Knowledge Transfer for Deep Learning from Private Training Data <https://arxiv.org/abs/1610.05755>`_
* `Practical Black-Box Attacks against Machine Learning <https://arxiv.org/abs/1602.02697>`_
* `awesome-differential-privacy <https://github.com/menisadi/awesome-differential-privacy>`_

*Lectures - MPC*

* `awesome-mpc <https://github.com/rdragos/awesome-mpc>`_ (Multi-Party Computation)

*Modules*

* `CrypTen <https://github.com/facebookresearch/CrypTen>`_ :
  l'approche la plus prometteuse par Facebook
* `ciphermed <https://github.com/rbost/ciphermed>`_, pas maintenu par l'auteur mais un peu
  plus par d'autres `ciphermed-forests <https://github.com/paberr/ciphermed-forests>`_
* `PySyft <https://github.com/OpenMined/PySyft>`_ : encrypted deep learning library
* `python-paillier (phe) <https://github.com/n1analytics/python-paillier>`_ : a library for partially homomorphic encryption in python,
  cette librairie fait du machine learning en clair une fois les données et le modèle décryptées,
  elle promet de faire `mieux <https://github.com/OpenMined/PySyft/blob/master/syft/nn/linear.py#L92>`_
* `PySEAL <https://github.com/Lab41/PySEAL>`_ (`SEAL <https://github.com/microsoft/SEAL>`_,
  `PySEAL: A Python wrapper implementation of the SEAL homomorphic encryption library
  <https://arxiv.org/abs/1803.01891>`_)
* `cryptotree <https://github.com/dhuynh95/cryptotree>`_
