

.. _l-election_report_voix:

Optimisation sous contraintes appliquée au calcul du report des voix
====================================================================

Recopié depuis `Optimisation sous contraintes appliquée au calcul du report des voix <http://www.xavierdupre.fr/blog/2013-12-07_nojs.html>`_.

Entre les deux tours des élections présidentielles, on parle beaucoup
du report des voix des élections. 
Dans la plupart des articles que j'ai trouvés 
`Les 1.139.316 voix qui ont fait la victoire d'Hollande <http://www.slate.fr/france/54761/presidentielle-hollande-sarkozy-ecart-voix-report>`_
ces intentions sont estimées par sondage. Un blog parle d'une méthode 
d'estimation après seulement que les élections ont eu lieu :
`Estimation des reports de voix - explications techniques <http://www.joelgombin.fr/?p=718>`_.
La méthode proposée est bayésienne. Ici, j'ai utilisé l'optmisation sous contraintes
car c'est la méthode que je souhaitais illustrer pour mes 
enseignements. J'ai pris les élections comme
exemples d'application. Les données sont accessibles sur le site 
(`data.gouv.fr <http://www.data.gouv.fr/>`_,
`élections 2012 <http://www.data.gouv.fr/DataSet/572077>`_)
Elles incluent les chiffres aggrégés par départements et cantons dont je 
me suis servi et que j'ai regroupés ici : :download:`french_elections.zip`.

On dispose donc des voix ventilées par candidats et disponibles pour chaque
départements. On cherche à calculer une matrice de report de voix qui soit 
la même pour tous les départements.

.. raw:: html

    <table border="1">
        <tfoot><tr align="right"><td colspan="15">
        <div id="no-paging">*source <a href="http://www.data.gouv.fr/DataSet/572077">open.data.gouv.fr: élections 2012</a>*
        </div></td></tr>
        </tfoot>
        
      <thead>
        <tr style="text-align: right;">
          <th>ARTHAUD</th>
          <th>Abstentions</th>
          <th>BAYROU</th>
          <th>Blancs et nuls</th>
          <th>CHEMINADE</th>
          <th>Code dep</th>
          <th>DUPONT-AIGNAN</th>
          <th>HOLLANDE</th>
          <th>JOLY</th>
          <th>LE PEN</th>
          <th>Département</th>
          <th>MÉLENCHON</th>
          <th>POUTOU</th>
          <th>SARKOZY</th>
          <th>total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1794</td>
          <td> 65996</td>
          <td>32650</td>
          <td>6453</td>
          <td> 860</td>
          <td>1</td>
          <td>7208</td>
          <td> 73096</td>
          <td> 7268</td>
          <td> 66540</td>
          <td>                     AIN</td>
          <td>30898</td>
          <td>3323</td>
          <td> 97722</td>
          <td>393808</td>
        </tr>
        <tr>
          <td>2490</td>
          <td> 72928</td>
          <td>19895</td>
          <td>5196</td>
          <td> 738</td>
          <td>2</td>
          <td>5853</td>
          <td> 80751</td>
          <td> 3455</td>
          <td> 78452</td>
          <td>                   AISNE</td>
          <td>30360</td>
          <td>3860</td>
          <td> 72090</td>
          <td>376068</td>
        </tr>
        <tr>
          <td>1482</td>
          <td> 45266</td>
          <td>17814</td>
          <td>5059</td>
          <td> 457</td>
          <td>3</td>
          <td>4068</td>
          <td> 61131</td>
          <td> 3232</td>
          <td> 37736</td>
          <td>                  ALLIER</td>
          <td>27969</td>
          <td>2584</td>
          <td> 49477</td>
          <td>256275</td>
        </tr>
        <tr>
          <td> 487</td>
          <td> 21034</td>
          <td> 7483</td>
          <td>2111</td>
          <td> 283</td>
          <td>4</td>
          <td>1845</td>
          <td> 24551</td>
          <td> 2933</td>
          <td> 20875</td>
          <td> ALPES DE HAUTE PROVENCE</td>
          <td>15269</td>
          <td>1394</td>
          <td> 25668</td>
          <td>123933</td>
        </tr>
        <tr>
          <td>1576</td>
          <td>153383</td>
          <td>38980</td>
          <td>9063</td>
          <td>1238</td>
          <td>6</td>
          <td>9241</td>
          <td>111990</td>
          <td>12556</td>
          <td>136982</td>
          <td>         ALPES MARITIMES</td>
          <td>49493</td>
          <td>4048</td>
          <td>216738</td>
          <td>745288</td>
        </tr>
      </tbody>
    </table>


