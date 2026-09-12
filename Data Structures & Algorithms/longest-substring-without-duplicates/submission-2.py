class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, res = 0, 0
        seen = set()
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, len(s[left:right+1]))
        return res
