class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def helper(i):
            if sum(curr) == target:
                res.append(curr.copy())
                return
            if sum(curr) > target:
                return
            if i >= len(nums):
                return
            curr.append(nums[i])
            helper(i)
            curr.pop()
            helper(i + 1)

        helper(0)
        return res
