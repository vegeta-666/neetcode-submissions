class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        res = {}
        for s in strs:
            count = [0]*26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)

        result = []
        for value in res.values():
            result.append(value)
        # print(list[res.values()])
        return result
