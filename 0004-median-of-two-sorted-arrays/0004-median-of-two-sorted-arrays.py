class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                mergedArray.append(nums1[i])
                i+=1
            else:
                mergedArray.append(nums2[j])
                j += 1
        if i < len(nums1):
            for k in range(i,len(nums1)):
                mergedArray.append(nums1[k])
        if j < len(nums2):
            for l in range(j,len(nums2)):
                mergedArray.append(nums2[l])
        #print(mergedArray)
        if len(mergedArray) % 2 == 0:
            mid = (mergedArray[len(mergedArray)//2]+mergedArray[(len(mergedArray)//2)-1])/2
            return mid
        else:
            return mergedArray[len(mergedArray)//2]

        