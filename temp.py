# def solve(nums):
#     reachmaxxing = 0
#     for i in range(len(nums)):
#         if i <= reachmaxxing:
#             reachmaxxing = max(reachmaxxing, i+nums[i])
#             if reachmaxxing >= len(nums)-1:
#                 return True
#     return False
    

# def solve(nums):
#     reachmaxxing = len(nums)-1
#     for i in range(len(nums)-2,-1,-1):
#         if i+nums[i] >= reachmaxxing:
#             reachmaxxing = min(reachmaxxing, i-nums[i])
#             if reachmaxxing <= 0:
#                 return True
#     return False

# print(solve([2,3,1,1,4]))

def solve(nums):
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
arr = [[0,1,1],[0,1,1],[1,2,3]]
print(solve(arr))