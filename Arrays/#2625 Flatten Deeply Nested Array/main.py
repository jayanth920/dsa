def solve(nums,n):
    res = []
    def helper(arr,depth):
        for i in range(len(arr)):
            if isinstance(arr[i], list) and depth < n:
                helper(arr[i], depth+1)
            else:
                res.append(arr[i])
    
    helper(nums,0)
    return res



print(solve([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]],1))