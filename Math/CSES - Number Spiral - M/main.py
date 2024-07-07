def matrix(row,col):
    if row == col:
        return (row*row)-row+1
    if row > col:
        if row % 2 == 0:
            return (row*row)-col+1
        else:
            return (row*row)-(row-1)-row+col
    else:
        if col % 2  == 0:
            return (col*col)-col+1-col+row
        else:
            return (col*col)-row+1
    return -1




# TEST CASES
# print(matrix(2,1))
# print(matrix(4,1))
# print(matrix(4,3))
# -------
# print(matrix(3,1))
# print(matrix(5,1))
# print(matrix(5,3))
# -------
# print(matrix(1,2))
# print(matrix(1,4))
# print(matrix(3,4))
# -------
# print(matrix(2,3))
# print(matrix(2,5))
# print(matrix(4,5))
# -------
# print(matrix(1,1))
# print(matrix(2,2))
# print(matrix(3,3))
# print(matrix(4,4))
# print(matrix(5,5))
