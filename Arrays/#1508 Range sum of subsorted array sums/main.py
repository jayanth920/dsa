def solve(nums,n,left,right):
    temp = []
    for i in range(len(nums)):
        sum = 0
        temp.append(nums[i])
        sum = nums[i]
        for j in range(i+1,len(nums)):
            sum += nums[j]
            temp.append(sum)
    temp.sort()
    res = temp[left-1:right]
    total = 0
    for item in res:
        total += item
    return total%((10**9) + 7)
        
    
# 1 , 
    
    
print(solve([1,2,3,4],4,1,5))

s = "HEL LO"
filtered_chars = [char.lower() for char in s if char.isalnum()]

print(''.join(filtered_chars))