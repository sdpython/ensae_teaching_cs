


Spark
=====


Installation de Spark en local
++++++++++++++++++++++++++++++

**Windows**

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


Spark DataFrame
+++++++++++++++

`Spark SQL, DataFrames and Datasets Guide <http://spark.apache.org/docs/latest/sql-programming-guide.html>`_

::

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.appName("nimportequoi").getOrCreate()
    
    df = spark.read.csv("tbl_type_credit.txt")
    df.show()
