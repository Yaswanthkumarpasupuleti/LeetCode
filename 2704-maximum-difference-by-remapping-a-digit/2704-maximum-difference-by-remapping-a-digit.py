class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        temp = s
        idx = 0
        while idx < len(s) and s[idx] == "9":
            idx += 1
        if idx < len(s):
            s = s.replace(s[idx],"9")
        temp = temp.replace(temp[0],"0")
        return int(s) - int(temp)
        