def solve(target,arr):
    # FIRST TRY (BEGINNER AT PYTHON)
    
    # if len(arr) != len(target):
    #     return False
    # arr.sort()
    # target.sort()
    # for i in range(len(arr)):
    #     if arr[i] == target[i]:
    #         continue
    #     else:
    #         return False
    # return True
    
    # Using shorthand
    return sorted(target) == sorted(arr)

print(solve([1,2,3,4],[2,4,1,3]))
print(solve([7],[7]))
print(solve([3,7,9],[3,7,11]))
    
    
    