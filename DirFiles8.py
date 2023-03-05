import os

file = "Testing8"
if os.access(file, os.F_OK):
    os.remove(file)
    print("File deleted.")
else:
    print("Path doesn't exist.")
