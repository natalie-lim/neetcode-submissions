class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        left.append(1)
        right = []
        right.append(1)

        # filling left
        for i, n in enumerate(nums):
            if i != 0:
                left.append(left[i-1] * nums[i-1])

        # filling right
        for i, n in enumerate(reversed(nums[1:])):
            right.append(right[-1] * n)

        right.reverse()

        

        arr = []
        for i in range(len(nums)):
            arr.append(left[i] * right[i])

        return arr