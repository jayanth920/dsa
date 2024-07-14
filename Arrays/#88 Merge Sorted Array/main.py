# Merge two sorted arrays



def merge(nums1,m,nums2,n):
    p1 = m-1
    p2 = n-1
    p = m+n-1
    
    while p1>=0 and p2>=0:
        if nums2[p2] > nums1[p1]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    
    while p2>=0:
        nums1[p] = nums2[p2]
        p-=1
        p2-=1
    return nums1
        
print(merge([2,3,6,0,0,0], 3, [2,27,29], 3))
        