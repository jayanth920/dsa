def solve(allowed,words: list[str]):
    f = 0
    res = 0
    my = set(allowed)

        
    for item in words:
        for i in item:
            if i not in my:
                f = -1
        if f == 0:
            res += 1
        else:
            f = 0
    return res
            
        
    
    
    
print(solve("ab", ["ad","bd","aaab","baa","badab"]))
print(solve("abc",["a","b","c","ab","ac","bc","abc"]))
print(solve("cad",["cc","acd","b","ba","bac","bad","ac","d"]))