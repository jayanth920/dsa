def solve(nums,k):
    my = {}
    for i in range(len(nums)):
        if (nums[i] in my) and (abs(my[nums[i]] - i)<=k):
            return True
        else:
            my[nums[i]] = i
    return False
    
    
print(solve([1,2,3,1],3))
print(solve([1,0,1,1],1))
print(solve([1,2,3,1,2,3],2))