def solve(nums: list,target: int):
        nums.sort()
        u = set()
        j = 0
        j = len(nums)-1
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = (i+1)
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                unique = (sum,abs(sum-target))
                if unique not in u :
                    u.add(unique)
                    res.append(list(unique))
                while j < k and nums[j] == nums[j + 1]:
                        j += 1
                while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                j += 1
                k -= 1
        res.sort(key=lambda x: x[1])
        return res
print(solve([-1,2,1,-4],1))
print(solve([0,0,0],1))
print(solve([-4,2,2,3,3,3],0))