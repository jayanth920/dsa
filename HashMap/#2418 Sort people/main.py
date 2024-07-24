def sortPeople(names, heights):
    my = {}
    for i in range(len(heights)):
        my[heights[i]] = names[i] 
    final  = sorted(my.items())
    for i in range(len(final)):
        names[i] = final[i][1]
    names.reverse()
    return names
    
    
names = ["Mary","John","Emma"] 
heights = [180,165,170]   
print(sortPeople(names,heights))