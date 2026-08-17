class Solution:
    def maxProfit(self, prices):
        hold, sold, rest = float('-inf'), 0, 0

        for p in prices:
            prev_sold = sold
            sold = hold + p            # sell today
            hold = max(hold, rest - p) # keep holding, or buy today
            rest = max(rest, prev_sold) # keep resting, or cooldown just ended
        return max(sold, rest)
