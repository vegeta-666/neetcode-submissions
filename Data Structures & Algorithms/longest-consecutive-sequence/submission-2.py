class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        logest = 0

        for num in nums:
            if num-1 not in num_set:
                length = 1
                while num+length in num_set:
                    length += 1
                logest = max(logest, length)
        return logest