.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="7">
        <div id="no-paging">*source <a href="http://www.data.gouv.fr/DataSet/572077">open.data.gouv.fr: élections 2012</a>*
        </div></td></tr>
        </tfoot>

      <thead>
        <tr style="text-align: right;">
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>Code</th>
          <th>HOLLANDE</th>
          <th>Département</th>
          <th>SARKOZY</th>
          <th>total</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td> 67279</td>
          <td>19513</td>
          <td>1</td>
          <td>131333</td>
          <td>                     AIN</td>
          <td>175741</td>
          <td>393866</td>
        </tr>
        <tr>
          <td> 73997</td>
          <td>21056</td>
          <td>2</td>
          <td>147260</td>
          <td>                   AISNE</td>
          <td>133760</td>
          <td>376073</td>
        </tr>
        <tr>
          <td> 45079</td>
          <td>14924</td>
          <td>3</td>
          <td>111615</td>
          <td>                  ALLIER</td>
          <td> 84593</td>
          <td>256211</td>
        </tr>
        <tr>
          <td> 20314</td>
          <td> 6639</td>
          <td>4</td>
          <td> 49498</td>
          <td> ALPES DE HAUTE PROVENCE</td>
          <td> 47444</td>
          <td>123895</td>
        </tr>
        <tr>
          <td>146254</td>
          <td>30067</td>
          <td>6</td>
          <td>203117</td>
          <td>         ALPES MARITIMES</td>
          <td>366055</td>
          <td>745493</td>
        </tr>
      </tbody>
    </table>

On cherche une matrice *V* qui permet d'obtenir les voix *Y* du second tour
en fonction des voix du premier tour *X* :
:math:`Y = VX, \; X \in M_{nc}, \; Y \in M_{nd}, \; V \in M_{cd}`.
*n* est le nombre de départements, *c* est le nombre 
de candidats du premier tour (abstention et bulletin nuls inclus),
*d* est le nombre de candidats du second tour.
La matrice *V* définit le report des voix : *V<sub>ij</sub>*
est la proportion des voix du candidat *c* allant au candidat *d*.
Elle vérifie les contraintes suivantes :


.. math::

    \begin{array}{l}
    \forall c,d, \; V_{cd} \leqslant 0 \\
    \forall c, \; \sum_{d=1}^{D} V_{cd} = 1 
    \end{array}

Le problème n'est pas très éloigné d'une régression avec des contraintes
sur les coefficients excepté que la matrice *Y* a plus d'une colonne.
Pour contourner l'obstacle, on construit une autre matrice :math:`Y^*`
d'une seule colonne et quatre fois plus de lignes (*D=4*). On applique une
transformation similaire sur *X*.

.. math::

    \begin{array}{l}
    Y^*_{k} = Y_{k \mod(n),[k/n]} \\
    X^*_{k,i} = X_{k \mod(n),i} 
    \end{array}

Par la suite, on désigne sous *X,Y* les matrices 
:math:`X^*, Y^*`.
On cherche à résoudre le problème d'optmisation sous contrainte :

