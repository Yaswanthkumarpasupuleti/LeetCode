class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid[0])
        for i in range(len(grid)):
            if grid[i][0] < 0:
                res += n
            # elif grid[i][0] == 0:
            #      res += (n-1)
            elif grid[i][n-1] >= 0:
                continue
            else:
                for j in range(n-1,-1,-1):
                    if grid[i][j] < 0:
                        res+=1
                    else:
                        break
        return res
