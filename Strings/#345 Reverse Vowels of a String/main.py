def solve(s):
    temp: list = []
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    for i in range(len(s)):
        if s[i] in vowels:
            temp.append(s[i])
        
    
    res = ""
    for i in range(len(s)):
        if s[i] in vowels:
            res+= temp.pop()
        else:
            res+= s[i]
    return res


print(solve("IceCreAm"))
print(solve("leetcode"))
