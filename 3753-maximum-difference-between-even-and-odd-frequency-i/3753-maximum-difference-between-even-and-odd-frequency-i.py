class Solution:
    def maxDifference(self, s: str) -> int:
        # freq  = {}
        # for char in s:
        #     if char in freq:
        #         freq[char] += 1
        #     else:
        #         freq[char] = 1
        # oddmax = evenmax = 0
        # for val in freq.values():
        #     if (val % 2 != 0) and (val > oddmax):
        #         oddmax = val
        #     if (val % 2 == 0) and (val > evenmax):
        #         evenmax = val
        # return oddmax - evenmax  
        c = Counter(s)
        print(c)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        print(maxOdd)
        minEven = min(x for x in c.values() if x % 2 == 0)
        print(minEven)
        return maxOdd - minEven      
        