def solve(nums):
    def merge(arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            
            #recursion
            merge(left)
            merge(right)
            
            i = 0 #left array's i
            j = 0 #right array's j
            k = 0 #merged arr idx
            
            #merge step
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    arr[k] = left[i]
                    i+=1
                else:
                    arr[k] = right[j]  
                    j+=1
                k+=1
            
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1
                
    merge(nums)
    return nums

print(solve([8,7,0,5,1,4,6]))