def spy_game(nums):
    one = 1
    two = 1
    for i in nums:
        if one == 1 and i == 0:
            one = 0
        elif one == 0 and two == 1 and i == 0:
            two = 0
        elif one == 0 and two == 0 and i == 7:
            return True
    else:
        return False


list1 = [1,2,4,0,0,7,5]
print(spy_game(list1))
list2 = [1,0,2,4,0,5,7]
print(spy_game(list2))
list3 = [1,7,2,0,4,5,0]
print(spy_game(list3))
