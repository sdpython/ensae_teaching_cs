


Installation de Spark en local
==============================

.. contents::
    :local:


Installation de Spark sous Windows
++++++++++++++++++++++++++++++++++

Ces instructions ont été testées le **2016/11/28**.
Il est possible que cela change un peu dans un futur proche.

Source `Installing Spark on a Windows PC <https://www.ukdataservice.ac.uk/media/604421/installing-spark-on-a-windows-pc.pdf>`_.

#. Installer `Java <https://java.com/en/download/>`_ (ou `Java 64 bit <https://java.com/en/download/manual.jsp>`_).
   Il faut faire attention car le setup a tendance à changer la page par défaut de votre navigateur.
#. Tester que Java est installé en ouvrant une fenêtre de ligne de commande et taper ``java``.
   Vous devriez avoir ceci : :ref:`fenêtre de commande <l-java-cmd>`.
#. Installer `Spark <http://spark.apache.org/downloads.html>`_.
   Il faut décompresser le fichier avec `7zip <http://www.7-zip.org/>`_
   dans le répertoire que vous avez choisi pour Spark.
#. Test *pyspark*. Ouvrir une ligne de commande,
   on ajoute si nécessaire à la variable d'environnement *PATH* le chemin vers
   l'interpréteur *python* :
   
   ::
   
        set PATH=%PATH%;c:\Python35_x64;c:\Python35_x64\Scripts
        cd <spark>\bin
        pyspark
        
   On obient :
    
   ::
    
        Welcome to
              ____              __
             / __/__  ___ _____/ /__
            _\ \/ _ \/ _ `/ __/  '_/
           /__ / .__/\_,_/_/ /_/\_\   version 2.0.2
              /_/

        Using Python version 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016 22:18:55)
        SparkSession available as 'spark'.
        >>>
        
#. Changer le fichier de configuration ``conf/log4j.properties.template``.
   *INFO* ou *WARN* doivent être remplacés par *ERROR*.

   :: 
    
        log4j.rootCategory=INFO, console
        log4j.logger.org.spark_project.jetty=WARN
        log4j.logger.org.apache.spark.repl.SparkIMain$exprTyper=INFO
        log4j.logger.org.apache.spark.repl.SparkILoop$SparkILoopInterpreter=INFO  

#. Télécharger le fichier *winutils.exe* dans le répertoire *bin* depuis cet emplacement :
   `winutils.exe <https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe>`_.
#. Ajouter deux variables environnements pointant sur le répertoire *bin* :

   :: 

        set HADOOP_HOME=C:\username\spark\spark-2.0.2-bin-hadoop2.7
        set SPARK_HOME=C:\username\spark\spark-2.0.2-bin-hadoop2.7
        
#. Ajouter ce même répertoire à la variable d'environnement ``%PATH%`` :

   ::
   
        set PATH=%PATH%;C:\username\spark\spark-2.0.2-bin-hadoop2.7\bin
   
#. Dernier test, on exécute (il faut créer le répertoire ``\tmp\hive``) :

   ::
   
        winutils.exe ls \tmp\hive
        
   Et cela donne :
   
   ::
   
        drwxrwxrwx 1 domain\username domain\username Users 0 Dec  6 2016 \tmp\hive
        
   Si ce n'est pas le cas, il faut exécuter :
   
   ::
   
        winutils.exe chmod -R 777 \tmp\hive
        
#. Test final : ``pyspark``.

L'ensemble de ces instructions est regroupés dans le script :
`run_pyspark_notebook.bat <https://github.com/sdpython/ensae_teaching_cs/blob/master/run_pyspark_notebook.bat>`_.


.. _l-petit-exemple-pyspark:

Petit test avec wordcount
+++++++++++++++++++++++++

Pour vérifier que tout fonctionne, on peut exécuter ce script sur n'importe quel fichier texte
(extrait de `Apache Spark Examples <http://spark.apache.org/examples.html>`_) :

::

    text_file = sc.textFile("fichier.txt")
    counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("fichier.out.txt")
    
Si tout se passe bien, un répertoire *fichier.out.txt* est créé avec les fichiers :

::

    _SUCCESS
    part-00000
    part-00001
    
Spark et notebook
+++++++++++++++++
    
Pour utiliser Spark depuis un notebook, il suffit de spécifier une variable d'environnement
avant de lancer *pyspark* :
   
::

    set PYSPARK_DRIVER_PYTHON=jupyter-notebook
    
Et pour spécifier un répertoire par défaut, il suffit d'exécuter `pyspark`
depuis ce répertoire.



Installation de Spark sous Linux
++++++++++++++++++++++++++++++++

Ces instructions ont été testées le **2016/12/01**.
Il est possible que cela change un peu dans un futur proche.

Source : `Install Apache Spark on Ubuntu-14.04 <http://blog.prabeeshk.com/blog/2014/10/31/install-apache-spark-on-ubuntu-14-dot-04/>`_

