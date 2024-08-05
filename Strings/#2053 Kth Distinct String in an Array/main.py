def solve(arr, k):
    my = {}
    for i in range(len(arr)):
        if arr[i] in my:
            my[arr[i]] += 1
        else:
            my[arr[i]] = 1
            
    dist = [k for k,v in my.items() if v == 1]
    
    if k<=len(dist):
        return dist[k-1]
    else:
        return ""
        
        
    
    
    
    
    
print(solve(["d","b","c","b","c","a"],2))
print(solve(["aaa","aa","a"],1))
print(solve(["a","b","a"],3))