class Solution:
    def helper(self, nums, target, start, end):
        if (end - start <= 1):
            end_val = nums[end]
            start_val = nums[start]
            if end_val == target:
                return end
            elif start_val == target:
                return start
            else:
                return -1
        mid_idx = (start + end) // 2
        start_val = nums[start]
        end_val = nums[end]
        mid_val = nums[mid_idx]
        # if rotated
        if start_val > end_val:
            if mid_val < start_val:
                # left side is greater than start or less than mid
                if target >= start_val or target <= mid_val:
                    return self.helper(nums, target, start, mid_idx)
                else:
                    return self.helper(nums, target, mid_idx, end)
            else:
                # left side is less than mid and greater than right
                if target <= mid_val and target >= end_val:
                    return self.helper(nums, target, start, mid_idx)
                else:
                    return self.helper(nums, target, mid_idx, end)
        else:
            if target <= mid_val:
                return self.helper(nums, target, start, mid_idx)
            else:
                return self.helper(nums, target, mid_idx, end)


    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, target, 0, (len(nums) - 1))
        