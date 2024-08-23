def solve(nums, k):
    my = {}
    for i in nums:
        if i not in my:
            my[i] = 0
        my[i] += 1
    final = [k for k, v in sorted(my.items(), key=lambda item: (item[1]),reverse=True)]
    return final[:k]
    
    
print(solve([1,1,1,2,2,3],2))
print(solve([1],1))