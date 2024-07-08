def solve(nums):
    ui = 1
    for i in range(0,len(nums)):
        if nums[i] != nums[ui]:
            ui+=1
            nums[ui] = nums[i]
    return ui
            
    
    
print(solve([1,1,1,1,1,2,2,3,4,5,5,5,6,6]))