class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 拋棄掉小的
        left = 0
        right = len(heights)-1

        #for i in range(len(heights)):
        res = 0
        while left < right:
            container = (right-left) * min(heights[left], heights[right])
            res = max(res, container)
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else: #如果相等怎麼辦
                left += 1
            print(container)

        return res