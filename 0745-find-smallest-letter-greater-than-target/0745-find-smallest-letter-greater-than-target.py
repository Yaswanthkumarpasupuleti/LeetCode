class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = "zz"
        left = 0
        right = len(letters)-1

        while left <= right :
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid+1
            else:
                if res > letters[mid]:
                    res = letters[mid]
                right = mid-1

        return res if res != "zz" else letters[0]
        