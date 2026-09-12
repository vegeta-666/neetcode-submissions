class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = {"}": '{', ")": "(", "]": "["}
        for c in s:
            if c in mappings:
                if not stack or stack.pop() != mappings[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0