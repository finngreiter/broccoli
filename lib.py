from book import *
from look import *
from new import *

def runcommand(cmd):
    # bad code
    if cmd == "quit":
        exit()
    else:
        command = cmd + "()"
        exec(command)