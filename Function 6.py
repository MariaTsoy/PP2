def rev(str1):
    words = []
    word = ""
    for i in str1:
        if i != " " and i != "\n":
            word += i
        else:
            words.append(word)
            word = ""
    else:
        words.append(word)
        word = ""
    newstr = ""
    u = len(words) - 1
    while u >= 0:
        newstr += words[u]
        u -= 1
        newstr += " "
    return newstr


strg = "I love sleeping very much"
print(rev(strg))
