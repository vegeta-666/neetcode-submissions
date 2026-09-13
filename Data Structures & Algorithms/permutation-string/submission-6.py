from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2: return False

        # 直接建立 s1 的計數字典
        dict1 = Counter(s1)
        # 建立 s2 第一個窗口的計數字典
        dict2 = Counter(s2[:len1])

        if dict1 == dict2: return True

        # 滑動窗口
        for i in range(len1, len2):
            dict2[s2[i]] += 1          # 增加右邊字元
            dict2[s2[i - len1]] -= 1   # 減少左邊字元

            # 🔥 Counter 的神奇之處：
            # 即使左邊字元扣到 0，只要使用 + 操作符（例如 dict2 + Counter()）
            # 或者直接比對，Python 3 的 Counter 比較會正確處理。
            # 但最安全且保證乾淨的做法是手動刪除 0 的項：
            if dict2[s2[i - len1]] == 0:
                del dict2[s2[i - len1]]

            if dict1 == dict2:
                return True

        return False
