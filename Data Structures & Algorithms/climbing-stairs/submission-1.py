class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def climb (curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in memo:
                return memo[curr]
            
            memo[curr] = climb(curr + 1) + climb(curr + 2)
            return memo[curr]
        
        climb(0)
        return memo[0]