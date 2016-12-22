

.. blogpost::
    :title: Deviner l'encoding d'un fichier
    :keywords: encoding, pandas
    :date: 2016-12-20
    :categories: pandas
    :lid: 
    
    Lire un fichier avec `pandas <http://pandas.pydata.org/>`_ 
    est parfois compliqué voire très frustrant parce que chaque source
    à sa propre façon de faire. Bref comment devenir 
    l'`encoding <https://en.wikipedia.org/wiki/Character_encoding>`_
    d'un fichier texte.
    
    ::
    
        import pandas
        df = pandas.read_csv("machin_tres_chiant.csv", 
                             sep="\t", 
                             encoding="UTF-16LE")

    Plutôt que de devenir fou, le plus simple est d'utiliser un module
    comme `chardet <http://chardet.readthedocs.io/en/latest/usage.html>`_
    qui retourne cette information avec l'exemple suivant :
    
    
    ::
    
        import chardet
        with open("machin_tres_chiant.csv", "rb") as f:
            raw = f.read()
        enc = chardet.detect(raw)
        print(enc)

