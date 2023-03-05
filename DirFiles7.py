file1 = open("Testing7.1", "r")
file2 = open("Testing7.2", "w")
lines1 = file1.readlines()
for i in lines1:
    file2.write(i)
print("Copied from file1 to file2.")
file1.close()
file2.close()
