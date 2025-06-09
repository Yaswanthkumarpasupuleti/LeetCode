class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            res ^= ele
        return res
        