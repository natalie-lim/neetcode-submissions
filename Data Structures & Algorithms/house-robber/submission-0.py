class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        memo = {}
        def robbing(curr):
            if curr >= n:
                return 0
            if curr in memo:
                return memo[curr]
            
            max_val = float('-inf')

            for i in range(curr + 2, n + 2):
                val = nums[curr] + robbing(i)
                print(val)
                max_val = max(val, max_val)
            
            memo[curr] = max_val
            return memo[curr]

        return max(robbing(0), robbing(1))