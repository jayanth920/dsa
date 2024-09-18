import functools
def solve(nums):
    comp = lambda a, b: 1 if a + b > b + a else -1 if a + b < b + a else 0
    nums = [str(i) for i in nums]
    nums.sort(key=functools.cmp_to_key(comp), reverse=True)
    return str(int("".join(nums)))


print(solve([10, 2]))
print(solve([3, 30, 34, 5, 9]))
