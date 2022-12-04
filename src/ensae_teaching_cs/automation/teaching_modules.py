# -*- coding: utf-8 -*-
"""
@file
@brief List of modules to maintain for the teachings.
"""


def get_teaching_modules(branch=True):
    """
    List of teachings modules to maintain (CI + documentation).

    :param branch: the default branch is usually master but could
        be main. If False, the branch name is not returned,
        otherwise the module name is `module:branch`.

    .. runpython::
        :showcode:

        from ensae_teaching_cs.automation import get_teaching_modules
        print('\\n'.join(sorted(get_teaching_modules())))
    """
    mods = ['deeponnxcustom:main', 'onnxcustom',
            "pymlbenchmark", "_benchmarks", "ensae_teaching_dl",
            "lecture_citation", "pyquickhelper", "jyquickhelper",
            "python3_module_template", "pymmails", "pymyinstall",
            "pyensae", "pyrsslocal", "ensae_projects", "ensae_teaching_cs",
            "code_beatrix", "actuariat_python", "mlstatpy", "jupytalk", "teachpyx",
            "tkinterquickhelper", "cpyquickhelper", "pandas_streaming",
            "mlinsights", "pyenbc", "mlprodict", "mloptonnx",
            "papierstat", "sparkouille", "manydataapi",
            "wrapclib", "myblog", "_check_python_install", "onnxortext"]
    if not branch:
        mods = [m.split(':', maxsplit=1)[0] for m in mods]
    return mods
