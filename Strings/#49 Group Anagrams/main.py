def solve(strs):
    my = {}
    for item in strs:
        temp = list(item)
        temp.sort()
        tempStr = "".join(temp)
        if tempStr not in my:
            my[tempStr] = []
        my[tempStr].append(item)
        
    return my.values()
        # my = {}
        # for i in strs:
        #     temp = ''.join(sorted(i))
        #     if temp in my:
        #         my[temp].append(i)
        #     else:
        #         my[temp] = [i]
        # return my.values()


print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solve([""]))
print(solve(["a"]))
