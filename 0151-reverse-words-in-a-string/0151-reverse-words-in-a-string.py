class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        lst = s.split()
        lst = lst[::-1]
        for ele in lst:
            res+= ele+" "
        return res[:-1]
        