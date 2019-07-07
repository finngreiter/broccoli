import os

name = input("Name of folder: ")

try:
    os.mkdir(name)
except FileExistsError:
    print(name + " already exists.")