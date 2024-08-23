def solve(nums):
    res = 0
    i = 0
    while i < len(nums)-1:
        if nums[i] == "-":
            res += -(int(nums[i+1])/int(nums[i+3]))
            i+= 4
        elif nums[i] == "+":
            res += +(int(nums[i+1])/int(nums[i+3]))
            i+=4
        else:
            res += (int(nums[i])/int(nums[i+2]))
            i+= 3
    final = str(round(res,3))
    return final
            
            
        
    
    
print(solve("-1/2+1/2"))
print(solve("-1/2+1/2+1/3"))
print(solve("1/3-1/2"))