# METHOD 1 EXCELLENT (but not optimised)


# def solve(nums,n,left,right):
#     temp = []
#     for i in range(len(nums)):
#         sum = 0
#         temp.append(nums[i])
#         sum = nums[i]
#         for j in range(i+1,len(nums)):
#             sum += nums[j]
#             temp.append(sum)
#     temp.sort()
#     res = temp[left-1:right]
#     total = 0
#     for item in res:
#         total += item
#     return total%((10**9) + 7)


# METHOD 2 EXCELLENT BUT OPTIMISED AS WELL
        
def solve(nums,n,left,right):
    temp = []
    for i in range(len(nums)):
        currsum = 0
        for j in range(i,len(nums)):
            currsum += nums[j]
            temp.append(currsum)
    temp.sort()
    total = sum(temp[left-1:right]) % (10**9 + 7)
    return total

    
    
print(solve([1,2,3,4],4,1,5))