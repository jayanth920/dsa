# Initial Approach. Bad Complexity--------------

# def solve(nums):
#     arr = sorted(nums)
#     for i in range(len(arr)):
#         new = rotate(arr,i)
#         if new == nums:
#             return True
#     return False
        
# def rotate(nums,k):
#     n = len(nums)
#     k = k%n
#     nums= nums[n-k:] + nums[:n-k]
#     return nums
    
# Best approach-------------
def solve(nums):
    c = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            c +=1
    return c<=1
    
    
print(solve([3,4,5,1,2]))