Toutes les étapes sont à réaliser depuis la ligne de commande.
Elles sont décrites et ont été testées pour la distribution 
`Ubuntu 16.04 <http://releases.ubuntu.com/16.04/>`_.
L'utilisateur peut passer une étape si sa distribution actuelle est
déjà mise à jour ou possède déjà l'outil à installer.
Il faudra mettre à jour les numéros de version et les chemins
en fonction de vos choix lors de l'installation.


#. Mise à jour de la machine Ubuntu : 
  
   ::
   
        sudo apt-get update
        
#. Installer `Java <https://www.java.com/en/>`_ 
   (`instructions <http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html>`_),
   il faut dire à Ubuntu où trouver Java (Oracle) avec `sudo add-apt-repository ...`,
   dire à Ubuntu de prendre en cmopte cette modification `sudo apt-get update`
   et installer Java 8 `sudo apt-get install oracle-java8-installer`.
   En résumé :
    
   ::
    
        sudo add-apt-repository ppa:webupd8team/java
        sudo apt-get update
        sudo apt-get install oracle-java8-installer

#. Installer `Scala <https://www.scala-lang.org/>`_ :

   ::
   
        sudo apt install scala
        
#. Installer `Anaconda 3 <https://www.continuum.io/anaconda-overview>`_, 
   on récupère le lien depuis cette page 
   `Anaconda/downloads <https://www.continuum.io/downloads>`_ :

   ::

        wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
        bash Anaconda3-4.2.0-Linux-x86_64.sh
        anaconda3/bin/conda update --all
    
#. Aller à la page `Spark/downloads <http://spark.apache.org/downloads.html>`_,
   récupérer le lien pour la dernière version, le télécharger, puis l'installer :
   
   :: 
   
        wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.7.tgz
        tar xvf spark-2.0.2-bin-hadoop2.7.tgz
        
#. Définir les chemins d'accès (les deux premières lignes sont à supprimer si vous souhaitez
   utiliser la ligne de commande et non le notebook :

   ::
   
        export PYSPARK_DRIVER_PYTHON=anaconda3/bin/jupyter
        export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

        export PYSPARK_PYTHON=anaconda3/bin/python
        export PATH=anaconda3/bin:$PATH
        
#. Exécuter *pyspark* : ``spark-2.0.2-bin-hadoop2.7/bin/pyspark``
    
    
Il ne reste plus qu'à tester le :ref:`l-petit-exemple-pyspark`
pour vérifier que tout marche bien.
Les versions utilisées pour ce test sont les suivantes.

::

    java -version
    scala -version

Ce qui donne :
    
::

    java version "1.8.0_111"
    Java(TM) SE Runtime Environment (build 1.8.0_111-b14)
    Java HotSpot(TM) 64-Bit Server VM (build 25.111-b14, mixed mode)
    Scala code runner version 2.11.6 -- Copyright 2002-2013, LAMP/EPFL

C'est souvent la première information qu'on vérifie lorsqu'une erreur se produit.
Ce tutoriel a utilisé les dernières versions disponibles.

Spark DataFrame
+++++++++++++++

`Spark SQL, DataFrames and Datasets Guide <http://spark.apache.org/docs/latest/sql-programming-guide.html>`_

::

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("nimportequoi").getOrCreate()
    
    df = spark.read.csv("tbl_type_credit.txt")
    df.show()



Script batch de lancement
+++++++++++++++++++++++++

La liste des instructions pour lancer pyspark est assez longue et fastidieuse mais il est possible
de l'écrire une bonne fois pour toute dans un script batch, d'extension ``.bat`` ou ``.cmd`` sous Windows
et ``.sh`` sous Linux et Mac. Il suffit de créer ce fichier et de l'enregistrer sur le bureau
pouvoir lancer pyspark en un double clic.


Windows
^^^^^^^

Voici ce script pour Windows.
Il faut remplacer les trois premiers chemins 
avec ceux de son ordinateur.
Il faut éviter d'appeler ce fichier ``pypark.bat`` ou ``pyspark.cmd``
car le système va le confondre avec celui du même nom installé par Spark.

``run_pypspark.bat``

::

    set local_pyspark=c:\%USERNAME%\spark\spark-2.0.2-bin-hadoop2.7
    set local_python=c:\Python35_x64
    set notebook_dir=c:\Users\username

    :hive:
    if NOT EXIST \tmp mkdir \tmp
    if NOT EXIST \tmp\hive mkdir \tmp\hive

    :update_path:
    set HADOOP_HOME=%local_pyspark%
    set SPARK_HOME=%local_pyspark%
    set PATH=%local_python%;%local_python%\Scripts;%PATH%
    set PATH=%PATH%;%local_pyspark%\bin
    set PYSPARK_PYTHON=%local_python%\python
    set SPARK_HIVE=true

    @echo HADOOP_HOME=%HADOOP_HOME%
    @echo PYTHONPATH=%PYTHONPATH%
    @echo PYSPARK_PYTHON=%PYSPARK_PYTHON%
    @echo SPARK_HIVE=%SPARK_HIVE%
    @echo SPARK_HOME=%SPARK_HOME%

    :wintutils:
    winutils.exe chmod -R 777 \tmp\hive
    winutils.exe ls \tmp\hive

    :run_pyspark:
    set PYSPARK_DRIVER_PYTHON=jupyter-notebook
    if NOT EXIST %local_pyspark% @echo Not found: %local_pyspark%
    
    pushd %notebook_dir%
    %local_pyspark%\bin\pyspark.cmd
    popd

