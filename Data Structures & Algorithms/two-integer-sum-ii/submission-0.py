class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, val in enumerate(numbers):
            diff = target - val
            if diff in d:
                return [d[diff], i+1]
            else:
                d[val] = i+1