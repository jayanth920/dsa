# A more intuitive Understandable way. (Neetcode) (O(n))

def solve(nums):
    res = 0
    l = r = 0

    while r < len(nums) - 1:
        farmax = 0
        for i in range(l, r + 1):
            farmax = max(farmax, i + nums [i])
        l = r + 1
        r = farmax
        res += 1
    return res

print(solve([2,3,1,1,4]))
print(solve([3,4,5,6,7,8,9]))
print(solve([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))

# HMMM
# def solve(nums):
#     n = len(nums)
#     curmax = 0
#     farmax = 0
#     jump = 0
#     for i in range(n):
#         farmax = max(farmax, i+nums[i])
#         if i == curmax:
#             jump+=1
#             curmax = farmax
#     return jump
    
