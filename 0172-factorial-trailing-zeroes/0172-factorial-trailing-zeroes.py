class Solution(object):
    def trailingZeroes(self, n):
        cnt = 0
        div = 5
        
        while n >= div:
            cnt  += n // div
            div *= 5

        return cnt