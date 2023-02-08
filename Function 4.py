import math


def isPrime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        else:
            return 1
    else:
        return 0


def onlyPrimes(list):
    for i in list:
        if not isPrime(i):
            list.remove(i)
            onlyPrimes(list)


list1 = list(map(int, input().split()))
onlyPrimes(list1)
print(list1)
