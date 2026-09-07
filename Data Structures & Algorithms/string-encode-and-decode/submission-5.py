class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        lag = 0
        res = []
        # 5#Hello5#World
        # 10#HelloWorld5#World
        while lag < len(s):
            lead = lag
            # number
            for i in s[lag:]:
                if i == '#':
                    break
                lead += 1
            # wording lag=0, lead=1, 
            print(int(s[lag:lead]))
            # lag=2, lead=7
            length = int(s[lag:lead])
            lag = lead + 1
            lead = lag + length
            res.append(s[lag:lead])
            lag = lead
        return res