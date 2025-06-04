class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_substring = ""
        max_len = n - numFriends + 1
        for i in range(n):
            end_index = min(i + max_len, n)
            current = word[i:end_index]
            if current > max_substring:
                max_substring = current
        return max_substring
    