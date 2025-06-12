class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix)
        m = len(matrix[0])
        minrow = [0]*n
        maxcol = [0]*m
        for i in range(n):
            minrow[i] = min(matrix[i])
        print(minrow)
        for j in range(m):
            maxc = 0
            for i in range(n):
                if matrix[i][j] > maxc:
                    maxc  = matrix[i][j]
                maxcol[j] = maxc
        print(maxcol)
        for ele in minrow:
            if ele in maxcol:
                res.append(ele)
        return res




        