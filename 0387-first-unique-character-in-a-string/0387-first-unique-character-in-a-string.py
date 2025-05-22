class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        for i in range(0,len(s)):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
        # n = len(s)
        # if s[n-1] not in s[:n-1]:
        #     return len(s)-1
        return -1
        