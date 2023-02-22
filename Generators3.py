def threeFour(n):
    num = 0
    while num <= n:
        for i in range(num + 1, num + 13):
            if i % 3 == 0 and i % 4 == 0:
                if i <= n:
                    num = i
                    yield num
                else:
                    break


n = int(input("n: "))
for u in threeFour(n):
    print(u)
