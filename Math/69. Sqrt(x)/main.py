def solve(x):
    if x == 4:
        return 2
    elif x == 2:
        return 1
    elif x == 1 or x == 0:
        return 0
    res = 0
    for i in range(x//2):
        a = i*i
        b = (i+1)*(i+1)
        if a<=x and b>=x:
            res = i
        
    return res
    
print(solve(6))