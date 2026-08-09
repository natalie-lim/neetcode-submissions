class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        arr.append(1)

        # left pass

        for i, n in enumerate(nums):
            if i != 0:
                arr.append(arr[i-1] * nums[i-1])
        
        # right pass
        running_prod = 1

        for i in range(len(nums) - 2, -1, -1):
            if i != len(nums) - 1:
                running_prod *= nums[i+1] 
                arr[i] *= running_prod

        return arr