
.. image:: pyeco.png
    :height: 20
    :alt: Economie
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-economiste

.. image:: pystat.png
    :height: 20
    :alt: Statistique
    :target: http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a_notions.html#pour-un-profil-plutot-data-scientist

.. _l-ml2a-mlethical:

Machine Learning éthique
++++++++++++++++++++++++

Toutes les entreprises ont des données. Ce qui a changé récemment est
ce ne sont plus seulement des données à caractère personnel, l'ensemble
de vos commandes, le montant, mais aussi des
données de déplacements. Le téléphone portable et les applications
permet à beaucoup plus d'acteurs de collecter ces mêmes données.
La législation n'est pas toujours très claire quant à ce qu'on le droit
d'en faire et les pays ne partagent pas tous les mêmes règles.
De plus, c'est une chose que de fixer une limite, c'est autre chose
que de vérifier qu'elle n'a pas été franchie.
Des modèles construits avec des données si précises peuvent
de retrouver des informations que vous n'avez pourtant pas divulgué.
Comment déterminer si un modèle ne produit pas des résultats biaisés
envers une partie de la population même avec des données anonymes ?
Les articles sont encore peu nombreux à
ce sujet et plutôt récents. Il est probable qu'il y en ait un peu plus
à l'avenir. Il n'existe pas de certitude quant au caractère éthique
d'un modèle. Quelques idées ont néanmoins émergé :

* La collecte des données est parfois biaisée, les échantillons aléatoires
  sont rares sur Internet, la collecte est incitative (échange service contre
  données). Certaines sous-population sont sur-représentées, d'autres sous-représentées.
  Il faut en tenir compte.
* Construire un modèle interprétable et de cette façon vérifier son côté éthique :
  `Ideas on interpreting machine learning <https://www.oreilly.com/ideas/ideas-on-interpreting-machine-learning>`_.
* Fabriquer de fausses observations pour vérifier que le modèle ne change
  pas de prédictions quand il ne le devrait pas :
  `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_.
* Construire deux modèles pour éviter les interactions entre :math:`X_1` et :math:`X_2`,
  le premier modèle ne voit que :math:`X_1`, le second ne voit que :math:`X_2`,
  puis on combine les prédictions :
  `When Recommendations Systems Go Bad <https://www.youtube.com/watch?v=MqoRzNhrTnQ>`_.
* Construire une partition de la population à étudier pour vérifier
  que l'appartenance à un sous-groupe n'est pas corrélée à la prédiction
  ou à l'erreur de prédiction :
  `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_.

L'article `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_
définit l'aspect éthique comme l'invariance d'une loi marginale. On suppose que *S*
est un attribut protégé binaire (exemple : le genre). *I* sont les entrées du modèle
de machine learning, *O* les sorties. Le modèle est éthique si :

.. math::

    \pr{ O | I, S=0} = \pr{ O | I, S=1}

La connaissance de *S* ne change pas la prédiction. Cela pose deux problèmes.
Le premier est que parfois cette distribution change car cet attribut est corrélé avec
un autre qui lui n'est pas protégé. Que décide-t-on dans ce cas ? Le second est
l'égalité n'est jamais vérifié sur de vraies données, les deux distributions
doivent être proches. Elles peuvent l'être sur l'ensemble de la population
tout en ne l'étant pas du tout sur une petite partie de la population.
L'article `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_
propose une réponse à ces deux problèmes.

L'article `A Reductions Approach to Fair Classification <https://arxiv.org/pdf/1803.02453.pdf>`_
pousse ces concepts jusqu'à définir mathématiquement la parité d'un modèle et l'égalité des chances
(voir :ref:`blog-ethique-fairlearn`).

*Notebooks*

.. toctree::

    ../notebooks/td2a_ethics
    ../notebooks/td2a_ethics_correction

*Lectures mathématiques*

* `A Reductions Approach to Fair Classification <https://arxiv.org/pdf/1803.02453.pdf>`_
* `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_

*Lectures françaises*

* `Guide des algorithmes publics <https://etalab.github.io/algorithmes-publics/guide.html>`_
* `Comment permettre à l'homme de garder la main ? <https://www.cnil.fr/sites/default/files/atoms/files/cnil_rapport_garder_la_main_web.pdf#page=58>`_,
  Les enjeux éthiques des algorithmes et de l’intelligence artificielle,
  Synthèse du débat public animé par la :epkg:`CNIL` dans le cadre de la mission
  de réflexion éthique confiée par la loi pour une république numérique.
