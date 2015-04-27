try:
    import pyquickhelper
except ImportError:
    import sys
    sys.path.append(r"../pyquickhelper/src")
    import pyquickhelper

try:
    import pymmails
except ImportError:
    import sys
    sys.path.append(r"../pymmails/src")
    import pymmails

try:
    import pyensae
except ImportError:
    import sys
    sys.path.append(r"../pyensae/src")
    import pyensae

try:
    import pyrsslocal
except ImportError:
    import sys
    sys.path.append(r"../pyrsslocal/src")
    import pyrsslocal

try:
    import ensae_teaching_cs
except ImportError:
    import sys
    sys.path.append(r"src")
    import ensae_teaching_cs

from ensae_teaching_cs.automation import rss_teachings_update_run_server
rss_teachings_update_run_server(browser="firefox")