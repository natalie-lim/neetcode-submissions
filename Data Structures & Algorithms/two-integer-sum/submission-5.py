class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {} # val, idx

        for i, n in enumerate(nums):
            rest = target - n
            if rest in d:
                return [d[rest], i]
            d[n] = i

        return [-1]