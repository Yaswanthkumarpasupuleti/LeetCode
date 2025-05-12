class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            length = len(str(ele))
            if length % 2 == 0:
                res += 1
        return res
        