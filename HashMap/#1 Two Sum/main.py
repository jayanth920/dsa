#1 Hash Table (Single pass) O(n) + Map storage optimisation based on nums - CLEVER, EXCELLENT
#2 Hash Table (Double pass) O(n) - GOOD
#3 Brute force O(n^2) - Dont know hash table ay, BASIC

#-------------1------------------------
#say a + b = target
def twoSum(nums, target):
    mymap = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in mymap:
            return [mymap[complement], i]
        
        # Add the current number and its index to the dictionary, here
        # since complement = target - a, meaning b is not present in map
        # we add a to the map...as we go on when we get b from nums and
        # do complement = target - b we already have a which we did in 
        # the beginning, so return positions
        mymap[num] = i
    
    return []
#---------------2---------------------
def twoSum(nums, target):
    mymap = {}
    n = len(nums)
    for i in range(n):
        mymap[nums[i]] = i
        
    for i in range(n):
        complement = target - nums[i]
        if complement in mymap and mymap[complement] != i:
            return [i,mymap[complement]]
    return []
#--------------------3----------------------
def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
#-------------------------------------------

# Test cases
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(twoSum([3, 3], 6))          # Output: [0, 1]