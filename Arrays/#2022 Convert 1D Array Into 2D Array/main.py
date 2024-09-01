def solve(nums, m, n):
    # if m*n > len(nums):
    #     return []
    # elif m*n < len(nums):
    #     return []
    # res = []
    # temp = []
    # cn = 0
    # for i in range(len(nums)):
    #     cn+=1
    #     if cn == n:
    #         temp.append(nums[i])
    #         res.append(temp)
    #         temp = []
    #         cn = 0
    #     else:
    #         temp.append(nums[i])
    # return res

    # max = m * n
    # if max != len(nums):
    #     return []
    # cn = 1
    # res = []
    # res.append(nums[0:n])
    # for i in range(1,m):
    #     cn+=1
    #     res.append(nums[i*n:n*cn])
    # return res

    # max = m * n
    # if max != len(nums):
    #     return []
    # res = []
    # for i in range(m):
    #     res.append(nums[i*n:n*(i+1)])
    # return res

    if m * n != len(nums):
        return []
    res = [nums[i * n : n * (i + 1)] for i in range(m)]
    return res

    # return [] if m * n != len(nums) else [nums[i*n:n*(i+1)] for i in range(m)]


print(solve([1, 2, 3, 4], 2, 2))
print(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 4, 3))
print(solve([1, 2], 1, 1))
print(solve([3], 2, 1))
