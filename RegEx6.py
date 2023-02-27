import re

string = str(input("Enter string: "))
x = re.sub("\.", ":", string)
x = re.sub(",", ":", x)
x = re.sub(" ", ":", x)
print(x)
