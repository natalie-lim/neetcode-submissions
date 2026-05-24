class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        idx = 0
        for i in nums:
            diff = target - i
            if diff in d:
                return [d[diff], idx]
            else:
                d[i] = idx
                idx += 1