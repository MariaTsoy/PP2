def hist(list):
    for i in list:
        while i > 0:
            print("*", end="")
            i -= 1
        print()


list = [4, 9, 7]
hist(list)
