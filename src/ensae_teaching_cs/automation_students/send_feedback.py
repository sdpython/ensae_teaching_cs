#-*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to grab mails from students about projects.
"""

import time
import random
from pyquickhelper.loghelper import noLOG
from pyquickhelper.texthelper.templating import apply_template
from pymmails.sender import send_email


template_mail_feedback = """
{{ begin }}
<br /><br />
<b>{{ col_name }}</b><br /><br />
{{ name }}<br /><br />
{{ content }}
<br /><br />
{{ end }}
"""

template_mail_columns = "<b>{{ key }}</b><br />{{ value }}<br />\n"


def enumerate_feedback(df1, col_group="Groupe",
                       col_mail="Mail", col_name="Name",
                       cols=["Sujet", "Rapport", "Code", "Soutenance"],
                       subject=None, begin=None, end=None, 
                       template=template_mail_feedback,
                       template_col=template_mail_columns,
                       engine="jinja2", exc=True, fLOG=noLOG):
    """
    sends feedback to students

    @param      df1             dataframe
    @param      col_group       name of the column which contains the group definition
    @param      col_mail        name of the column which contains the mail of the members
    @param      col_name        name of the column which contains the names of the members
    @param      cols            list of columns to add to the mails, if there are multiple values
                                per group, they will be joined by space or another separator
                                if an element in this list is a tuple ``(col_name, sep)``
    @param      subject         subject of the mail
    @param      begin           beginning of the mail
    @param      template        template of the mail
    @param      template_col    template for additional columns, the outcome will be joined
                                to fill ``{{ content }}`` in the other template
    @param      engine          engine for the template
    @param      exc             raise an exception if there is no mail
    @return                     enumerate mails content as tuple *(mail, html, text)*

    Example of dataframe containing feedback:

    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    | Mail | Name      | Groupe | Sujet                                 | Pitch                                                                                                                                                                                                                                                             | Code                                                                                                                                             |
    +======+===========+========+=======================================+===================================================================================================================================================================================================================================================================+==================================================================================================================================================+
    |      | AAA bbb   | 1      |                                       |                                                                                                                                                                                                                                                                   |                                                                                                                                                  |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | ABA ccc   | 1      | jeu de hex                            | ok                                                                                                                                                                                                                                                                | ok                                                                                                                                               |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | VVV uuu   | 2      |                                       |                                                                                                                                                                                                                                                                   |                                                                                                                                                  |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | ZZZZ xxxx | 2      | élections US, twitter, nuages de mots | ok                                                                                                                                                                                                                                                                | ok                                                                                                                                               |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | GGG ffff  | 3      | distribution des sièges dans un avion | ok                                                                                                                                                                                                                                                                | Les print peuvent être remplacés par une autre fonction afin de désactiver les print qui ne servent qu'à la mise au point.                       |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | ??        | 31     |                                       |                                                                                                                                                                                                                                                                   |                                                                                                                                                  |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
    |      | RRRR yyyy | 31     | analyse de texte / nuage de mots      | Il faut éviter le code dans le contenu du pitch. Le pitch est un peu flou quant aux raisons qui vous poussent à développer votre propre tokenizer. A bien justifier avant de vous lancer dans ce type de travail et ne pas oublier la question de son évaluation. | L'interface graphique est-elle indispensable ? Le code alterne fonction, lecture de texte. N'hésitez pas à séparer les deux pour le rendu final. |
    +------+-----------+--------+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

    """
    
    if begin is None:
        raise ValueError("begin cannot be None, it should be string.")
    if end is None:
        raise ValueError("end cannot be None, it should be you signature.")
    if subject is None:
        raise ValueError("subject cannot be None, it should be the subject of the mail.")
    
    def sums(spl):
        spl = [_ for _ in spl if isinstance(_, str) if "??" not in _]
        return ";".join(spl)

    def sums2(spl):
        spl = [_ for _ in spl if isinstance(_, str)]
        return ", ".join(spl)

    def sums3(spl, sep):
        spl = [_ for _ in spl if isinstance(_, str)]
        return sep.join(spl)

    begin = begin.replace("\n", "<br />\n")
    end = end.replace("\n", "<br />\n")

    aggs = {col_mail: sums, col_name: sums2}
    for c in cols:
        if isinstance(c, tuple):
            aggs[c[0]] = lambda s, sep=c[1]: sums3(s, sep)
        else:
            aggs[c] = lambda s: sums3(s, " ")

    group = df1.groupby(col_group).agg(aggs)
    common = dict(begin=begin, col_group=col_group, col_name=col_name, col_mail=col_mail, end=end)
    common_rev = {v: k for k, v in common.items()}
    lc = list(group.columns)
    colsi = [lc.index(c[0] if isinstance(c, tuple) else c) for c in cols]

    for row in group.itertuples(index=False):
        # key, value pairs
        content = []
        for c, i in zip(cols, colsi):
            cn = c[0] if isinstance(c, tuple) else c
            ct = dict(key=cn, value=row[i])
            text = apply_template(template_col, ct, engine=engine)
            content.append(text)
            
        # main mail
        context = common.copy()
        context["content"] = content
        mail = None
        
        # rest of columns
        for k, v in zip(group.columns, row):
            if k == col_mail:
                mail = v
            k = common_rev.get(k, k)
            if k.startswith("col_"):
                k = k[4:]
            context[k] = v
        text = apply_template(template, context, engine=engine)
        if mail is None or "@" not in mail:
            if exc:
                raise ValueError("No mail for:\n" + text)
            else:
                fLOG("No mail for:\n" + text)
        html = ('<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>\n' +
                text + "\n</body></html>\n")
        text = text.replace("<b>", "").replace(
            "</b>", "").replace("<br />", "\n")
        yield (mail, html, text)


def enumerate_send_email(mailbox, subject, fr, df1, cc=None, delay=[1000, 1500],
                         delay_sending=False, exc=True, skip=0, only=None, **params):
    """
    Send feedback to students

    @param      mailbox         mailbox, see `create_smtp_server <http://www.xavierdupre.fr/app/pymmails/helpsphinx/pymmails/sender/email_sender.html?pymmails.sender.email_sender.create_smtp_server>`_
    @param      fr              from
    @param      df1             first dataframe
    @param      cc              additional receivers
    @param      delay           random delay between two mails
    @param      delay_sending   returns functions
    @param      exc             raise exception when mail is empty
    @param      skip            skip the first mail
    @param      only            send only to these groups (group id)
    @param      params          see @see fn enumerate_feedback
    @return                     enumerate mails

    Code example::

        import pandas
        import sys
        import os

        cc = ["cc@cc.org"]
        sujet = "Projet informatique, feedback sur le pitch"
        only = None # {28, 20, 19}

        from pyquickhelper.loghelper import fLOG
        fLOG(OutputPrint=True)

        from ensae_teaching_cs.automation_students import enumerate_feedback, enumerate_send_email
        import pymmails

        df = pandas.read_excel("groupes_eleves_pitch.xlsx", sheetname=0)
        comment = pandas.read_excel("groupes_eleves_pitch.xlsx", sheetname=1, header=None)


        mailbox = pymmails.sender.create_smtp_server("gmail", "xavier.dupre", "****")
        mails = enumerate_send_email(mailbox, sujet, "xavier.dupre AT gmail.com",
                                          df, comment, exc=True, fLOG=fLOG, delay_sending=False,
                                          cc=cc, only=only)
        mailbox.close()

    """
    loop = 0
    for mails, html, text in enumerate_feedback(df1, exc=exc, subject=subject, **params):
        if loop < skip:
            loop += 1
            continue
        if only is not None and loop not in only:
            loop += 1
            continue
        if mails is None or "@" not in mails:
            # if there is an issue, it should been cautch by the previous
            # function (we skip)
            continue
        if not delay_sending and "fLOG" in params:
            params["fLOG"](loop, "send mail to ", mails)
        res = send_email(mailbox, fr=fr, to=mails.split(";"), cc=cc, delay_sending=delay_sending,
                         body_html=html, body_text=text, subject=subject)
        if delay_sending:
            def delay():
                if "fLOG" in params:
                    params["fLOG"](loop, "send mail to ", mails)
                res()
                rnd = random.randint(*delay)
                time.sleep(rnd / 1000.0)
            yield delay
        else:
            yield res
            rnd = random.randint(*delay)
            time.sleep(rnd / 1000.0)
        loop += 1
