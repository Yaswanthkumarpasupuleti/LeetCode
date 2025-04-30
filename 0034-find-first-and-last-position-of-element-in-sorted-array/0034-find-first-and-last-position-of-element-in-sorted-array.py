class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # cnt = nums.count(target)
        # if target not in nums or cnt == 0 or len(nums) == 0:
        #     return [-1,-1]
        # else:
        #     #cnt = nums.count(target)
        #     idx = nums.index(target)
        #     res =[]
        #     # for i in range(idx,idx+cnt):
        #     #     res.append(i)
        #     res.append(idx)
        #     res.append(idx+cnt-1)
        #     # if len(res) == 1:
        #     #     res.append(res[0])
        #     return res
        leftidx = self.binarySearch(nums,target,True)
        rightidx = self.binarySearch(nums,target,False)
        return [leftidx,rightidx]
        
        
    def binarySearch(self,nums,target,leftBias):
        left , right = 0 ,len(nums)-1
        idx = -1
        while left <= right:
            mid =  (left+right) // 2
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
            else:
                idx = mid
                if leftBias:
                    right = mid-1
                else:
                    left = mid+1
        return idx
                    

        