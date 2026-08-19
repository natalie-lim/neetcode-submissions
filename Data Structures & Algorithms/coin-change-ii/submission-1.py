class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {} # (idx, amt): answer
        
        def helper(idx, amt):
            if idx >= len(coins):
                return 0
            if amt > amount:
                return 0
            if amt == amount:
                return 1
            if (idx, amt) in memo:
                return memo[(idx, amt)]

            coin = coins[idx]
            # try same
            same = helper(idx, coin + amt)
            # dont use
            dont = helper(idx+1, amt)

            memo[(idx, amt)] = same  + dont
            return memo[(idx, amt)]


        return helper(0, 0)