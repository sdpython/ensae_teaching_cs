# -*- coding: utf-8 -*-
"""
@file
@brief Helpers for blog classification
"""


privateKeyClassification = {
    "~recreative": ["\xE9conomie farfelue", "xaveir", "xavier", "xavier dupr\xE9", "litt\xE9rature",
                    "green website", "restaurant", "alimentation", "cuisine", "emploi", "discussion",
                    "wifi", "smart cities", "t\xE9l\xE9vision", "jeu", "jeux", "cin\xE9ma",
                    "d\xE9couverte", "cheminement", "\xE9conomie", "d\xE9mocratie", "d\xE9mographie",
                    "m\xE9decine", "th\xE9\xE2tre", "\xE9cole", "papa", "recreative", "video", "photo", "joke",
                    "tennis"],
    "~technical": ["python", "programming", "c", "p-value", "edit distance",
                   "latex", "vba", "javascript", "big data", "math\xE9matique",
                   "programmation", "programmer", "internet", "algorithm", "algorithme",
                   "extreme values", "C#", "c#", "c sharp", "csharp", "machine learning", "os", "r", "git",
                   "doon\xE9es"],
    "~ENSAE": ["ensae alumni", "data scientist", "ensae", "ENSAE", "enseignement", ],
}

privateKeyClassificationMandatory = list(privateKeyClassification.keys())


def classify_post(keywords, content):
    """
    returns a list of keywords as a classification
    - technical
    - recreative
    - English
    - French
    """
    available_classes = list(privateKeyClassification.keys())
    clean_keywords = [_.lower()
                      for _ in keywords if _ not in available_classes]

    # adds keywords in lower caase
    key = privateKeyClassification

    res_class = []
    for _ in clean_keywords:
        for k, v in key.items():
            if _ in v:
                res_class.append(k)
                # break

    return res_class + clean_keywords