Linux
+++++

Voici ce script pour Linux.
Il faut remplacer les trois premiers chemins 
avec ceux de son ordinateur.
Il faut éviter d'appeler ce fichier ``pypark.sh``
car le système va le confondre avec celui du même nom installé par Spark.
Il faut le lancer depuis le répertoire contenant les notebooks.

``run_pypspark.sh``

::

    export local_pyspark=/usr/username/Spark
    export local_python=/user/username/anaconda3

    export PYSPARK_DRIVER_PYTHON=$local_python/bin/jupyter
    export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
    export PYSPARK_PYTHON=$local_path/bin/python
    export PATH=$local_path/bin:$local_pyspark:$PATH

    pyspark



Erreurs rencontrées avant les premiers scripts
++++++++++++++++++++++++++++++++++++++++++++++


Py4JJavaError: An error occurred while calling o162.csv.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:: 

    Py4JJavaError: An error occurred while calling o162.csv.
    : java.lang.RuntimeException: java.lang.RuntimeException: Unable to instantiate org.apache.hadoop.hive.ql.metadata.SessionHiveMetaStoreClient"
    
Il est suggéré dans ce cas de supprimer le répertoire ``metastore_db``.

    
Erreur : Cannot run program "python"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Il vous manque probablement ``PYSPARK_PYTHON``.
Voici ce que vous devriez avoir :

::

    LOCAL_PYSPARK            = c:\<username>\spark\spark-2.0.2-bin-hadoop2.7
    PYSPARK_DRIVER_PYTHON    = jupyter-notebook
    PYSPARK_PYTHON           = c:\Python35_x64\python
    PYSPARK_SUBMIT_ARGS      = "--name" "PySparkShell" "pyspark-shell" 
    SPARK_CMD                = set PYSPARK_SUBMIT_ARGS="--name" "PySparkShell" "pyspark-shell" && jupyter-notebook 
    SPARK_ENV_LOADED         = 1
    SPARK_HIVE               = true
    SPARK_HOME               = c:\<username>\spark\spark-2.0.2-bin-hadoop2.7\bin\..
    SPARK_JARS_DIR           = "c:\<username>\spark\spark-2.0.2-bin-hadoop2.7\bin\..\jars"
    SPARK_SCALA_VERSION      = 2.10
    _SPARK_CMD_USAGE         = Usage: bin\pyspark.cmd [options]
    
The trust relationship between this workstation and the primary domain failed (Windows)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cette survient lorsqu'on exécute :

::

    sdf = spark.read.csv("data_adult.txt") #, sep="\t", encoding="utf-8")

Cette erreur est un peu mystérieuse à vrai dire. J'ai trouvé ce 
`lien <https://support.microsoft.com/en-us/kb/2771040>`_ qui donne 
une solution sans vraiment expliquer le problème. Dans mon cas, j'ai créé un nouveau compte
sur l'ordinateur et je l'ai supprimé. J'ai redémarré l'ordinateur et cela a disparu.


Erreurs rencontrées durant l'exécution des premiers scripts
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Erreur : Output directory  file:/... already exists
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Spark n'aime pas écrire des données dans un RDD qui existe déjà. 
Il faut le supprimer. Tout dépend de l'environnement où on se trouve, 
sur Hadoop ou en local.

Failed to start database 'metastore_db' with class loader    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    Caused by: java.sql.SQLException: Failed to start database 'metastore_db' with class loader org.apache.spark.sql.hive.client.IsolatedClientLoader$$anon$1@79af752f, see the next exception for details.
            at org.apache.derby.impl.jdbc.SQLExceptionFactory.getSQLException(Unknown Source)
            at org.apache.derby.impl.jdbc.SQLExceptionFactory.getSQLException(Unknown Source)
            at org.apache.derby.impl.jdbc.Util.seeNextException(Unknown Source)
            at org.apache.derby.impl.jdbc.EmbedConnection.bootDatabase(Unknown Source)
            at org.apache.derby.impl.jdbc.EmbedConnection.<init>(Unknown Source)    

Il est suggéré dans ce cas de supprimer le répertoire ``metastore_db``.
Il faut redémarrer le notebook si jamais ce n'est pas possible.


