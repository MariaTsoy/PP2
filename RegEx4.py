import re

string = str(input("Enter string: "))
x = re.findall("[A-Z][a-z]+", string)
print(x)
