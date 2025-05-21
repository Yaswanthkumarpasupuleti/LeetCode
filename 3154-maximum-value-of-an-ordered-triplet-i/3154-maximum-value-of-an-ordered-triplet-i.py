class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                #sum = 0
                for k in range(j+1,len(nums)):
                    sum = (nums[i]-nums[j])*nums[k]
                    if sum > res :
                        res = sum
        return res if res >= 0 else 0

        