def solve(nums, k):
    if k > len(nums):
        return -1
    if k == len(nums):
        return sum(nums) / len(nums)   
    
    l = 0
    r = k - 1
    summer = 0
    maxAvg = float('-inf')
    
    for i in range(k):
        summer += nums[i]
                   
    while r < len(nums):
        avg = (summer) / k
        if avg > maxAvg:
            maxAvg = avg
        summer -= nums[l]
        l += 1
        r += 1   
        summer += nums[r]     
    return maxAvg


# print(solve([1, 12, -5, -6, 50, 3], 4))
# print(solve([5], 1))
print(solve([0,1,1,3,3], 4))
