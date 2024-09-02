def solve(n):
    cache = set()
    while n!= 1:
        temp = str(n)
        # n = sum([int(temp[i])*int(temp[i]) for i in range(len(temp))])
        n = sum([int(i)**2 for i in (temp)])
        if n in cache:
            return False
        else:
            cache.add(n)
    return True

print(solve(2))
print(solve(19))