.. math::

    \begin{array}{l}
    \min_V (Y-XV)'(Y-XV) \\
        avec \; \left \{ \begin{array}{l}
        \forall c,d \; V_{cd} \geqslant 0 \\
        \forall c \; \sum_{d=1}^{D} V_{cd} = 1 
        \end{array} \right .
    \end{array}

C'est un problème d'`optimisation convexe <http://fr.wikipedia.org/wiki/Optimisation_convexe>`_
sous contraintes linéaires qu'on peut résoudre avec le module `cvxopt <http://cvxopt.org/>`_.
La fonction `qp <http://abel.ee.ucla.edu/cvxopt/userguide/coneprog.html?highlight=qp#cvxopt.solvers.qp>`_
est la plus adaptée. Elle résoud le problème présenté sous la forme :

.. math::

    \begin{array}{l}
    \min_x \frac{1}{2} x'Px + q'x \\
        avec \; \left \{ \begin{array}{l}
        Gx \leqslant h \\
        Ax = b
        \end{array} \right .
    \end{array}

Il suffit d'associer les lettres de ce problème *P,q,G,h,A,b* à nos données :

* *x,P,q* dépendent de *X,Y,V*,
* *G = -<b>1</b>*, vecteur composé de -1,
* *h=0*,
* *A* experiment le fait que les coefficients de *V* somment à 1 sur la même ligne,
* *b=<b>1</b>*.

Les matrices *P,Q* sont construites en développant l'erreur de régression.
Le vecteur *x* est une représentation de la matrice *V* cherchée.

.. math::

    \left\|(Y-XV)'(Y-XV)\right\|
              = \sum_{i=1}^D Y_i'Y_i \underbrace{- 2 \sum_{i=1}^D   Y_i' X_i}_{p'} x + 
                x' \underbrace{\sum_{i=1}^D  X_i' X_i}_{\frac{1}{2}Q} x

Je passe les détails d'implémentation que vous pouvez trouver là :
`class ElectionResults <http://www.xavierdupre.fr/app/pyhome3/helpsphinx/pyhome/pyhome3/srcpyhome/wandering/election/elections.html>`_,
`def vote_transfer <http://www.xavierdupre.fr/app/pyhome3/helpsphinx/_modules/pyhome3/srcpyhome/wandering/election/elections.html#ElectionResults.vote_transfer>`_
et `study_french_elections.py <http://www.xavierdupre.fr/app/pyhome3/helpsphinx/pyhome/studies/french_elections/study_french_elections.html>`_.
Cette classe lit les fichiers Excel venant du site 
`open.data.gouv.fr <http://www.data.gouv.fr/>`_,
puis construit les matrices *P,q,G,h,A,b* qui permettent de résoudre le problème 
d'optimisation. Elle corrige aussi les nombres d'inscrits pour chaque département.
car le nombre d'inscrits est légèrement
différents d'une tour à l'autre (voir les deux premiers tableaux).
Avec une règle de trois, on s'assure que le nombre d'inscrits est identique
aux deux tours.

.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*optimisation dynamique sous contrainte (aggrégation par départements) en 2012*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>HOLLANDE</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>ARTHAUD</th>
          <td> 30%</td>
          <td>   </td>
          <td> 70%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>Abstentions</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td> 31%</td>
          <td>   </td>
          <td> 18%</td>
          <td>51%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td> 32%</td>
          <td>   </td>
          <td> 68%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>CHEMINADE</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>DUPONT-AIGNAN</th>
          <td>    </td>
          <td>   </td>
          <td> 45%</td>
          <td>55%</td>
        </tr>
        <tr>
          <th>HOLLANDE</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>JOLY</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td> 33%</td>
          <td> 6%</td>
          <td>    </td>
          <td>61%</td>
        </tr>
        <tr>
          <th>MELENCHON</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>POUTOU</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td>  6%</td>
          <td>   </td>
          <td>    </td>
          <td>94%</td>
        </tr>
      </tbody>
    </table>

Il est difficile d'interpréter ces résultats sans prendre quelques précautions.
La fonction d'erreur donne le même poids à toutes les voix. 
Cela signifie que la précision de ces chiffres est meilleure pour les 
partis les plus représentés. Ci-dessous,
les mêmes résultats mais en partant des résultats aggrégés par cantons (environ 4000).

.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*optimisation dynamique sous contrainte (aggrégation par cantons) en 2012*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>HOLLANDE</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>ARTHAUD</th>
          <td> 98%</td>
          <td>   </td>
          <td>  2%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>Abstentions</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td> 46%</td>
          <td>   </td>
          <td>  6%</td>
          <td>48%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td> 46%</td>
          <td>   </td>
          <td> 54%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>CHEMINADE</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>DUPONT-AIGNAN</th>
          <td> 28%</td>
          <td>   </td>
          <td> 37%</td>
          <td>35%</td>
        </tr>
        <tr>
          <th>HOLLANDE</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>JOLY</th>
          <td>100%</td>
          <td>   </td>
          <td>    </td>
          <td>   </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td> 17%</td>
          <td> 5%</td>
          <td>  8%</td>
          <td>70%</td>
        </tr>
        <tr>
          <th>MELENCHON</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>POUTOU</th>
          <td>    </td>
          <td>   </td>
          <td>100%</td>
          <td>   </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td>  9%</td>
          <td>   </td>
          <td>    </td>
          <td>91%</td>
        </tr>
      </tbody>
    </table>

Ces résultats sont assez fluctuants. Le 
`bootstrap <http://fr.wikipedia.org/wiki/Bootstrap_%28statistiques%29>`_
est une méthode statistique qui permet d'obtenir des intervalles 
de confiance. J'ai appliqué la méthode sur la série des cantons, plus longue,
car elle réduit la variance
du nombre d'inscrits après rééchantillonage.
On retrouve le fait que la marge d'erreur est grande pour les candidats
ayant obtenu peu de voix.

.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*intervalles de confiance à 20% (aggrégation par cantons) en 2012*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>HOLLANDE</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>ARTHAUD</th>
          <td> 0%-100%</td>
          <td>          </td>
          <td>   0%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>Abstentions</th>
          <td>    100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td> 0%- 81%</td>
          <td>          </td>
          <td>   0%- 33%</td>
          <td>  19%- 79%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td> 0%-100%</td>
          <td>          </td>
          <td>   0%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>CHEMINADE</th>
          <td>    100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>DUPONT-AIGNAN</th>
          <td> 0%-100%</td>
          <td>          </td>
          <td>   0%- 64%</td>
          <td>   0%- 96%</td>
        </tr>
        <tr>
          <th>HOLLANDE</th>
          <td> 0%-  7%</td>
          <td>          </td>
          <td>  93%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>JOLY</th>
          <td>    100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td> 0%- 31%</td>
          <td>   3%-  6%</td>
          <td>   2%- 14%</td>
          <td>  61%- 82%</td>
        </tr>
        <tr>
          <th>MELENCHON</th>
          <td> 0%-  2%</td>
          <td>          </td>
          <td>  98%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>POUTOU</th>
          <td>        </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td> 0%- 24%</td>
          <td>          </td>
          <td>          </td>
          <td>  76%-100%</td>
        </tr>
      </tbody>
    </table>

Pour réduire la fourchette de confiance pour les petits
candidats, on peut s'inspirer d'un test statistique
comme le test du `chi-deux <http://fr.wikipedia.org/wiki/Test_du_%CF%87%C2%B2>`_.
On donne à chaque voix d'un candidat un poids inversement
proportionnel à son nombre de votants. Pour ce faire, j'ai
divisé chaque colonne par le nombre d'inscrits comptabilisés dans 
cette colonne (voir la matrice des inscrits du premier tour) puis
j'ai normalisé chaque ligne de la matrice du second tour de façon à ce qu'il
y ait le même nombre de voix aux premier et second tour dans chaque canton.
J'ai ensuite calculé la matrice de transfert des votes.

.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*transferts de votes, chaque vote est divisé <br /> par le nombre de voix obtenues par le candidat (aggrégation par cantons) en 2012*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>HOLLANDE</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>ARTHAUD</th>
          <td> 56%</td>
          <td>  7%</td>
          <td> 37%</td>
          <td>    </td>
        </tr>
        <tr>
          <th>Abstentions</th>
          <td>100%</td>
          <td>    </td>
          <td>    </td>
          <td>    </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td>    </td>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td> 34%</td>
          <td>    </td>
          <td> 36%</td>
          <td> 30%</td>
        </tr>
        <tr>
          <th>CHEMINADE</th>
          <td>100%</td>
          <td>    </td>
          <td>    </td>
          <td>    </td>
        </tr>
        <tr>
          <th>DUPONT-AIGNAN</th>
          <td> 14%</td>
          <td>  2%</td>
          <td> 20%</td>
          <td> 65%</td>
        </tr>
        <tr>
          <th>HOLLANDE</th>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
          <td>    </td>
        </tr>
        <tr>
          <th>JOLY</th>
          <td> 69%</td>
          <td>    </td>
          <td> 31%</td>
          <td>    </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td>    </td>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
        </tr>
        <tr>
          <th>MELENCHON</th>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
          <td>    </td>
        </tr>
        <tr>
          <th>POUTOU</th>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
          <td>    </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td>    </td>
          <td>    </td>
          <td>    </td>
          <td>100%</td>
        </tr>
      </tbody>
    </table>

Et on vérifie que les intervalles de confiance sont plus petits pour les 
derniers candidats. 

.. raw:: html

    <table border="1">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*intervalles de confiance des transferts de votes, <br /> chaque vote est divisé par le nombre de voix obtenues par le candidat (aggrégation par cantons) en 2012*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>HOLLANDE</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>ARTHAUD</th>
          <td>  45%- 69%</td>
          <td>   2%-  8%</td>
          <td>  27%- 48%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>Abstentions</th>
          <td>      100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td>          </td>
          <td>          </td>
          <td>   0%- 11%</td>
          <td>  89%-100%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td>  18%- 59%</td>
          <td>          </td>
          <td>  21%- 59%</td>
          <td>   5%- 40%</td>
        </tr>
        <tr>
          <th>CHEMINADE</th>
          <td>  93%-100%</td>
          <td>          </td>
          <td>          </td>
          <td>   0%-  7%</td>
        </tr>
        <tr>
          <th>DUPONT-AIGNAN</th>
          <td>   0%- 23%</td>
          <td>   0%-  5%</td>
          <td>   0%- 30%</td>
          <td>  54%-100%</td>
        </tr>
        <tr>
          <th>HOLLANDE</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>JOLY</th>
          <td>  49%- 92%</td>
          <td>          </td>
          <td>   8%- 51%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td>          </td>
          <td>   0%-  3%</td>
          <td>          </td>
          <td>  97%-100%</td>
        </tr>
        <tr>
          <th>MELENCHON</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>POUTOU</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td>          </td>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
        </tr>
      </tbody>
    </table>


Les mêmes résultats en 2007 laisse penser que les reports de voix étaient plus bruités :

.. raw:: html

    <table border="1" class="dataframe">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*intervalles de confiance des transferts de votes, <br /> chaque vote est divisé par le nombre de voix obtenues par le candidat (aggrégation par cantons) en 2007*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>ROYAL</th>
          <th>SARKOZY</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Abstentions</th>
          <td>  84%-100%</td>
          <td>        </td>
          <td>          </td>
          <td>   0%- 16%</td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td>   0%- 14%</td>
          <td>        </td>
          <td>  39%- 87%</td>
          <td>  10%- 59%</td>
        </tr>
        <tr>
          <th>BESANCENOT</th>
          <td>          </td>
          <td>        </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>BOVET</th>
          <td>   3%- 44%</td>
          <td>        </td>
          <td>   8%- 68%</td>
          <td>   4%- 67%</td>
        </tr>
        <tr>
          <th>BUFFET</th>
          <td>  18%- 41%</td>
          <td>        </td>
          <td>  33%- 71%</td>
          <td>   0%- 40%</td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td>  51%- 87%</td>
          <td>        </td>
          <td>   5%- 45%</td>
          <td>   0%- 13%</td>
        </tr>
        <tr>
          <th>LAGUILLER</th>
          <td>  61%- 91%</td>
          <td>        </td>
          <td>   0%- 17%</td>
          <td>   0%- 38%</td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td>          </td>
          <td>        </td>
          <td>          </td>
          <td>      100%</td>
        </tr>
        <tr>
          <th>NIHOUS</th>
          <td>   0%-  9%</td>
          <td> 0%-  6%</td>
          <td>  53%- 76%</td>
          <td>  16%- 41%</td>
        </tr>
        <tr>
          <th>ROYAL</th>
          <td>          </td>
          <td>        </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>SARKOZY</th>
          <td>          </td>
          <td>        </td>
          <td>          </td>
          <td>      100%</td>
        </tr>
        <tr>
          <th>SCHIVARDI</th>
          <td>   0%- 17%</td>
          <td> 0%-  4%</td>
          <td>   0%- 47%</td>
          <td>  40%- 98%</td>
        </tr>
        <tr>
          <th>VOYNET</th>
          <td>   0%- 65%</td>
          <td>        </td>
          <td>          </td>
          <td>  32%-100%</td>
        </tr>
        <tr>
          <th>de VILLIERS</th>
          <td>   0%- 13%</td>
          <td> 0%-  4%</td>
          <td>   0%- 25%</td>
          <td>  65%-100%</td>
        </tr>
      </tbody>
    </table>


Les élections en 2002 montrent des résultats
plutôt surprenants pour le candidats Chirac. 
L'hypothèse de proabilités de reports uniformes est 
probablement fausse dans ce cas même si ces résultats
paraissent dans l'ensemble sensés. C'est comme ci
les électeurs de Chirac du premier avaient considérés les élections
comme gagnées et n'avaient pas cru utile de se déplacer au second tour.

.. raw:: html

    <table border="1" class="dataframe">
        <tfoot><tr align="right">
        <td colspan="5">
        <div id="no-paging">*intervalles de confiance des transferts de votes, <br /> chaque vote est divisé par le nombre de voix obtenues par le candidat (aggrégation par cantons) en 2002*
        </div></td></tr>
        </tfoot>
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Abstentions</th>
          <th>Blancs et nuls</th>
          <th>CHIRAC</th>
          <th>LE PEN</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Abstentions</th>
          <td>      100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>BAYROU</th>
          <td>   0%- 19%</td>
          <td>          </td>
          <td>  81%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>BESANCENOT</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>BOUTIN</th>
          <td>   6%- 65%</td>
          <td>          </td>
          <td>  35%- 94%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>Blancs et nuls</th>
          <td>   0%- 48%</td>
          <td>          </td>
          <td>  52%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>CHEVENEMENT</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>CHIRAC</th>
          <td>      100%</td>
          <td>          </td>
          <td>          </td>
          <td>          </td>
        </tr>
        <tr>
          <th>GLUCKSTEIN</th>
          <td>   0%- 25%</td>
          <td>          </td>
          <td>  75%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>HUE</th>
          <td>   6%- 47%</td>
          <td>          </td>
          <td>  49%- 81%</td>
          <td>   3%- 11%</td>
        </tr>
        <tr>
          <th>JOSPIN</th>
          <td>   0%-100%</td>
          <td>          </td>
          <td>   0%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>LAGUILLER</th>
          <td>   0%-100%</td>
          <td>          </td>
          <td>   0%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>LE PEN</th>
          <td>   0%- 25%</td>
          <td>          </td>
          <td>   0%- 19%</td>
          <td>  68%-100%</td>
        </tr>
        <tr>
          <th>LEPAGE</th>
          <td>          </td>
          <td>          </td>
          <td>      100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>MADELIN</th>
          <td>   0%- 69%</td>
          <td>          </td>
          <td>  31%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>MAMERE</th>
          <td>   0%- 72%</td>
          <td>          </td>
          <td>  28%-100%</td>
          <td>          </td>
        </tr>
        <tr>
          <th>MEGRET</th>
          <td>  33%- 62%</td>
          <td>          </td>
          <td>          </td>
          <td>  38%- 67%</td>
        </tr>
        <tr>
          <th>SAINT-JOSSE</th>
          <td>          </td>
          <td>   5%- 12%</td>
          <td>  58%- 64%</td>
          <td>  27%- 33%</td>
        </tr>
        <tr>
          <th>TAUBIRA</th>
          <td>  48%- 72%</td>
          <td>          </td>
          <td>  28%- 52%</td>
          <td>          </td>
        </tr>
      </tbody>
    </table>
