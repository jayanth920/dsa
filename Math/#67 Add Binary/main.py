def solve(a, b):
    if a == "0" and b == "0":
        return "0"
    m = max(len(a), len(b))
    alen = len(a) - 1
    blen = len(b) - 1
    sum = 0
    for i in range(m):
        if i < len(a) and alen >= 0:
            sum += int(a[i]) * (2**alen)
            alen -= 1
        if i < len(b) and blen >= 0:
            sum += int(b[i]) * (2**blen)
            blen -= 1
    res = []
    while sum != 0:
        q = sum % 2
        res.append(q)
        sum = sum // 2
    res.reverse()
    result = "".join(str(num) for num in res)
    return result


print(solve("11", "1"))
print(solve("1010", "1011"))
