class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, sur, res = [0]*n, [0]*n, [0]*n
        pre[0] = sur[-1] = 1
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            sur[i] = sur[i+1] * nums[i+1]
        for i in range(n):
            res[i] = pre[i] * sur[i]

        return res