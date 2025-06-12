class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = -1
        n = len(nums)
        for i in range(n-1):
            diff = abs(nums[i] - nums[i+1])
            if diff > res:
                res = diff
        diff = abs(nums[n-1] - nums[0])
        if res < diff:
            res = diff
        return res
        


        