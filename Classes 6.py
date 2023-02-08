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


def filter(list):
    for i in list:
        if not isPrime(i):
            list.remove(i)
            filter(list)
    return list


list1 = [0, 1, 1, 2, 3, 3, 4, 6, 7, 9, 11, 12, 13, 55, 59, 11, 14]
filter(list1)
print(list1)
