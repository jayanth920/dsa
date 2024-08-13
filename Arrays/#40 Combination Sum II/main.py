def solve(nums):
    nums.sort()
    res = []
    for i in range(0, len(nums)):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        res.append(nums[i])
    return res


print(solve([10, 1, 2, 7, 6, 7, 1, 5, 11, 10]))
# print(solve([2,5,2,1,2],5))
