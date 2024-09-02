def solve(n):
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1


print(solve(1))
print(solve(16))
print(solve(3))
