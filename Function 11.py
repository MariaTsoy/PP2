def pal(word):
    backs = ""
    i = len(word) - 1
    while i >= 0:
        backs += word[i]
        i -= 1
    if backs == word:
        return True
    else:
        return False


word1 = "madam"
print(pal(word1))
w2 = "madame"
print(pal(w2))
