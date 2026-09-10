class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        overall_max=0
        while l<r:
            local_max=(r-l)*min(heights[l],heights[r])
            if local_max>overall_max:
                overall_max=local_max
            if heights[l]>heights[r]:
                r=r-1
            else:
                l=l+1
        return overall_max


        