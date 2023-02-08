def solve(numheads, numlegs):
    for ch in range(numheads + 1):
        r = numheads - ch
        if 2 * ch + 4 * r == numlegs:
            return ch, r
    else:
        return "There is no solution"


legs = 94
heads = 35
print(solve(heads, legs))
