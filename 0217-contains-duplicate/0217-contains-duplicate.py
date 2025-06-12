class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for ele in nums:
            hashset.add(ele)
        if len(hashset) < len(nums):
            return True
        return False

        