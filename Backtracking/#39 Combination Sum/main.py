# Method 1 (where we keep adding to the sum)
def combinationSum(candidates, target):
    res, sol = [], []
    nums = candidates
    n = len(nums)

    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(sol[:])
            return

        if cur_sum > target or i == n:
            return

        # Skip the current candidate
        backtrack(i + 1, cur_sum)
        
        # Include the current candidate
        sol.append(nums[i])
        backtrack(i, cur_sum + nums[i])
        sol.pop()

    backtrack(0, 0)
    return res

# Method 2 (where we keep adding to the sum)
def combinationSum(candidates, target):
        res = []
        n = len(candidates)
        
        def dfs(i, current_sum, ds):
            if current_sum == target:
                res.append(ds.copy())
                return
            if i >= n or current_sum > target:
                return
            
            # Include the current candidate
            ds.append(candidates[i])
            dfs(i, current_sum + candidates[i], ds)
            ds.pop()
            
            # Skip the current candidate and move to the next one
            dfs(i + 1, current_sum, ds)
        
        dfs(0, 0, [])
        return res


# Method 3 (where we keep subtracting from the target till 0)
def combinationSum(candidates, target):
    res = []
    n = len(candidates)

    def dfs(i, target, ds):
        if target == 0:
            res.append(ds.copy())
            return
        if i >= n or target < 0:
            return

        # Include the current candidate
        ds.append(candidates[i])
        dfs(i, target - candidates[i], ds)
        ds.pop()

        # Skip the current candidate and move to the next one
        dfs(i + 1, target, ds)

    dfs(0, target, [])
    return res
