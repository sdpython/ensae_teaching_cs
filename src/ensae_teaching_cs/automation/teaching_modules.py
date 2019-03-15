# -*- coding: utf-8 -*-
"""
@file
@brief List of modules to maintain for the teachings.
"""


def get_teaching_modules():
    """
    List of teachings modules to maintain (CI + documentation).

    .. runpython::
        :showcode:

        from ensae_teaching_cs.automation import get_teaching_modules
        print('\\n'.join(sorted(get_teaching_modules())))
    """
    return ["pymlbenchmark", "_benchmarks", "ensae_teaching_dl", "machinelearningext",
            "lecture_citation", "botadi", "pyquickhelper", "jyquickhelper",
            "python3_module_template", "mathenjeu", "pymmails", "pymyinstall",
            "pyensae", "pyrsslocal", "pysqllike", "ensae_projects", "ensae_teaching_cs",
            "code_beatrix", "actuariat_python", "mlstatpy", "jupytalk", "teachpyx",
            "tkinterquickhelper", "cpyquickhelper", "pandas_streaming",
            "lightmlboard", "lightmlrestapi", "mlinsights", "pyenbc", "mlprodict",
            "papierstat", "sparkouille", "manydataapi", "csharpy", "csharpyml",
            "wrapclib",
            ]
