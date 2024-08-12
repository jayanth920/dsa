# 2 Methods both are almost same, 1st one is what I came up with initially.
# Method 1
def solve(s,t):
    idx = 0
    if s == "" or len(s) <= 0:
        return True
    for i in range(len(t)):
        if t[i] == s[idx]:
            idx+=1
            if idx == len(s):
                return True
    return False

# Method 2

def solve(s,t):
    idx = 0
    if not s:
        return True
    for i in range(len(t)):
        if idx<len(s) and t[i] == s[idx]:
            idx+=1
    return idx == len(s)
            
    
    
print(solve("abc","ahbgdc"))
print(solve("aec","ahcgde"))