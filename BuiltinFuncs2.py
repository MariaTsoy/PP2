strg = "Hello World"
low = 0
up = 0
for i in strg:
    if i.islower():
        low += 1
    elif i.isupper():
        up += 1
print("Lowercase letters:", low)
print("Uppercase letters:", up)
