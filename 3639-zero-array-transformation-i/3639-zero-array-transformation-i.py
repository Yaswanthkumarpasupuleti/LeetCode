class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # maxele = max(nums)
        # secmax = nums.sort()
        # secmaxele = 0
        # for ele in range(-1,0,-1):
        #     if secmax[ele] != secmax[ele-1]:
        #         secmaxele = secmax[ele-1]
        # n = len(queries)
        # idx = nums.index(maxele)
        # # idx1 = nums.index(secmaxele)
        # cnt = 0
        # # cnt1 =0
        # if secmaxele != 0:
        #     idx1 = nums.index(secmaxele)
        #     cnt1 =0
        #     for ele in queries:
        #         l = ele[0]
        #         r = ele[1]
        #         if l == r :
        #             if maxele == nums[l]:
        #                 cnt +=1
        #             elif secmaxele == nums[l]:
        #                 cnt1 +=2
        #         elif (idx in range(l,r+1)):
        #             cnt +=1 
        #         elif idx in range(l,r+1):
        #             cnt1 += 1
        #     if cnt < maxele or cnt1 < secmaxele:
        #         return False
        #     return True
        # else:
        #     for ele in queries:
        #         l = ele[0]
        #         r = ele[1]
        #         if l == r :
        #             if maxele == nums[l]:
        #                 cnt +=1
        #             # elif secmaxele == nums[l]:
        #             #     cnt1 +=2
        #         elif (idx in range(l,r+1)):
        #             cnt +=1 
        #         # elif idx in range(l,r+1):
        #         #     cnt1 += 1
        #     if cnt < maxele:
        #         return False
        #     return True
    
        n = len(nums)
        difArray = [0] * (n + 1)

        for l, r in queries:
            difArray[l] += 1
            difArray[r + 1] -= 1

        for i in range(1, n):
            difArray[i] += difArray[i - 1]
        
        for i in range(n):
            if nums[i] > difArray[i]:
                return False
        return True

