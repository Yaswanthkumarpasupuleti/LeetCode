class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = abs(x)
        else:
            temp = x
        rev = 0
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if rev < -(2**31) or rev > ((2**31)-1):
            return 0
        if x < 0:
            return -rev
        return rev
        