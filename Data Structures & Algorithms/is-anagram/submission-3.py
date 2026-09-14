class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = [0]*26
        tCount = [0]*26

        for si in range(len(s)):
            sCount[ord(s[si])-ord('a')] += 1
            tCount[ord(t[si])-ord('a')] += 1

        return sCount == tCount