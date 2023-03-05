import string
import os

try:
    for i in string.ascii_uppercase:
        file = open(i + ".txt", "x")
    print("Created 26 files.")
except:
    print("Some of these already exist.")

# try:
#     for i in string.ascii_uppercase:
#         os.remove(i + ".txt")
#     print("Deleted 26 files.")
# except:
#     print("Cannot delete these files.")
