strg = "Madam"
revstrg = "".join(list(reversed(strg)))
if strg.lower() == revstrg.lower():
    print("Is palindrome.")
else:
    print("Is not palindrome.")
