class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row = [0]*n
        col= [0]*m
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        print(row)
        print(col)
        for i in range(n):
            if row[i] == 1:
                for j in range(m):
                    matrix[i][j] = 0
        
        for j in range(m):
            if col[j] == 1:
                for i in range(n):
                    matrix[i][j] = 0
        return matrix

        