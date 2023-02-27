import re

string = str(input("Enter string: "))
x = re.findall("[a-z]+_[a-z]+", string)
print(x)
