class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lcnt = rcnt = maxlength = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                lcnt += 1
            else:
                rcnt += 1
            
            if lcnt == rcnt:
                maxlength = max(maxlength,lcnt+rcnt)
            elif lcnt < rcnt:
                lcnt = rcnt = 0
            i+=1

        i = len(s)-1
        lcnt = rcnt =0
        while i > 0:
            if s[i] == ")":
                lcnt+=1
            else:
                rcnt += 1
            
            if lcnt == rcnt:
                maxlength = max(maxlength,lcnt+rcnt)
            elif lcnt < rcnt:
                lcnt = rcnt = 0
            i -= 1 

        return maxlength
        