def solve(s):
    my = {}
    for i in range(len(s)):
        if s[i] in my:
            my[s[i]] += i
        else:
            my[s[i]] = 1
    return len(my)
            
            
        
        
    
    

print(solve("aaabbb"))
print(solve("aba"))