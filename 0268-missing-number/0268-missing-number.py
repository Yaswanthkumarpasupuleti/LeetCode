class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        listSum = 0
        n = len(nums)
        for i in range(0,n):
            listSum += nums[i]
        print(listSum)
        actualSum = (n*(n+1))//2
        print(actualSum)
        return actualSum - listSum
        