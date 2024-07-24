def solve(haystack, needle):
    if not needle:
        return 0
    if not haystack:
        return -1

    c = 0
    init = -1
    i = 0

    while i <= len(haystack) - 1:
        if haystack[i] == needle[c]:
            if c == 0:
                init = i
            c += 1
            if c == len(needle):
                return init
        else:
            if c > 0:
                i = init
            c = 0
            init = -1
        i += 1

    return -1

hay = "leetcode"
need = "leet"
hay1 = "mississippi"
need1 = "issip"
# print(solve(hay, need))  # Output: 0
print(solve(hay1, need1))  # Output: 4

