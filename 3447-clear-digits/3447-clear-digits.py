class Solution:
    def clearDigits(self, s: str) -> str:
        res = []
        for char in s:
            if char in "1234567890":
                res.pop()
            else:
                res.append(char)
        return "".join(res)
        