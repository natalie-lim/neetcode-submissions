class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def climb(curr):
            if curr >= n:
                return 0
            if curr in memo:
                return (memo[curr])

            memo[curr] = cost[curr] + min((climb(curr+1)), (climb(curr+2)))
            return memo[curr]
        
        return min(climb(0), climb(1))
        
        