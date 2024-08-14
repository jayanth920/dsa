def solve(nums, k):
        nums.sort()
        def count(dist):
            l, res = 0, 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res
        l, r = 0, max(nums) 
        # or we can use l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = l + (r - l) // 2
            if count(m) >= k:
                r = m
            else:
                l = m + 1
        return l
                
    
print(solve([1,3,1],1))
print(solve([1,1,1],2))
print(solve([1,6,1],3))
print(solve([62,100,4],2))
print(solve([2,2,0,1,1,0,0,1,2,0],2))
print(solve([38,33,57,65,13,2,86,75,4,56],26))