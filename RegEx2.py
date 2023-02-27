import re

string = str(input("Enter string: "))
x = re.search("ab{2}b?", string)
if x:
    print("Match")
else:
    print("No match")
