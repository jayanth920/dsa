def solve(nums):
    if len(nums) == 0:
        return 0

    ptr = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[ptr]:
            ptr += 1
            nums[ptr] = nums[i]
    return ptr+1


solve([1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6])
solve([0,0,1,1,1,2,2,3,3,4])
solve([1,1,2])
# print(solve([1,1,1,1,1,2,2,3,4,5,5,5,6,6]))
