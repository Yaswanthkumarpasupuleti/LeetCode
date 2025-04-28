class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 2
        n = len(points)
        if(n <= 2):
            return n
        for i in range(0,n):
            for j in range(i+1,n):
                cnt = 2
                for k in range(j+1,n):
                    x1 = points[i][0]
                    y1 = points[i][1]
                    x2 = points[j][0]
                    y2 = points[j][1]
                    x3 = points[k][0]
                    y3 = points[k][1]
                    if ((y2-y1)*(x3-x1)) == ((x2-x1)*(y3-y1)):
                        cnt = cnt + 1
                    if cnt > res:
                        res = cnt 
        return res

        