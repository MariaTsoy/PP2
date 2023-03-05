file = open("Testing1-4", "r")
count = 0
for line in file.readlines():
    count += 1
print("Lines in file:", count)
file.close()
