class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo= {} #(idx, prev_idx), longest increasing sub

        def recurse(idx, prev_idx):
            if idx >= len(nums):
                return 0
            if (idx, prev_idx) in memo:
                return memo[(idx, prev_idx)]
            if prev_idx is not None and nums[idx] <= nums[prev_idx]:
                memo[(idx, prev_idx)] = recurse(idx + 1, prev_idx)
            else:
                # don't include this one
                first = 0 + recurse(idx + 1, prev_idx)
                # include this one
                second = 1 + recurse(idx + 1, idx)
                memo[(idx, prev_idx)] = max(first, second)

            return memo[(idx, prev_idx)]

        val = recurse(0, None)
        return val