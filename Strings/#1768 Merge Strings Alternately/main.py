def solve(word1: str, word2: str):
    # res = ""
    # l1 = len(word1)
    # l2 = len(word2)
    # length = min(l1, l2)
    # p1 = 0
    # p2 = 0
    # for i in range (length):
    #     res += word1[i]
    #     res += word2[i]
    #     p1 = i
    #     p2 = i

    
    # if l1 == l2:
    #     return res
    # elif length == l1:
    #     for i in range(p2+1,l2):
    #         res += word2[i]
    # else:
    #     for i in range(p1+1,l1):
    #         res += word1[i]
    
    # return res


    a = []
    length = min(len(word1), len(word2))
    for i in range(length):
        a.append(word1[i])
        a.append(word2[i])
    a.append(word1[length:])
    a.append(word2[length:])
    return ''.join(a)
        
            
        
    
    
print(solve("abc","pqr"))
print(solve("ab","pqrs"))
print(solve("abcd","pq"))
print(solve("cdf","a"))