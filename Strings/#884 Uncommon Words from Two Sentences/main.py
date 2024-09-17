from collections import defaultdict

def solve(s1,s2):
    my = defaultdict(int)  # For counting occurrences
    s1 = s1.split(" ")
    s2 = s2.split(" ")
    s1Len = len(s1)
    s2Len = len(s2)
    length = min(s1Len,s2Len)
    
    for i in range(length):
        my[s1[i]] += 1
        my[s2[i]] += 1
    
    if s1Len > s2Len:
        for i in range(length,s1Len):
            my[s1[i]] += 1
    else:
        for i in range(length,s2Len):
            my[s2[i]] += 1
            
    res = []  
    for k,v in my.items():
        if v == 1:
            res.append(k)
        
    return res
    
    
    
print(solve("this apple is sweet", "this apple is sour"))
print(solve("apple apple", "banana"))

