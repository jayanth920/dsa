    for i in range(1,len(arrays)):
        if arrays[i][len(arrays[i])-1] > max and i != imin:
            max = arrays[i][len(arrays[i])-1]
            imax = i
        elif arrays[i][0] < min and i!= imax:
            max = arrays[i][len(arrays[i])-1]
            imin = i