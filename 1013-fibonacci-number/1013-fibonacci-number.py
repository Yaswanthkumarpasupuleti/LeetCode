class Solution:
    # def solve(self,n,dp):
    #     if n <= 1:
    #         return n
    #     if dp[n] != -1:
    #         return dp[n]
    #     dp[n] = self.solve(n-1,dp)+self.solve(n-2,dp)
    #     return dp[n]

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        #dp = [-1]*(n+1)
        a = 0
        b = 1
        for i in range(1,n):
            c = a+b
            a = b
            b = c
        return c

        