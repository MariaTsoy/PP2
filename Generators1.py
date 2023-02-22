def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


n = int(input("N: "))
for i in squares(n):
    print(i)
