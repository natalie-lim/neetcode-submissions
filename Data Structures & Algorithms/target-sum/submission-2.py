class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(idx, amt):
            if idx == len(nums):
                if amt == target:
                    return 1
            if idx >= len(nums):
                return 0
            if (idx, amt) in memo:
                return memo[(idx, amt)]
            
            num = nums[idx]
            memo[(idx, amt)] = dp(idx+1, amt-num) + dp(idx+1, amt+num)
            return memo[(idx, amt)]
        
        return dp(0, 0)