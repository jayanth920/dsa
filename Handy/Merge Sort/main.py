# def solve(nums):
#     def merge(arr):
#         if len(arr)>1:
#             mid = len(arr)//2
#             left = arr[:mid]
#             right = arr[mid:]
            
#             #recursion
#             merge(left)
#             merge(right)
            
#             i = 0 #left array's i
#             j = 0 #right array's j
#             k = 0 #merged arr idx
            
#             #merge step
#             while i<len(left) and j<len(right):
#                 if left[i]<right[j]:
#                     arr[k] = left[i]
#                     i+=1
#                 else:
#                     arr[k] = right[j]  
#                     j+=1
#                 k+=1
            
#             while i < len(left):
#                 arr[k] = left[i]
#                 i+=1
#                 k+=1
            
#             while j < len(right):
#                 arr[k] = right[j]
#                 j+=1
#                 k+=1
                
#     merge(nums)
#     return nums

# print(solve([8,7,0,5,1,4,6]))


def mergesort(nums):
    if len(nums) <=1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
        
    return merge(mergesort(left),mergesort(right))
    # if len(nums) <= 1:
    #     return nums
    # l = 0
    # r = len(nums)-1
    # # mid = len(nums)//2
    # mid = l + (r-l)//2
    # return merge(mergeSort(nums[:mid+1]), mergeSort(nums[mid+1:]))
        
def merge(left,right):
    res = []
    li = 0
    ri = 0
    while li<len(left) and ri<len(right):
        if left[li] < right[ri]:
            res.append(left[li])
            li+=1
        else:
            res.append(right[ri])
            ri +=1
    res.extend(left[li:])
    res.extend(right[ri:])
    return res



print(mergesort([4, 2, 3, 8, 6, 5, 7, 1]))
                