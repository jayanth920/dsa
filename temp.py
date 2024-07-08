# def solve(nums1,m,nums2,n):
#     p1 = m - 1
#     p2 = n - 1
#     p = m+n-1
#     while(p1>=0 and p2>=0):
#         if nums2[p2] > nums1[p1]:
#             nums1[p] = nums2[p2]
#             p2 -=1
#         else:
#             nums1[p] = nums1[p1]
#             p1-=1
#         p-=1
#     return nums1
            
    
# print(solve([3,6,7,0,0,0],3,[4,8,27],3))


# def solve(arr,n):
#     c=0
#     for i in range(0,len(arr)):
#         if arr[i] == n:
#             arr[i] = 0
#             c+=1
#     ans = len(arr) - c
    
#     for i in range(c):
#         arr.remove(0)

            
#     return ans

# print(solve([3,2,2,3,4,5,6,7,8,3],3))


def solve(nums):
    print()
    j=0
    l = list()
    
    for i in range(0,len(nums)):
        if i != len(nums)-1 and nums[i+1] == nums[i]:
            j+=1
        else:
            l.append(nums[i])
            i = j+1
    return l

print(solve([1,1,1,2,2,3,4,5,5,5,6,7,7])) 
            
            
    