def solve(nums):
    # METHOD 1
    itemSum = sum(nums)
    k = len(nums)
    lenTotalSum = int(k*(k+1)/2)
    return lenTotalSum - itemSum

    # METHOD 2 SLOWER and MORE SPACE
    # hash = [0] * (k+1) # k+1 because we need an index for the missing number which is not currently here
    # for i in range(k):
    #     hash[nums[i]] += 1
    
    # for i in range(k+1):
    #     if hash[i] == 0:
    #         return i
    # return -1
        
    
    
    
print(solve([3,0,1]))
print(solve([0,1]))
print(solve([9,6,4,2,3,5,7,0,1]))