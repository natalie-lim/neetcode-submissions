class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(houses):
            prev, curr = 0, 0

            for n in houses:
                prev, curr = curr, max(curr, prev + n)
            
            return curr
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))