def solve(n):
    # MY VERSION (RUNS FASTER BTW LOL)
    num = str(n)
    mem = set()
    tempSum = 0
    while num != "1":
        for i in range(len(num)):
            tempSum += int(num[i]) ** 2
        num = str(tempSum)
        tempSum = 0
        if num in mem:
            return False
        else:
            mem.add(num)
    return True


        # ANOTHER WAY WITHOUT USING THE STR CONVERSION, WE USE % and // here
        # seen = set()
        
        # while n != 1:
        #     current = n
        #     total_sum = 0
            
        #     # Extract each digit and calculate the sum of squares
        #     while current > 0:
        #         digit = current % 10  # Extract the last digit
        #         total_sum += digit ** 2  # Square it and add to the sum
        #         current //= 10  # Remove the last digit
            
        #     # Check if we have seen this sum before
        #     if total_sum in seen:
        #         return False
            
        #     seen.add(total_sum)
        #     n = total_sum
        
        # return True
        
        
        

    # IMPROVED VERSION BY PY CODE - BUT RUNS SLOWER LOL
    # cache = set()
    # while n!= 1:
    #     temp = str(n)
    #     # n = sum([int(temp[i])*int(temp[i]) for i in range(len(temp))])
    #     n = sum([int(i)**2 for i in (temp)])
    #     if n in cache:
    #         return False
    #     else:
    #         cache.add(n)
    # return True



print(solve(2))
print(solve(19))
