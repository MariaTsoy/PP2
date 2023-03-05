file = open("Testing5", "w")
myList = ["Hello", "How r u?", "Bye"]
count = 0
for i in myList:
    file.write(i + "\n")
print("Wrote list to a file")
file.close()
