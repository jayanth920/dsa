def solve(nums):
    ui = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[ui]:
            ui+=1
            nums[ui] = nums[i]
    print("ui = ",ui)
    print("nums = ",nums)
            
    
    
solve([1,1,1,1,1,2,2,3,4,5,5,5,6,6])
# print(solve([1,1,1,1,1,2,2,3,4,5,5,5,6,6]))