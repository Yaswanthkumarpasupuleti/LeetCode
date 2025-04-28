class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        if len(s) == 1:
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(substring) > len(res):
                    res = substring
        return res
        