def solve(flowerbed, n):
    length = len(flowerbed)
    for i in range(length):
        if flowerbed[i] == 0:
            prev = i == 0 or flowerbed[i-1] == 0
            next = i == length-1 or flowerbed[i+1] == 0
            if prev and next:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
    return n == 0
                
            
    


print(solve([1, 0, 0, 0, 1], 1))
print(solve([1, 0, 0, 0, 1], 2))
