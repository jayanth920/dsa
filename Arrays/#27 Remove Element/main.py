def solve(nums,val):
        ui=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ui] = nums[i]
                ui+=1
        
        return ui