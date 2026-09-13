class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False

        count1 = [0] * 26
        count2 = [0] * 26

        # 1. 初始化第一個窗口（長度為 len1）
        for i in range(len1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # 保留第一筆的比對
        if count1 == count2: return True

        # 2. 定義指標：right 直接從 len1 開始，此時 left 就是 0
        left = 0
        for right in range(len1, len2):
            # 移除左邊舊字元，並將 left 前移
            count2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            
            # 加入右邊新字元
            count2[ord(s2[right]) - ord('a')] += 1
            
            # 每次同步移動後立刻比對
            if count1 == count2: return True

        return False
