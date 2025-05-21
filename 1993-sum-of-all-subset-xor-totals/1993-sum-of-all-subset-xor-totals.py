# class Solution:
#     def subsetXORSum(self, nums: List[int]) -> int:
#         subset = [[]]
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 sub = nums[i:j+1]
#                 subset.append(sub)
#         #subset.sort()
#         print(subset)
#         cnt = 0
#         for sub in subset:
#             sum = 0
#             for ele in sub:
#                 sum ^= ele
#             cnt+=sum
#         return cnt
class Solution:
    def subsetXORSum(self, nums):

        def generate_subsets(nums, index, subset, subsets):
            # Base case: index reached end of nums
            # Add the current subset to subsets
            if index == len(nums):
                subsets.append(subset[:])
                return

            # Generate subsets with nums[i]
            subset.append(nums[index])
            generate_subsets(nums, index + 1, subset, subsets)
            subset.pop()

            # Generate subsets without nums[i]
            generate_subsets(nums, index + 1, subset, subsets)

        # Generate all of the subsets
        subsets = []
        generate_subsets(nums, 0, [], subsets)

        # Compute the XOR total for each subset and add to the result
        result = 0
        for subset in subsets:
            subset_XOR_total = 0
            for num in subset:
                subset_XOR_total ^= num
            result += subset_XOR_total

        return result
