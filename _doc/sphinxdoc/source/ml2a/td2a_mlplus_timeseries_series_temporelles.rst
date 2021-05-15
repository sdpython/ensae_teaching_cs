
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/td_2a_notions.html#pour-un-profil-plutot-data-scientist

Timeseries - Séries temporelles
+++++++++++++++++++++++++++++++

*Notebooks*

.. toctree::
    :maxdepth: 2

    ../notebooks/ml_timeseries_base
    ../notebooks/td2a_timeseries
    ../notebooks/td2a_timeseries_correction
    ../notebooks/seasonal_timeseries

(à venir : modèles SETAR pour les séries non périodiques, modèles proies prédateurs)

Quelques rappels sur les lissages, saisonnalités, modèles linéaires
appliqués aux séries temporelles :
`Projet Machine Learning pour la Prévision: séries temporelles <https://www.math.u-psud.fr/~goude/Materials/ProjetMLF/time_series.html>`_

*Lectures*

* `Time series analysis with pandas <http://earthpy.org/pandas-basics.html>`_
* `Consistent Algorithms for Clustering Time Series <http://www.jmlr.org/papers/volume17/khaleghi16a/khaleghi16a.pdf>`_
* `Learning Time Series Detection Models from Temporally Imprecise Labels <https://arxiv.org/abs/1611.02258>`_
* `Time Series Prediction With Deep Learning in Keras <http://machinelearningmastery.com/time-series-prediction-with-deep-learning-in-python-with-keras/>`_
* `Sequence Classification with LSTM Recurrent Neural Networks in Python with Keras <http://machinelearningmastery.com/sequence-classification-lstm-recurrent-neural-networks-python-keras/>`_
  (voir `LSTM <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>`_)
* `Time Series Classification and Clustering with Python <http://alexminnaar.com/time-series-classification-and-clustering-with-python.html>`_
* `Dynamic Time Warping <https://en.wikipedia.org/wiki/Dynamic_time_warping>`_
* `Functional responses, functional covariates and the concurrent model <http://www.ece.uvic.ca/~bctill/papers/mocap/Ramsay_Silverman_2005ao.pdf>`_
* `Fast and Accurate Time Series Classification with WEASEL <https://arxiv.org/pdf/1701.07681.pdf>`_ (text and timeseries)
* `Forecasting at Scale <https://facebookincubator.github.io/prophet/static/prophet_paper_20170113.pdf>`_ (Facebook)
* `SETAR <https://en.wikipedia.org/wiki/SETAR_(model)>`_ : prédiction sur des modèles
  en apparence cycliques mais non périodiques (type proies-prédateurs, chaotiques),
  SETAR = Self-Exciting Threshold AutoRegressive
* `Using predator-prey models on the Canadian lynx series <http://andrewgelman.com/2012/01/28/the-last-word-on-the-canadian-lynx-series/>`_,
  `Inference for nonlinear dynamical systems <http://www.pnas.org/content/103/49/18438.full.pdf>`_
* `Milestones of Deep Learning <http://www.codesofinterest.com/2017/07/milestones-of-deep-learning.html#more>`_
* `Engineering Extreme Event Forecasting at Uber with Recurrent Neural Networks <https://eng.uber.com/neural-networks/>`_
* `Holt-Winters seasonal method <https://www.otexts.org/fpp/7/5>`_,
  `Initializing the Holt-Winters method <https://robjhyndman.com/hyndsight/hw-initialization/>`_
* `A Comparison of Estimation Methods for Vector Autoregressive Moving-Average Models <http://www.christiankascha.com/wp-content/uploads/2013/03/ERVARMAmain_final.pdf>`_
* `A state space framework for automatic forecasting using exponential smoothing methods <https://robjhyndman.com/papers/hksg.pdf>`_
* `Clustering Time Series with Nonlinear Dynamics: A Bayesian Non-Parametric and Particle-Based Approach
  <https://arxiv.org/abs/1810.09920>`_

*Compétitions*

* Kaggle Web Traffic Time Series Forecasting `code <https://github.com/Arturus/kaggle-web-traffic>`_,
  `modèle <https://github.com/Arturus/kaggle-web-traffic/blob/master/how_it_works.md>`_

*Modules*

* `statsmodels <http://statsmodels.sourceforge.net/>`_
* `pyflux <http://pyflux.readthedocs.io/en/latest/>`_ (la documentation est plutôt bien faite)
* `fbprophet <https://github.com/facebookincubator/prophet/tree/master/python>`_
  (requires `pystan <http://pystan.readthedocs.io/en/latest/index.html>`_)
* `tensorflow <https://www.tensorflow.org/tutorials/structured_data/time_series>`_
* `Rob J Hyndman software <https://robjhyndman.com/software/>`_
  (disponible uniquement en R)
* `influxdb <https://github.com/influxdata/influxdb>`_ (An Open-Source Time Series Database)
* `seasonal <https://github.com/welch/seasonal>`_
* `seglearn <https://github.com/dmbee/seglearn>`_
* `sktime <https://github.com/alan-turing-institute/sktime>`_
* `flow-forecast <https://github.com/AIStream-Peelout/flow-forecast>`_

Un peu plus expérimental :

* `sulekha_holtwinters <https://github.com/sulekhaaloorravi-python/sulekha_holtwinters>`_, Holt-Winters sur
  :epkg:`Spark`
* `holtwinters.py <https://gist.github.com/andrequeiroz/5888967>`_,
  Holt-Winters dans un fichier.
