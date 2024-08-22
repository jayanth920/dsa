def solve(num):
    a = bin(num)[2:]
    b = ""
    for i in range(len(a)):
        if a[i] == "0":
            b += "1"
        else:
            b += "0"
            
    d = len(b)-1
    res = 0
    for i in range(len(b)):
        res += (int(b[i])) * (2**d)
        d -= 1
    return res
        

solve(1)