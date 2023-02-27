import re

string = str(input("Enter string: "))

while True:
    x = re.search("[a-z][A-Z]", string)
    if x == None:
        break
    currentWord = str(x.group())
    currentWord = currentWord.replace(currentWord[0], "")
    string = re.sub(currentWord, '_' + currentWord.lower(), string, 1)

print(string)
