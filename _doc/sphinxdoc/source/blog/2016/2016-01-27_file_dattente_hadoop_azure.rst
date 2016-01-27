
.. _blogpost_azure_file_attente:

.. blogpost::
    :title: File d'attente sur Azure HD Insight
    :keywords: Hadoop, Azure, job, queue, HD Insight
    :date: 2016-01-27
    :categories: Azure
    
    La plupart du temps, un job reste coincé dans la file d'attente
    car celle-ci est pleine. Voici un code pour s'en assurer
    sur un cluster Azure HDInsight. A exécuter depuis un notebook.
    
    Connexion ::
    
        blobstorage = "..."
        blobpassword = "..."
        hadoop_server = "..."
        hadoop_password = "..."
        username = "..."

        import pyensae
        client, bs = %hd_open

    Liste d'attente ::
    
        res = client.job_queue()
        res.reverse()   # les derniers jobs d'abord
        
    On affiche les premiers jobs ::
    
        for i, r in enumerate(res[:20]):
            st = client.job_status(r["id"])
            print(i, r, st["status"]["state"],datetime.fromtimestamp(float(st["status"]["startTime"])/1000), st["status"]["jobName"])
            print(st["userargs"].get("file", None), st["profile"].get("jobName", None))
            
    Cela donne ::    

        0 {'detail': None, 'id': 'job_1451961118663_3126'} PREP 2016-01-26 21:57:28.756000 TempletonControllerJob
        wasb://..../scripts/pig/titi.pig TempletonControllerJob
        1 {'detail': None, 'id': 'job_1451961118663_3125'} PREP 2016-01-26 21:57:28.517999 TempletonControllerJob
        wasb://..../scripts/pig/pre_processing.pig TempletonControllerJob
        2 {'detail': None, 'id': 'job_1451961118663_3124'} PREP 2016-01-26 21:50:32.742000 TempletonControllerJob
        wasb://..../scripts/pig/titi.pig TempletonControllerJob
        3 {'detail': None, 'id': 'job_1451961118663_3123'} RUNNING 2016-01-26 21:46:57.219000 TempletonControllerJob
        wasb://..../scripts/pig/alg1.pig TempletonControllerJob
        4 {'detail': None, 'id': 'job_1451961118663_3122'} SUCCEEDED 2016-01-26 21:40:34.687999 PigLatin:pre_processing.pig
        None PigLatin:pre_processing.pig
        5 {'detail': None, 'id': 'job_1451961118663_3121'} RUNNING 2016-01-26 21:41:29.657000 TempletonControllerJob
        wasb://..../scripts/pig/Algo_LDA2.pig TempletonControllerJob
        6 {'detail': None, 'id': 'job_1451961118663_3120'} SUCCEEDED 2016-01-26 21:40:06.859999 TempletonControllerJob
        wasb://..../scripts/pig/alg1.pig TempletonControllerJob
        
    Et pour détruire un job ::
    
        client.job_kill("id")
        
    
