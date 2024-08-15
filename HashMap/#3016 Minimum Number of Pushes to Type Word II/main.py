# def solve(word):
    # METHOD 1 - GOOD SOLUTION - without the tweak
    # my = {}
    # for i in range(len(word)):
    #     if word[i] in my:
    #         my[word[i]] += 1
    #     else:
    #         my[word[i]] = 1

    # res = [(k,v) for k,v in my.items()]
    # res.sort(key=lambda x: x[1], reverse=True)
    # multiplier = 1
    # counter = 1
    # sum = 0
    # for i in range(len(res)):
    #     if counter < 8:
    #         sum += (res[i][1] * multiplier)
    #         counter += 1
    #     elif counter == 8:
    #         sum += (res[i][1] * multiplier)
    #         counter = 1
    #         multiplier += 1
    # return sum
    
# METHOD 2 - Also an GREAT soln but with a small tweak, mentioned in the comments below
def solve(word):
    my = {}
    for i in range(len(word)):
        if word[i] in my:
            my[word[i]] += 1
        else:
            my[word[i]] = 1
    # Important thing here is that we dont need keys anymore(meaning we do my.values()), 
    # we take biggest values by reverse sorting so that their cost pressing is 1.
    my_sorted = sorted(my.values(),reverse=True)
    pushsum = 0
    for i,freq in enumerate(my_sorted):
        keypress = (i//8) + 1
        pushsum += freq * keypress
        
    return pushsum


print(solve("abcde"))
print(solve("xyzxyzxyzxyz"))
print(solve("aabbccddeeffgghhiiiiii"))
