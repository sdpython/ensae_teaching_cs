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
<b>{{ col_subject }}</b><br /><br />
{{ subject }}<br /><br />
<b>{{ col_pitch}}</b><br /><br />
{{ pitch }}<br /><br />
<b>{{ col_code}}</b><br /><br />
{{ code }}<br /><br />
<b>{{ text_comments }}</b><br /><br />
{{ comments }}<br /><br />
{{ end }}
"""


def enumerate_feedback(df1, df2, col_group="Groupe", col_subject="Sujet",
                       col_pitch="Pitch", col_code="Code", col_mail="Mail",
                       col_name="Nom", subject="Projet informatique, feedback sur le pitch",
                       begin="Bonjour,\n\nVoici mon feedback sur votre pitch. Ce mail est automatisé. Veuillez vérifier les informations.\n\n",
                       end="Xavier", text_comments="Remarques générales",
                       template=template_mail_feedback, engine="jinja2", exc=True, fLOG=noLOG):
    """
    sends feedback to students

    @param      df1             first dataframe
    @param      df2             a draframe or a list or a list of general comments to add at the end
    @param      col_group       name of the column which contains the group definition
    @param      col_subject     name of the column which contains the subject of each group
    @param      col_pitch       name of the column which contains the comments on the report or the pitch
    @param      col_code        name of the column which contains the comments on the code
    @param      col_mail        name of the column which contains the mail of the members
    @param      col_name        name of the column which contains the names of the members
    @param      subject         subject of the mail
    @param      intro           beginning of the mail
    @param      template        template of the mail
    @param      text_comments   sentance before the general comments
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
    def sums(spl):
        spl = [_ for _ in spl if isinstance(_, str) if "??" not in _]
        return ";".join(spl)

    def sums2(spl):
        spl = [_ for _ in spl if isinstance(_, str)]
        return ", ".join(spl)

    if df2 is not None:
        if isinstance(df2, (list, tuple)):
            comments = "\n".join(df2)
        else:
            comments = "\n\n".join(df2[df2.columns[0]])
    else:
        comments = ""
    comments = comments.replace("\n", "<br />\n")
    begin = begin.replace("\n", "<br />\n")
    end = end.replace("\n", "<br />\n")

    group = df1.groupby(col_group).agg({col_mail: sums, col_name: sums2,
                                        col_subject: sums, col_pitch: sums,
                                        col_code: sums})
    common = dict(begin=begin, col_group=col_group, col_pitch=col_pitch,
                  col_subject=col_subject, col_code=col_code, col_name=col_name,
                  text_comments=text_comments, comments=comments, end=end, col_mail=col_mail)
    common_rev = {v: k for k, v in common.items()}

    for row in group.itertuples(index=False):
        context = common.copy()
        mail = None
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


def enumerate_send_email(mailbox, subject, fr, df1, df2, cc=None, delay=[1000, 1500],
                         delay_sending=False, exc=True, skip=0, only=None, **params):
    """
    Send feedback to students

    @param      mailbox         mailbox, see `create_smtp_server <http://www.xavierdupre.fr/app/pymmails/helpsphinx/pymmails/sender/email_sender.html?pymmails.sender.email_sender.create_smtp_server>`_
    @param      fr              from
    @param      df1             first dataframe
    @param      df2             a draframe or a list or a list of general comments to add at the end
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
    for mails, html, text in enumerate_feedback(df1, df2, exc=exc, **params):
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
