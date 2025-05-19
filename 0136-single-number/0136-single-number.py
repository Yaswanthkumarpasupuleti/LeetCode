class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_operator = 0
        for ele in nums:
            xor_operator ^= ele
        return xor_operator 
        