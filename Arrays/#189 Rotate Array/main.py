# Solution 1 - O(n,k)
# def rotate(nums,k):
#     for i in range(k):
#         nums.insert(0 ,nums.pop())
#     return nums

# print(rotate([1,2,3,4,5,6,7],3))

# Solution - O(n)
def rotate(nums,k):
    n = len(nums)
    k = k%n
    nums= nums[n-k:] + nums[:n-k]
    return nums

print(rotate([1,2,3,4,5,6,7,8],4))
# [5,6,7,8,1,2,3,4]