# Solution 1 - O(n_
def rotate(nums,k):
    for i in range(k):
        nums.insert(0 ,nums.pop())
    return nums

print(rotate([1,2,3,4,5,6,7],3))