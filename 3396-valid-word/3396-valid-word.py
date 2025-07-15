class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vCnt=cCnt= 0
        for char in word:
            if char.isalpha():
                if char in "aeiouAEIOU":
                    vCnt += 1
                else:
                    cCnt += 1
            elif  not char.isdigit():
                return False
        if (vCnt >= 1) and (cCnt >= 1):
            return True
        return False

        