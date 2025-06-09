class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # res = 0
        # for ele in nums:
        #     res ^= ele
        # return res
        freq = {}
        for ele in nums:
            if ele in freq:
                freq[ele] += 1
            else:
                freq[ele] = 1
        for key, val in freq.items():
            if val == 1:
                return key
        