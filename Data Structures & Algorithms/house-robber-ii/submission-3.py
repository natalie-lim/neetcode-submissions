class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        memo = {} # n: {start: val}

        def robbing(curr, start):
            if curr == n - 1 and start == 0:
                return 0
            if curr >= n:
                return 0
            if curr in memo:
                d = memo[curr]
                if start in d:
                    return d[start]

            lots = 0
            for i in range(curr + 2, n + 2):
                lots = max(lots, nums[curr] + robbing(i, start))
            
            prev_d = memo[curr] if curr in memo else {}
            prev_d[start] = lots
            memo[curr] = prev_d
            return prev_d[start]
            
        max_val = 0
        for i in range(n):
            print("run?")
            max_val = max(max_val, robbing(i, i))
        print(memo)

        return max_val
