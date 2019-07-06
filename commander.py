from lib import *

commands = ["book", "look", "new", "quit"]
trueorfalse = False

def commander():
    global trueorfalse
    command = input("Broccoli: ")
    for i in range(len(commands)):
        if commands[i] == command:
            trueorfalse = True
            break
        else:
            trueorfalse = False
            continue
    if trueorfalse == True:
        runcommand(command)
    else:
        print("Command not found.")