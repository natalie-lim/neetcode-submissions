class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        res = []
        prod = 1

        left.append(prod)

        for i in range(len(nums[1:])):
            print(prod)
            prod *= nums[i]
            left.append(prod)

        prod = 1

        right.append(prod)

        for i in reversed(range(len(nums[::-1]))):
            right.insert(0, prod)
            prod *= nums[i]
        
        print (len(left))
        print (left)
        print (len(right))
        
        l = []
        for i in range(len(nums)):
            l.append(left[i] * right[i])

        return l