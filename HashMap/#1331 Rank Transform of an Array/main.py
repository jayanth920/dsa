def solve(arr):
        my = {}
        temp = sorted(set(arr))
        for i in range(len(temp)):
                my[temp[i]] = i+1
                
        res = []
        for i in range(len(arr)):
            res.append(my[arr[i]])
        return res

    
    
print(solve([40,10,20,30]))
print(solve([100,100,100]))
print(solve([37,12,28,9,100,56,80,5,12]))