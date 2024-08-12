class KthLargest:
# Method 1 (What i thought initally, 0 brain power used)
    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = nums
        

    # def add(self, val: int) -> int:
    #     self.nums.append(val)
    #     self.nums.sort(reverse=True)
    #     return self.nums[self.k-1]

# Method 2 using brain power a bit
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
# Lets sort it off in the beginning, then when we insert 
# we will do a binary search and insert in the approriate place
        

    def add(self, val: int) -> int:
        index = self.binarySearch(val)
        self.nums.insert(index, val)
        return self.nums[-self.k]

    def binarySearch(self,v: int) -> int:
        l, r = 0, len(self.nums) - 1
        while l <= r:
            m = (l + r) // 2
            if self.nums[m] == v:
                return m
            elif v > self.nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l





# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(1, [2,40,5,6,10,80,9,5,20])
param_1 = obj.add(10)
param_2 = obj.add(20)
param_3 = obj.add(30)
print(param_1)