import re

string = str(input("Enter string: "))
x = re.search("^a.*b$", string)
if x:
    print("Match")
else:
    print("No match")
