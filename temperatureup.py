import subprocess
import time



for x in xrange(16, 26):
  sendir = subprocess.call(["irsend", "SEND_ONCE", "TCL", "KEY_" + str(x) + "C-cool-hi-mid"])
  time.sleep(3)


