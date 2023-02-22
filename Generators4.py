def squares(a, b):
    num = a
    while num <= b:
        yield num * num
        num += 1


a = int(input("a: "))
b = int(input("b: "))
for i in squares(a, b):
    print(i)
