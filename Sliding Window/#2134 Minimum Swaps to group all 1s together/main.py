def solve(nums):
    r = 0
    l = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            r=i
            if r == 1:
                l = i
            
    # for i in range(l,r):
    #     if nums[i] == 0:
            
        
    
            
    return r

print(solve([0,1,0,1,1,0,0]))
print(solve([0,1,1,1,0,0,1,1,0]))
print(solve([1,1,0,0,1]))
    