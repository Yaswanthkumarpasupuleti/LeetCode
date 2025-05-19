class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums.count(nums[0]) == 3:
            return "equilateral"
        if len(nums) > 3:
            return "none"
        flag = False
        if ((nums[0]+nums[1]) > nums[2]) and ((nums[0]+nums[2]) > nums[1]) and ((nums[1]+nums[2]) > nums[0]):
            flag = True
        if flag:
            if (nums[0] == nums[1]) or (nums[0] == nums[2]) or (nums[1] ==nums[2]):
                return "isosceles"
            return "scalene"
        return "none"
        