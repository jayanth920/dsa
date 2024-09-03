def solve(s, k):
    my = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    num = ""
    for i in range(len(s)):
       num += str(my[s[i]] )
    
    temp = 0
    for i in range(k):
        for j in (num):
            temp += int(j)
        num = str(temp)
        temp = 0
    return int(num)
        

print(solve("iiii", 1))
print(solve("leetcode", 2))
print(solve("zbax", 2))
