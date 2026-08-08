class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {} # sum: subset
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total / 2

        def recurse(idx, curr):
            if curr == target:
                return True
            if idx >= len(nums):
                return False
            
            # include or don't include
            next_curr = curr + nums[idx]

            if next_curr <= target:
                return recurse(idx + 1, next_curr) or recurse(idx + 1, curr)
            else:
                return recurse(idx + 1, curr)

        return recurse(0, 0)