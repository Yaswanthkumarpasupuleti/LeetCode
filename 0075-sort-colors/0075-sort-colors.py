class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cntZero = nums.count(0)
        # cntOne = nums.count(1)
        # cntTwo = nums.count(2)
        # # for i in range(len(nums)):
        # #     if nums[i] == 0:
        # #         cntZero += 1
        # #     elif nums[i] == 1:
        # #         cntOne += 1
        # #     elif nums[i] == 2:
        # #         cntTwo += 1
        # #     else:
        # #         continue
         
        # # i = 0
        # # while i < len(nums):
        # #     if i < cntZero:
        # #         nums[i] = 0
        # #         i+=1
        # #     elif i < cntOne and i > cntZero:
        # #         nums[i] = 1
        # #         i+=1
        # #     elif i < cntTwo and i > cntOne:
        # #         nums[i] = 2
        # #         i+=1

        # for i in range(0,cntZero):
        #     nums[i] = 0
        # for j in range(cntZero,cntZero+cntOne):
        #     nums[j] = 1
        # for k in range(cntOne+cntZero,cntZero+cntOne+cntTwo):
        #     nums[k] = 2

        first = 0
        last = len(nums)-1
        while first < last:
            if nums[first] > nums[last]:
                temp = nums[first]
                nums[first] = nums[last]
                nums[last] = temp
                first += 1
                last -= 1
            elif nums[first] < nums[last]:
                first += 1
            else:
                last -= 1
        nums.sort()
        

