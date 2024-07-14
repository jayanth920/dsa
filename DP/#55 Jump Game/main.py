def solve(nums):
    reachmaxxing = 0
    for i in range(len(nums)):
        if i <= reachmaxxing:
            reachmaxxing = max(reachmaxxing, i+nums[i])
            if reachmaxxing >= len(nums)-1:
                return True
    return False
            
    
print(solve([2, 3, 1, 1, 4]))
#            0, 1, 2, 3, 4
print(solve([3, 2, 1, 0, 4]))
#            0, 1, 2, 3, 4
print(solve([2, 5, 0, 0]))
#            0, 1, 2, 3

        