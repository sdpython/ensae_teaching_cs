import sys
sys.path.append(r"D:\Dupre\_data\program\pyhome")
import pyhome3
from pyhome3 import HalLOG
from pyhome3.srcpyhome.internet.simple_server.simple_server_custom import run_server

HalLOG(OutputPrint=True)
HalLOG("running server")
run_server(None)
HalLOG("end running server")

# http://localhost:8080/localfile/D:\Dupre\_data\informatique\support\python_td_2013\programme\td9_by_hours.json
# http://localhost:8080/debug_string/

