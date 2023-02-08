def uniq(list):
    newlist = []
    for i in list:
        if not (i in newlist):
            newlist.append(i)
    return newlist


list1 = [1, 1, 2, 3, 4, 2, 5, 6, 7, 7, 7, 8, 9, 0, 1]
print(uniq(list1))