* `O21 : La transparence des algorithmes relève des droits civiques <http://www.lemonde.fr/campus/article/2017/05/02/o21-la-transparence-des-algorithmes-releve-des-droits-civiques_5121201_4401467.html>`_
* `Enquête : comment les apps Figaro, L'Equipe ou Closer participent au pistage de 10 millions de Français <https://www-numerama-com.cdn.ampproject.org/c/www.numerama.com/politique/282934-enquete-comment-les-apps-figaro-lequipe-ou-closer-participent-au-pistage-de-10-millions-de-francais.html/amp>`_
* `Surveiller et prévenir, l'ère de la pénalité prédictive <https://bourgoinblog.wordpress.com/2017/11/10/surveiller-et-prevenir-lere-de-la-penalite-predictive/>`_
* `Nozha Boujemaa : "Les algorithmes doivent apporter une aide à la décision mais pas en être les prescripteurs" <https://www.acteurspublics.com/2017/12/08/les-algorithmes-doivent-apporter-une-aide-a-la-decision-mais-pas-en-etre-les-prescripteurs>`_

*Lectures*

* `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_
* `TransAlgo : évaluer la responsabilité et la transparence des systèmes algorithmiques <https://www.inria.fr/actualite/actualites-inria/transalgo>`_
* `Réguler les algorithmes : remise d'un rapport à Axelle Lemaire <https://www.economie.gouv.fr/reguler-algorithmes-rapport-axelle-lemaire-cge>`_
* `Accountable Algorithms <https://www.jkroll.com/papers/dissertation.pdf>`_ (PhD thesis)
* `Improving the Transparency of the Sharing Economy <http://mathias.lecuyer.me/assets/assets/www2017airbnb.pdf>`_
* `Sunlight: Fine-grained Targeting Detection at Scale with Statistical Confidence <http://www.cs.columbia.edu/~djhsu/papers/sunlight.pdf>`_
* `Justice actuarielle, algorithmes... et données <http://freakonometrics.hypotheses.org/51783>`_
* `On Fairness, Diversity and Randomness in Algorithmic Decision Making <https://arxiv.org/pdf/1706.10208.pdf>`_
* `Ten simple rules for responsible big data research <https://www.microsoft.com/en-us/research/publication/ten-simple-rules-for-responsible-big-data-research/>`_
* `Concrete Problems in AI Safety <https://arxiv.org/abs/1606.06565>`_
* `Predict Responsibly: Increasing Fairness by Learning to Defer <https://arxiv.org/pdf/1711.06664.pdf>`_
* `Ethics by Design: necessity or curse? <http://www.aies-conference.com/wp-content/papers/main/AIES_2018_paper_68.pdf>`_
* `Equality of Opportunity in Supervised Learning <https://arxiv.org/abs/1610.02413>`_
* `Algorithm Assessment Report <https://www.data.govt.nz/assets/Uploads/Algorithm-Assessment-Report-Oct-2018.pdf>`_
  (issu de l'INSEE néozélandaise)
* `Impossibility and Uncertainty Theorems in AI Value Alignment <https://arxiv.org/pdf/1901.00064.pdf?utm_campaign=the_algorithm.unpaid.engagement&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz-8SQPvr8mh-ICrJzt0vJhRCEPzgIalY3fRUX7Q4iMwG1rNFf-v4-GR9BNEI_UB8R-0z08Jm>`_
* `Themis-ml: A Fairness-aware Machine Learning Interface for
  End-to-end Discrimination Discovery and Mitigation
  <https://github.com/cosmicBboy/themis-ml/blob/master/paper/main.pdf>`_
* `Automated Directed Fairness Testing <https://arxiv.org/abs/1807.00468>`_
* `Automated Experiments on Ad Privacy Settings
  <http://www.andrew.cmu.edu/user/danupam/dtd-pets15.pdf>`_
* `Fairness in Criminal Justice Risk Assessments: The State of the Art
  <https://arxiv.org/abs/1703.09207>`_
* `Counterfactual Fairness <https://arxiv.org/pdf/1703.06856.pdf>`_
* `Fairness Constraints: A Flexible Approach for Fair Classification
  <http://www.jmlr.org/papers/volume20/18-262/18-262.pdf>`_

*Conférences*

* `Katharine Jarmul | Keynote: Ethical Machine Learning: Creating Fair Models in an Unjust World <https://www.youtube.com/watch?v=hDgXIUM3Rmw>`_
* `When Recommendations Systems Go Bad <https://www.youtube.com/watch?v=MqoRzNhrTnQ>`_
* `How AI Designers will Dictate Our Civic Future <https://vimeo.com/238221677>`_ de
  `Latanya Sweeney <https://dataprivacylab.org/people/sweeney/>`_,
  je recommande vivement cette conférence qui montre comment des biais
  peuvent apparaître dans un système intégrant le machine learning,
  il n'existe pas de façon d'éviter les biais si ce n'est en gardant
  constamment à l'esprit qu'ils apparaîtront quoiqu'il arrive
  si un système est prévu pour s'adapter au fur et à mesure.
  Le système apprend les biais et limite de plus en plus
  tout ce qui pourrait l'en faire sortir.

*Sites*

* `Data Transparency Lab <http://datatransparencylab.org/>`_
* `OPAL <http://www.data4sdgs.org/dc-opal/>`_
* `FATML <https://www.fatml.org/>`_ ou Fairness, Accountability, and Transparency in Machine Learning,
  ce site est une excellente source d'article scientifiques sur le sujet.
* `FATE <https://www.microsoft.com/en-us/research/group/fate/>`_, groupe de recherche sur
  Fairness, Accountability, Transparency, and Ethics in AI chez :epkg:`Microsoft`
* `Data&Society <https://datasociety.net/>`_, publications d'articles ou rapports comme celui-ci
  `Fairness in Precision Medicine <https://datasociety.net/output/fairness-in-precision-medicine/>`_
  qui traite des biais qui peuvent survenir lorsqu'on adapte les décisions
  médicales en fonction des données récoltées pour une personne
  en particulier (*precision medecine*).
* `CS 294: Fairness in Machine Learning <https://fairmlclass.github.io/>`_
* `Algorithms and Bias: Q. and A. With Cynthia Dwork
  <https://www.nytimes.com/2015/08/11/upshot/algorithms-and-bias-q-and-a-with-cynthia-dwork.html>`_
* `Fairness is not static: deeper understanding of long term fairness via simulation studies
  <https://github.com/google/ml-fairness-gym/blob/master/papers/acm_fat_2020_fairness_is_not_static.pdf>`_

*Articles*

* `Microsoft is developing a tool to help engineers catch bias in algorithms
  <https://venturebeat.com/2018/05/25/microsoft-is-developing-a-tool-to-help-engineers-catch-bias-in-algorithms/>`_
* `Sent to Prison by a Software Program's Secret Algorithms
  <https://www.nytimes.com/2017/05/01/us/politics/sent-to-prison-by-a-software-programs-secret-algorithms.html>`_,
  `Emotional Judges and Unlucky Juveniles
  <https://www.nber.org/papers/w22611?utm_campaign=ntw&utm_medium=email&utm_source=ntw>`_,
  `How artificial intelligence can help us make judges less biased
  <https://www.theverge.com/2019/1/17/18186674/daniel-chen-machine-learning-rule-of-law-economics-psychology-judicial-system-policy>`_
* `How We Analyzed the COMPAS Recidivism Algorithm
  <https://www.propublica.org/article/how-we-analyzed-the-compas-recidivism-algorithm>`_
* `ML-fairness-gym: A Tool for Exploring Long-Term Impacts of Machine Learning Systems
  <https://ai.googleblog.com/2020/02/ml-fairness-gym-tool-for-exploring-long.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+blogspot%2FgJZg+%28Google+AI+Blog%29>`_

*Modules*

* `aequitas <https://github.com/dssg/aequitas>`_
* `fairlearn <https://github.com/Microsoft/fairlearn>`_
* `fairness-comparison <https://github.com/algofairness/fairness-comparison>`_
  (un peu maintenu)
* `fairness-indicators
  <https://github.com/tensorflow/fairness-indicators>`_
* `ml-fairness-gym <https://github.com/google/ml-fairness-gym>`_

*Modules non maintenu*

C'est souvent le cas de code produit par des chercheurs qui
écrive le code pour écrire un article scientifique et qui n'a
pas vocation à être maintenu par la suite.

* `fair-classification <https://github.com/mbilalzafar/fair-classification>`_
  (non maintenu)
* `fairml <https://github.com/adebayoj/fairml>`_ (non maintenu)
* `fairml-farm <https://github.com/yoshavit/fairml-farm>`_ (non maintenu)
* `fairtest <https://github.com/columbia/fairtest>`_ (non maintenu)
* `themis-ml <https://github.com/cosmicBboy/themis-ml>`_ (non maintenu)

