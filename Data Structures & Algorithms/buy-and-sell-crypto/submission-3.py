class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 記錄當前最大獲利
        # 紀錄最小值
        res = 0
        min = prices[0]
        for price in prices:
            # print(price)
            if price < min:
                min = price
                continue
            else:
                if res < price-min:
                    res = price-min
                # res = max(res, price-min)

        return res