class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        min_left = prices[0]
        max_profit = 0

        for i in prices[1:]:
            if i >= min_left:
                profit = i - min_left
                if profit > max_profit:
                    max_profit = profit
            else:
                min_left = i

        return max_profit