import re

string = str(input("Enter snake string: "))

while True:
    x = re.search("_[a-z]+", string)
    if x == None:
        break
    currentWord = str(x.group())
    string = re.sub(currentWord[0] + currentWord[1], currentWord[1].upper(), string, 1)

print("Camel string: ", string)