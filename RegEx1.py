import re

string = str(input("Enter string: "))
x = re.search("ab*", string)
if x:
    print("Match")
else:
    print("No match")
