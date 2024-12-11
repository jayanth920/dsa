def solve(nums):
    i = 0

    while i < len(nums):
        n = nums[i]  # Current value determines the number of inner loops
        print("Outer num =", nums[i])
        j = 0
        i+=1

        while j < n and i < len(nums):  # Inner loop controlled by `n`
            print("Inner element =", nums[i]) 
            i += 1
            j += 1

solve([2, 1, 3, 4, 5, 6, 7, 8, 9])



"""
O/P


Outer num = 2
Inner element = 1
Inner element = 3
Outer num = 4
Inner element = 5
Inner element = 6
Inner element = 7
Inner element = 8
Outer num = 9
"""