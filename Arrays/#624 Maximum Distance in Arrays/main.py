def solve(arrays):
    minVal = arrays[0][0]
    maxVal = arrays[0][-1]
    reachmaxxing = 0
    for i in range(1, len(arrays)):
        reachmaxxing = max(
            reachmaxxing, abs(maxVal - arrays[i][0]), abs(arrays[i][-1] - minVal)
        )
        # update min and max vals
        maxVal = max(maxVal, arrays[i][-1])
        """this is for the abs(maxval - array[i][0]) 2nd condition above"""
        minVal = min(minVal, arrays[i][0])
        """this is for the abs(array[i][-1] - minVal) 3rd condition above"""
    return reachmaxxing


print(solve([[-1,1],[-3,1,4],[-2,-1,0,2]]))
print(solve([[-5, -2, 0, 1, 1, 2], [-7, -6, -3], [-8, -7, -4, -4, 0, 2, 3, 4]]))
print(solve([[1,2,3],[4,5],[1,2,3]]))
print(solve([[1],[1]]))
print(solve([[1,4],[0,5]]))
print(solve([[1,5],[3,4]]))
print(solve([[1,4,5],[0,2]]))
