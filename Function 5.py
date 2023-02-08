def perms(strg, find, lind):
    if find == lind:
        print(str(strg))
    else:
        for i in range(find, lind):
            strg[find], strg[i] = strg[i], strg[find]
            perms(strg, find + 1, lind)
            strg[find], strg[i] = strg[i], strg[find]


def str(list):
    return ''.join(list)


string1 = "Ilu"
list1 = list(string1)
perms(list1, 0, len(string1))
