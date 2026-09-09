class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, surfix, res = [0]*n, [0]*n, [0]*n
        prefix[0] = surfix[-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-2, -1, -1):
            surfix[i] = nums[i+1] * surfix[i+1]
        for i in range(n):
            res[i] = prefix[i] * surfix[i]
        
        return res