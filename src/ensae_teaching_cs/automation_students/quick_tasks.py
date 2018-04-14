# -*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to grab mails from students about projects.
"""


def build_mailing_list(names, domain, format="{first}.{last}@{domain}"):
    """
    Infers mails from a list of names.

    @param      names       list of strings
    @param      domain      something like ``ensae.fr``.
    @param      format      mail format
    @return                 list of mails

    Examples :

    ::

        DUPRE Xavier

    Everything upper case is the last name,
    everything lower case is the first name.
    """
    mails = []
    for name in names:
        words = name.split()
        first = []
        last = []
        for w in words:
            if w.upper() == w:
                last.append(w)
            else:
                first.append(w)
        first = ".".join(s.lower() for s in first)
        last = ".".join(s.lower() for s in last)
        mail = format.format(first=first, last=last, domain=domain)
        mails.append(mail)
    return mails
