def solve(nums,k):
    n = len(nums)
    
    # Min/Least size of a part
    part_size = n // k
    
    # Number of parts getting extra items
    num_xtra_parts = n % k
    temp = []
    res = []
    idx = 0
    for i in range(k):
        if num_xtra_parts > 0 :
            while len(temp) != part_size+1:
                temp.append(nums[idx])
                idx+=1
            res.append(temp)
            temp = []
            num_xtra_parts -= 1
        else:
            res.append(nums[idx:idx+part_size])
            idx += part_size
    return res
            
        
    
    
    
print(solve([1, 2, 3, 4, 5, 6, 7], 8))

print(solve([1, 2, 3], 5))  # Output: [[1], [2], [3], [], []]
print(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]