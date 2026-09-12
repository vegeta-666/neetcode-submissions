class Solution:
    def isValid(self, s: str) -> bool:
        opposites = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []
        for i in range(0, len(s)):
            if s[i] not in opposites.keys():
                stack.append(s[i])
            else:
                if not stack or opposites[s[i]] != stack.pop(-1):
                    return False

        return not stack

