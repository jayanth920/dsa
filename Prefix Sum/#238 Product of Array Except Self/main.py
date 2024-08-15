def solve(nums):
    # METHOD 1 with 3 loops
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    res = [0] * n

    # Step 1: Calculate prefix products 
    # so here is how it will look [1,1,2,6]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Step 2: Calculate suffix products
    # so here is how it will look [24,12,4,1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Step 3: Combine prefix and suffix products
    # Multiple both with ref to index
    for i in range(n):
        res[i] = prefix[i] * suffix[i]

    return res
    
    
    
print(solve([1,2,3,4]))
# 24, 12, 8, 6
# print(solve([-1,1,0,-3,3]))