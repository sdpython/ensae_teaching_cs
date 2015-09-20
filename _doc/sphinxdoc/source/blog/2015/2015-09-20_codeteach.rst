

.. blogpost::
    :title: Petits codes qu'on écrit parfois
    :keywords: code, élèves, mail, petit code
    :date: 2015-09-20
    :categories: setup, enseignement
    
    Je dois créer un sous-répertoire par élève et je ne retrouve
    jamais ce petit code que j'écris chaque année pour le faire::
    
        import os
        fold  = "."
        mails = """prenom1.nom1@ensae.fr;prenom2.nom2@ensae.fr"""
        lines = [_.split("@")[0].strip() for _ in mails.split(";")]
        lines = [_ for _ in lines if _]
        for add in lines:
            os.makedirs(os.path.join(fold, add))