


Spark
=====

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
   `winutils.exe <https://github.com/steveloughran/winutils/blob/master/hadoop-2.6.0/bin/winutils.exe>`_.
#. Ajouter deux variables environnements pointant sur le répertoire *bin* :

   :: 

        set HADOOP_HOME=C:\xadupre\spark\spark-2.0.2-bin-hadoop2.7
        set SPARK_HOME=C:\xadupre\spark\spark-2.0.2-bin-hadoop2.7
        
#. Ajouter ce même répertoire à la variable d'environnement ``%PATH%`` :

   ::
   
        set PATH=%PATH%;C:\xadupre\spark\spark-2.0.2-bin-hadoop2.7\bin
   
#. Test final : ``pyspark``.

.. _l-petit-exemple-pyspark:

Petit test avec wordcount
+++++++++++++++++++++++++

Pour vérifier que tout fonctionne, on peut exécuter ce script sur n'importe quel fichier texte
(extrait de `Apache Spark Examples <http://spark.apache.org/examples.html>`_) :

::

    text_file = sc.textFile("fichier.txt")
    counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("fichier.out.txt")
    
Si tout ce passe bien, un répertoire *fichier.out.txt* est créé avec les fichiers :

::

    _SUCCESS
    part-00000
    part-00001
    
#. Pour utiliser Spark depuis un notebook, il suffit de spécifier une variable d'environnement
   avant de lancer *pyspark* :
   
   ::
   
        set PYSPARK_DRIVER_PYTHON=jupyter-notebook


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


#. Mise à jour de la machine Ubuntu : ``sudo apt-get update``
#. Installer de java (`instructions <http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html>`_)

   * Dire à Ubuntu où trouver Java (Oracle) ``sudo add-apt-repository ppa:webupd8team/java``
   * Mettre à jour Ubuntu : ``sudo apt-get update``
   * Installer Java 8 : ``sudo apt-get install oracle-java8-installer``
    
   ::
    
        sudo add-apt-repository ppa:webupd8team/java
        sudo apt-get update
        sudo apt-get install oracle-java8-installer

#. Installer `Scala <https://www.scala-lang.org/>`_ : ``sudo apt install scala``
#. Installer `Anaconda 3 <https://www.continuum.io/anaconda-overview>`_, 
   on récupère le lien depuis cette page 
   `Anaconda/downloads <https://www.continuum.io/downloads>`_ :

   ::

        wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
        bash Anaconda3-4.2.0-Linux-x86_64.sh
        anaconda3/bin/conda update --all
    
#. Aller à la page `Spark/downloads <http://spark.apache.org/downloads.html>`_ e
   récupérer le lien pour la dernière version puis le télécharger :
   ``wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.2-bin-hadoop2.7.tgz``
#. Installer *Spark* : ``tar xvf spark-2.0.2-bin-hadoop2.7.tgz``
#. Définir les chemins d'accès (les deux premières lignes sont à supprimer si vous souhaitez
   utiliser la ligne de commande et non le notebook :

   ::
   
        export PYSPARK_DRIVER_PYTHON=anaconda3/bin/ipython
        export PYSPARK_DRIVER_PYTHON_OPTS="notebook"

        export PYSPARK_PYTHON=anaconda3/bin/python
        export PATH=anaconda3/bin:$PATH
        
#. Exécuter *pyspark* : ``spark-2.0.2-bin-hadoop2.7/bin/pyspark``
    

Voici les versions utilisées pour ce test :

::

    java -version
    scala -version

Ce qui donne :
    
::

    java version "1.8.0_111"
    Java(TM) SE Runtime Environment (build 1.8.0_111-b14)
    Java HotSpot(TM) 64-Bit Server VM (build 25.111-b14, mixed mode)
    Scala code runner version 2.11.6 -- Copyright 2002-2013, LAMP/EPFL
    
Il ne reste plus qu'à tester le :ref:`l-petit-exemple-pyspark`
pour vérifier que tout marche bien.


Spark DataFrame
+++++++++++++++

`Spark SQL, DataFrames and Datasets Guide <http://spark.apache.org/docs/latest/sql-programming-guide.html>`_

::

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("nimportequoi").getOrCreate()
    
    df = spark.read.csv("tbl_type_credit.txt")
    df.show()
