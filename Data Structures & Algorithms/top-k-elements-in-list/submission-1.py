class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket solution
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # create bucket
        feq = [ [] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            feq[cnt].append(num)

        res = []
        for i in range(len(feq)-1, 0, -1):
            for num in feq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        