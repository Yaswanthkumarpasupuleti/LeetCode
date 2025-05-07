class Solution:
    def maxProduct(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        return max(a[i] * a[j] for i in range(len(a)) for j in range(i + 1, len(a)))
        