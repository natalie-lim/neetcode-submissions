class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pt1 = 0
        pt2 = 1
        profit = 0

        while pt2 < len(prices):
            val1 = prices[pt1]
            val2 = prices[pt2]
            if val2 < val1:
                pt1 = pt2
            else:
                profit = max(profit, val2 - val1)
            pt2 += 1

        profit = max(profit, prices[-1] - prices[pt1])
        return profit