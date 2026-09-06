class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        arr = []
        for num, count in res.items():
            arr.append([count, num])
        arr.sort()

        r = []
        for i in range(k):
            r.append(arr.pop()[1])

        return r