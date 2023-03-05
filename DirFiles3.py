import os

path = "/Testing1-4"
try:
    print("File name: ", os.path.basename(path))
    print("Dir part of path:", os.path.dirname(path).split("/"))
except:
    print("Cannot access this path")
