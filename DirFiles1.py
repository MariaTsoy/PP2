import os

# only directories
print(os.getcwd())
path = "C:/Users/Maria/PycharmProjects/Lab6"
os.chdir(path)
print("Only Directories: ")
for i in os.listdir():
    if os.path.isdir(i):
        print(i)
print()

# only files
print("Only Files: ")
for i in os.listdir():
    if os.path.isfile(i):
        print(i)
print()

# all Files and Dirs
print("All Files and Dirs: ")
print(os.listdir())
