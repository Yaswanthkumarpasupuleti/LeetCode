
from math import factorial
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = []
        for n in range(rowIndex+1):
            row = []
            for r in range(n+1):
                ncr = (factorial(n)) // (factorial(r)*factorial(n-r))
                row.append(ncr)
            lst.append(row)
        return lst[rowIndex]
        