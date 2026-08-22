class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # for each subarray, you can basically choose one to pop. memoize by big ahh tuples
        memo = {}

        def pop(arr):
            if len(arr) == 0:
                return 0
            
            if tuple(arr) in memo:
                return memo[tuple(arr)]

            m = float('-inf')

            for i, n in enumerate(arr):
                first = 1
                if i-1 >= 0:
                    first = arr[i-1]
                third = 1
                if i+1 < len(arr):
                    third = arr[i+1]
                second = arr[i]

                mult = first * second * third
                firsttry = mult + pop(arr[0:i] + arr[i+1:])
                m = max(m, firsttry)

            memo[tuple(arr)] = m
            return memo[tuple(arr)]

        return pop(nums)
            