def solve(nums):
    res = []
    def helper(arr):
        for i in range(len(arr)):
            if isinstance(arr[i], list):
                helper(arr[i])
            else:
                res.append(arr[i])
    
    helper(nums)
    return res



print(solve([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]))