def solve(nums, target):
    # APPROACH 1 - BUT IT TAKES SPACE DUE TO HASHMAP
    # my = {}
    # for i in range(len(nums)):
    #     complement = target-nums[i]
    #     if complement in my:
    #         return [my[complement], i]
    #     else:
    #         my[nums[i]] = i
    
    # APPROACH 2 - IT TAKES O(nlogn) time
    # for i in range(len(nums)):
    #     comp = target - nums[i]
    #     j = i+1
    #     k = len(nums)-1
    #     while j<=k:
    #         mi = j+(k-j)//2
    #         if comp == nums[mi]:
    #             print("SOLVED")
    #             return [i+1,mi+1]
    #         elif comp > nums[mi]:
    #             j = mi + 1
    #         elif comp < nums[mi]:
    #             k = mi -  1
    
    # APPROACH 3 - O(n) where we check by 2 pointers. it is O(n)
    x = 0
    y = len(nums)-1
    while x<=y:
        sum = nums[x] + nums[y]
        if sum < target:
            x += 1
        elif sum > target:
            y -= 1
        else:
            return [x,y]
    return []
    
print(solve([2,7,11,15,20],26))