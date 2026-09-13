class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        # 建立 s1 和當前窗口的字母頻率計數器（大小為 26 的陣列）
        count1 = [0] * 26
        count2 = [0] * 26
        
        # 初始化第一個窗口
        for i in range(len1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        # 如果第一個窗口就匹配成功，直接返回 True
        if count1 == count2:
            return True
            
        # 開始滑動窗口
        for i in range(len1, len2):
            # 加入新字母（右邊界擴展）
            count2[ord(s2[i]) - ord('a')] += 1
            # 移除舊字母（左邊界收縮）
            count2[ord(s2[i - len1]) - ord('a')] -= 1
            
            # 比較當前窗口是否與 s1 的字母頻率完全一致
            if count1 == count2:
                return True
                
        return False
