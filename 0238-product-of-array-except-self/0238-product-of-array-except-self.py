class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) == len(nums):
            return nums
        if nums.count(0) == len(nums)-1 and len(nums) > 2:
            return [0]*len(nums)
        res =  1
        flag = False
        for ele in nums:
            if ele == 0:
                flag = True
                continue
            else:
                res *= ele
        if flag:
            if nums.count(0) == 1:
                for i in range(len(nums)):
                    if nums[i] == 0:
                        nums[i]= res
                    else:
                        nums[i] = 0
            else:
                return [0]*len(nums)
        else:
            for i in range(len(nums)):
                 nums[i] = (res // nums[i])
        return nums
        