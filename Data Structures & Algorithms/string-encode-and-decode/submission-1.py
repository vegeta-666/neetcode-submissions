class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        start = 0
        res = []
        while start < len(s):
            # get the number
            n = ""
            for c in s[start:]:
                if c == "#":
                    break
                n += c
            end = start + int(n) + len(n) + 1 #
            # print out the wording, and res
            res.append(s[start+1+len(n):end])
            start = end

        return res
