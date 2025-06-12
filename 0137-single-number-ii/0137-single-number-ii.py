class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for ele in nums:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1
        for key,val in freq.items():
            if val == 1:
                return key
        