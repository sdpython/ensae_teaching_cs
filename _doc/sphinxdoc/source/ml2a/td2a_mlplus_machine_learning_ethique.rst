
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

*Lectures mathémtiques*

* `A Reductions Approach to Fair Classification <https://arxiv.org/pdf/1803.02453.pdf>`_
* `FairTest: Discovering Unwarranted Associations in Data-Driven Applications <https://arxiv.org/pdf/1510.02377.pdf>`_

*Lectures*

* `Comment permettre à l'homme de garder la main ? <https://www.cnil.fr/sites/default/files/atoms/files/cnil_rapport_garder_la_main_web.pdf#page=58>`_,
  Les enjeux éthiques des algorithmes et de l’intelligence artificielle,
  Synthèse du débat public animé par la :epkg:`CNIL` dans le cadre de la mission
  de réflexion éthique confiée par la loi pour une république numérique.
* `Equality of Opportunity in Supervised Learning <http://ttic.uchicago.edu/~nati/Publications/HardtPriceSrebro2016.pdf>`_
* `O21 : La transparence des algorithmes relève des droits civiques <http://www.lemonde.fr/campus/article/2017/05/02/o21-la-transparence-des-algorithmes-releve-des-droits-civiques_5121201_4401467.html>`_
* `TransAlgo : évaluer la responsabilité et la transparence des systèmes algorithmiques <https://www.inria.fr/actualite/actualites-inria/transalgo>`_
* `Réguler les algorithmes : remise d'un rapport à Axelle Lemaire <https://www.economie.gouv.fr/reguler-algorithmes-rapport-axelle-lemaire-cge>`_
* `Enquête : comment les apps Figaro, L'Equipe ou Closer participent au pistage de 10 millions de Français <https://www-numerama-com.cdn.ampproject.org/c/www.numerama.com/politique/282934-enquete-comment-les-apps-figaro-lequipe-ou-closer-participent-au-pistage-de-10-millions-de-francais.html/amp>`_
* `Accountable Algorithms <https://www.jkroll.com/papers/dissertation.pdf>`_ (PhD thesis)
* `Improving the Transparency of the Sharing Economy <http://mathias.lecuyer.me/assets/assets/www2017airbnb.pdf>`_
* `Sunlight: Fine-grained Targeting Detection at Scale with Statistical Confidence <http://www.cs.columbia.edu/~djhsu/papers/sunlight.pdf>`_
* `Justice actuarielle, algorithmes... et données <http://freakonometrics.hypotheses.org/51783>`_
* `Surveiller et prévenir, l'ère de la pénalité prédictive <https://bourgoinblog.wordpress.com/2017/11/10/surveiller-et-prevenir-lere-de-la-penalite-predictive/>`_
* `Nozha Boujemaa : "Les algorithmes doivent apporter une aide à la décision mais pas en être les prescripteurs" <https://www.acteurspublics.com/2017/12/08/les-algorithmes-doivent-apporter-une-aide-a-la-decision-mais-pas-en-etre-les-prescripteurs>`_
* `On Fairness, Diversity and Randomness in Algorithmic Decision Making <https://arxiv.org/pdf/1706.10208.pdf>`_
* `Ten simple rules for responsible big data research <https://www.microsoft.com/en-us/research/publication/ten-simple-rules-for-responsible-big-data-research/>`_
* `Concrete Problems in AI Safety <https://arxiv.org/abs/1606.06565>`_
* `Predict Responsibly: Increasing Fairness by Learning to Defer <https://arxiv.org/pdf/1711.06664.pdf>`_
* `Ethics by Design: necessity or curse? <http://www.aies-conference.com/wp-content/papers/main/AIES_2018_paper_68.pdf>`_
* `Equality of Opportunity in Supervised Learning <https://arxiv.org/abs/1610.02413>`_

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

*Articles*

* `Microsoft is developing a tool to help engineers catch bias in algorithms <https://venturebeat.com/2018/05/25/microsoft-is-developing-a-tool-to-help-engineers-catch-bias-in-algorithms/>`_ (2018/05/25)

*Modules*

* `fairtest <https://github.com/columbia/fairtest>`_
* `fairlearn <https://github.com/Microsoft/fairlearn>`_
