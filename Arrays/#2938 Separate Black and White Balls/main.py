def solve(s):
    swaps = 0
    res = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            res += swaps
        else:
            swaps += 1
    return res


# print(solve("101"))
print(solve("11010"))
# print(solve("0111"))
