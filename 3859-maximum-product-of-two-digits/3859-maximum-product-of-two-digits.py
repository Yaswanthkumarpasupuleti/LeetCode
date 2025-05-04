class Solution:
    def maxProduct(self, n: int) -> int:
        lst = []
        lar = 0
        while n > 0:
            dig = n % 10
            if dig > lar:
                lar = dig
            lst.append(dig)
            n = n // 10
        if lst.count(lar) == 1:
            lst.sort()
            return lar*lst[-2]
        if lst.count(lar) >= 2:
            return lar*lar
        
            
        