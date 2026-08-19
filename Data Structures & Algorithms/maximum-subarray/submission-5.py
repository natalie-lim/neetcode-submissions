class Solution:
    # kadane's algo
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curSum = nums[0], 0
        # assumes that if a sum is negative it will never help 
        for num in nums:
            # if the sum is negative, zero it out
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)
        return maxSum