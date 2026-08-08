class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ult_max = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for n in nums[1:]:
            candidates = (n, max_prod * n, min_prod * n)
            # start here, end here, end here
            max_prod = max(candidates)
            min_prod = min(candidates)
            ult_max = max(ult_max, max_prod)

        return(ult_max)
        