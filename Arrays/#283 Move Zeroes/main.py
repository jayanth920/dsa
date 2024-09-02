def solve(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    ptr = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            ptr = i
            break
    if ptr == -1:
        return
    for i in range(ptr + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1


print(solve([0, 1, 0, 3, 12]))
print(solve([0]))
