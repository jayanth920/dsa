def solve(nums):
    nums = sorted(nums)
    ans = list()
    seen = set()
    j=0
    k=0
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicates for the first element
        j=(i+1)
        k=len(nums)-1
        while j<k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                    k-=1
            elif sum < 0:
                    j+=1
            else:
                unique = (nums[i],nums[j],nums[k])
                if unique not in seen:
                    seen.add(unique)
                    ans.append(list(unique))
                     # Move both pointers to avoid duplicates
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
    return ans


nums = [-1, 0, 1, 2, -1, -4]
result = solve(nums)
print(result)