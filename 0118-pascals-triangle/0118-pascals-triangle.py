from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for n in range(numRows):
            row = []
            for r in range(n+1):
                ncr = (factorial(n)) // (factorial(r)*factorial(n-r))
                row.append(ncr)
            lst.append(row)
        return lst

        