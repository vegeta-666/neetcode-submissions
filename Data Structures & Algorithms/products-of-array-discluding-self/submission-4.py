class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, surfix = [0]*len(nums), [0]*len(nums)
        prod_prfix, prod_sufix = 1, 1

        for i in range(len(nums)):
            prod_prfix = prod_prfix*nums[i]
            prefix[i] = prod_prfix
        for i in range(len(nums)-1, -1, -1):
            prod_sufix = prod_sufix*nums[i]
            surfix[i] = prod_sufix
        print(prefix[-2])
        res = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = surfix[1]
            elif i == len(nums)-1:
                print(i)
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * surfix[i+1]

        return res