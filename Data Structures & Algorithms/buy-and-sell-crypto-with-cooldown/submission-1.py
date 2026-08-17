class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def profit(idx, buy_idx):
            if idx >= len(prices):
                return 0

            if (idx, buy_idx) in memo:
                return memo[(idx, buy_idx)]
            
            # sell or ignore
            if buy_idx >= 0:
                prof = prices[idx] - prices[buy_idx]
                memo[(idx, buy_idx)] = max(prof + profit(idx+2, -1),profit(idx+1, buy_idx))
                return memo[(idx, buy_idx)]
            
            # buy or ignore
            else:
                memo[(idx, buy_idx)] = max(profit(idx+1, idx), profit(idx + 1, -1))
                return memo[(idx, buy_idx)]
        
        return profit(0, -1)