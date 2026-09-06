class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        res = {}

        for s in strs:
            c = [0]*26
            for i in range(len(s)):
                c[ord(s[i])-ord('a')] += 1
            
            key = tuple(c)

            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())
