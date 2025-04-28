class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == " ":
                continue
            elif char == "[" or char  == "{" or char == "(":
                stack.append(char)
            elif char == "]" or char == "}" or char == ")":
                if len(stack) < 1:
                    return False
                out = stack.pop()
                if char == "]" and out == "[":
                    continue
                elif char == "}" and out == "{":
                    continue
                elif char == ")" and out == "(":
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        