def solve(n,k):
    temp = 0
    curr = 1
    for _ in range(n):
        temp = curr
        k -= 1
        if k == 0:
            return temp
        if curr*10 <= n:
            curr = curr*10
        else:
            while curr == n or curr%10 == 9:
                curr = curr // 10
            curr = curr+1
    
    
    
print(solve(13,2))
print(solve(1,1))
print(solve(681692778,351251360))