class Solution:
    def threeSum(self, nums: List[int]) -> List[List[List[int]]]:
        nums.sort()  # 先排序：[-4, -1, -1, 0, 1, 2]
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # 判斷一：如果當前數字大於 0，後面更不可能相加等於 0（因為已排序）
            if nums[i] > 0:
                break
                
            # 判斷二：跳過重複的固定數，避免外層重複
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 雙指標只從 i 的下一個位置開始，往後搜尋
            left = i + 1
            right = n - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    # 找到一組解
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 關鍵：找到解後，left 和 right 都要跳過周圍重複的值
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # 指標繼續往內移動，尋找下一個可能的組合
                    left += 1
                    right -= 1
                    
        return res
