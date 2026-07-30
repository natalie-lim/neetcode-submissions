class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def helper(arr_left):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for idx, n in enumerate(arr_left):
                subset.append(n)
                a = arr_left.copy()
                del a[idx]
                helper(a)
                subset.pop()
        
        helper(nums)
        return res