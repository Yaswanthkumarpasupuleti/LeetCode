class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        cnt =0
        for i in nums:
            if i < 0:
                cnt+=1
        if cnt % 2 == 0:
            return 1
        return -1
        