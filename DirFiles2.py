import os

path = "Testing1-4"
print("Existence:", os.access(path, os.F_OK), "\n")
print("Readability:", os.access(path, os.R_OK), "\n")
print("Writability:", os.access(path, os.W_OK), "\n")
print("Executability:", os.access(path, os.X_OK), "\n")
