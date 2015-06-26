"""
@file
@brief Builds a setup for the teachings
"""
try:
    import pymyinstall
except ImportError:
    import sys
    sys.path.append("../pymyinstall/src")
    import pymyinstall

try:
    import pyquickhelper
except ImportError:
    import sys
    sys.path.append("../pyquickhelper/src")
    import pyquickhelper


if __name__ == "__main__":
    import sys
    sys.path.append("src")

    from ensae_teaching_cs.automation.win_setup_helper import last_function
    from pymyinstall import win_python_setup, installation_ensae, installation_teachings

    list_modules = installation_ensae() + installation_teachings()

    win_python_setup(module_list=list_modules, verbose=True,
                     download_only=False,
                     no_setup=False,
                     last_function=last_function)
