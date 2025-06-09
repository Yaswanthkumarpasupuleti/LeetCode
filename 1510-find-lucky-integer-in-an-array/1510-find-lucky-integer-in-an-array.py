class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # freq = {}
        # for ele in arr:
        #     if ele not in freq:
        #         freq[ele] = 1
        #     else:
        #         freq[ele] += 1
        # res = - 1
        # for key,val in freq.items():
        #     if val == key and key > res:
        #         res = key
        # return res

        res = -1
        for ele in arr:
            if ele == arr.count(ele) and ele > res:
                res = ele
        return res

        

        