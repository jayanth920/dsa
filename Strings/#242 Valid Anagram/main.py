from collections import Counter
def solve(s,t):
    # Method 1
    # i = list(s)
    # i.sort()
    # j = list(t)
    # j.sort()
    # return i == j
    
    # Method 2 
        # mapping = dict()

        # for c in s :
        #     mapping[c] = mapping.get(c,0)+1
        # for c in t :
        #     mapping[c] = mapping.get(c,0) - 1

        # for val in mapping.values():
        #     if val != 0:
        #         return False

        # return True
    # Method 3
    return Counter(s) == Counter(t)
        
        
    
print(solve("anagram","nagaram"))
print(solve("rat","car"))