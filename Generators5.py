def fronNto0(n):
    num = n
    while n >= 0:
        yield n
        n -= 1


n = int(input("n: "))
for i in fronNto0(n):
    print(i)
