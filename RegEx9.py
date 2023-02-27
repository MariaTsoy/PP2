import re

string = str(input("Enter string: "))

while True:
    x = re.search("\B[A-Z][a-z]+", string)
    if x == None:
        break
    currentWord = str(x.group())
    string = re.sub(currentWord, ' ' + currentWord, string, 1)

print(string)
