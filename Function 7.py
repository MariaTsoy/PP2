def has_33(nums):
    before = -999
    for i in nums:
        if before == i:
            return True
        else:
            before = i
    else:
        return False


lst = [1, 4, 3, 3, 3, 5]
print(has_33(lst))
lst2 = [1, 3, 4, 3]
print(has_33(lst2))
