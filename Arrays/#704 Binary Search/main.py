def search(nums ,target):
        i = 0
        j = len(nums) - 1
        while i<=j :
            mid = i +(j-i)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1
    
print(search([-1,0,3,5,9,12],9))
print(search([-1,0,3,5,9,12],2))