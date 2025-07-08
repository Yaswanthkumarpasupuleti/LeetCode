class Solution:
    def rotate(self, lst: List[List[int]]) -> None:
        n = len(lst)
        transpose = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(lst[j][i])
            transpose.append(row)
        #print(transpose)
        #print(transpose)
        # for i in range(0,n):
        # 	temp = transpose[i][0]
        # 	#print(temp)
        # 	#print(transpose[i][n-1])
        # 	transpose[i][0] = transpose[i][n-1]
        # 	transpose[i][n-1]= temp
        # #print(transpose)
        for i in range(len(transpose)):
            transpose[i] = transpose[i][::-1]
        # for i in range(n):
        #     for j in range(n):
        #         print(transpose[i][j],end=" ")
        #     print()
        for i in range(n):
            lst[i] = transpose[i]
        return lst