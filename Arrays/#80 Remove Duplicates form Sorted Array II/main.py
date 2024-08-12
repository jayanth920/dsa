def removeDuplicates(nums):
    ui = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[ui - 2]:
            nums[ui] = nums[i]
            ui += 1
    return ui
