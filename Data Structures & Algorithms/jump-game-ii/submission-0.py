class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {} # idx, min

        def help(idx):
            if idx >= len(nums):
                return float('inf')
            if idx == len(nums) - 1:
                return 0
            if idx in memo:
                return memo[idx]
            val = nums[idx]
            curr_min = float('inf')
            for i in range(val + 1):
                if i != 0:
                    curr_min = min(curr_min, 1 + help(idx + i))
            memo[idx] = curr_min
            return memo[idx]

        return help(0)