class Solution:
    def helper(self, start, end, nums) -> int:
        if (end - start <= 1):
            n1 = nums[start]
            n2 = nums[end]
            if n1 < n2:
                return n1
            else:
                return n2

        mid_idx = (end + start) // 2
        mid_val = nums[mid_idx]
        start_val = nums[start]
        end_val = nums[end]

        if mid_val > start_val:
            #go right
            if end_val > start_val:
                return self.helper(start, mid_idx, nums)
            return self.helper(mid_idx, end, nums)
        else:
            #go left
            return self.helper(start, mid_idx, nums)

    def findMin(self, nums: List[int]) -> int:
        return self.helper(0, len(nums) - 1, nums)
        