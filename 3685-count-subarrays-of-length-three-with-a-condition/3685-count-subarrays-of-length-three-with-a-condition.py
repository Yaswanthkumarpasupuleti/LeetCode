class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)-2):
            first = nums[i]
            second = nums[i+1]
            third = nums[i+2]
            if (first+third) == (second/2):
                cnt += 1
        return cnt
        