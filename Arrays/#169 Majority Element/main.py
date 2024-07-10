def majorityElement(nums):
    my = {}
    v = 0
    k = 0
    for i in range (len(nums)):
        if nums[i] not in my:
            my[nums[i]] = 1
        else:
            my[nums[i]] += 1
            
    for i in range(len(nums)):
        if my[nums[i]] > v:
            v = my[nums[i]]
            k = nums[i]
    return k
        
print(majorityElement([2,2,1,1,1,2,2]))