class Solution:
    def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(len(matrix)):
            matrix[i].reverse()

# make sure to add () in .reverse() method
# use matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
