class Solution:
    def search_helper(self, nums: List[int], start: int, end: int, target: int) -> int:
        if (end < start):
            return -1
        middle_pt = int((end + start) / 2)
        middle_val = nums[middle_pt]
        print(middle_val)
        if middle_val == target:
            return middle_pt
        elif target > middle_val:
            return self.search_helper(nums, middle_pt + 1, end, target)
        else:
            return self.search_helper(nums, start, middle_pt - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.search_helper(nums, 0, len(nums) - 1, target)
