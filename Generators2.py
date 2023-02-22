def evens(n):
    num = 0
    while num <= n:
        yield num
        num += 2


n = int(input("n: "))
for i in evens(n):
    print(i, end=', ')
