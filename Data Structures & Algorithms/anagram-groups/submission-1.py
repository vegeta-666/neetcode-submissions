class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        result = {}
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i) - ord('a')] += 1

            key = tuple(count)
            if key not in result:
                result[key] = []
            result[key].append(s)

        return list(result.values())