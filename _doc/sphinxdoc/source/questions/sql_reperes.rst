
Quelques repères de SQL
======================

Source : `Cours ensae - structure de donnée <http://www.xavierdupre.fr/enseignement/complements/cours_structure_donnee.pdf>`_,
Nicolas Rousset

Base de donnees usuelles
------------------------

La majeur partie des bases de donnees actuelles
(`PostGres <https://www.postgresql.org/>`_,
`MySql <https://www.mysql.com/>`_,
`SQL Server <https://www.microsoft.com/en-us/sql-server/>`_
`Oracle <https://www.oracle.com/index.html>`_,
`MariaDB <https://mariadb.com/>`_, ...)
sont des bases de données relationnelles et transactionnelles "classiques".
Elles assurent la cohérence des données selon les principes définies par l'acronyme
`ACID <https://en.wikipedia.org/wiki/ACID>`_.
Ces principes impliquent des mécanismes assez coûteux,
notamment les `tablespace <https://fr.wikipedia.org/wiki/Tablespace>`_.

Notion de transaction
---------------------

Une transaction est un ensemble de requête qui amène la
base d'un état cohérent vers un autre état cohérent.
Par exemple pour une base de donnée comptable, cela pourrait être :

::

    INSERT into DEBIT values( ... );
    INSERT into CREDIT values( ... );

    INSERT into DEPARTEMENT( 78, 'Yvelines', 'Versailles' );
    INSERT into PERSON( 'Martin', 'Jacques', 32, 13245, 78 );

Principes ACID
--------------

- **Atomicité** : une transaction doit être exécuté totalement ou pas du tout.
- **Cohérence** : une transaction doit amener la base d'un état respectant
  toutes les règles de la base vers un autre état respectant ces mêmes règles.
- **Isolation** : les transactions doivent être isolées les unes des autres,
  c'est à dire que les résultats d'une exécution parallèle doivent correspondre
  à ceux d'une execution séquentielle.
- **Durabilité** : Les données en base doivent être stockées de façon permanente,
  de façon à supporter une panne de courant.

Problème des tablespace
-----------------------

La propriété d'isolation peut être très coûteuse avec des grosses bases
de données, lorsque le volume d'information et les temps d'exécution deviennent importants.

::

    SELECT * FROM DOCUMENT WHERE AGENCY_CODE = 'FR0076' and issue_date = '2014-10-19';

    UPDATE DOCUMENT SET CANCELLED = 1 WHERE ID = 2001567345;

Le principe d'isolation signifie que la première requête doit renvoyer un
résultat identique que la deuxième soit faite ou non.
Comment cela est-il possible ? En fait on va devoir se souvenir de
l'état de la base de donnée au moment où la première requête a été lancée.
C'est le principe des *tablespaces*, qui peut être très coûteux.

Non ACID
--------

Les propriétés ACID sont coûteuses à maintenir.
Un des inconvénients est qu'on peut modifier des données,
les anciennes valeurs sont écrasées par les nouvelles. Aucune
lecture ne doit intervenir pendant la modification sous peine d'aboutir
à un mauvais calcul.

La notion d'index est beaucoup plus difficile à maintenir sur un
cluster car les fichiers sont volumineux et les accès coûteux. On préfère
alors construire des bases d'événements. La mise bout à bout
de ces événements permet d'obtenir l'état du système. Le montant
d'un compte en banque est la somme des transactions qui ont eu lieu.
Comme les données ne sont jamais modifiées, il n'y a pas de risques de
considérer une valeur en train d'être modifiées.
