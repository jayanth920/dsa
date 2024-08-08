def solve(matrix):
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    while left < right and top < bottom:
        # Get all the elements in the row - left to right
        for i in range(left,right):
            res.append(matrix[top][i])
        top += 1
        # Get all elements in column - top to bottom
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
        right -= 1
        
        if not (left < right and top < bottom):
            break
        
        # Get all elements in row - right to left
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom -= 1
        # Get all elements in column - bottom to top
        for i in range(bottom-1,top-1,-1):
            res.append(matrix[i][left])
        left += 1
    return res


print(solve([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
# 1 2 3 4 5 6 7 8 9 10 11 12
# 1  2  3
# 4  5  6
# 7  8  9
# 10 11 12
