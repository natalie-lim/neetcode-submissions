class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {} # n, val

        def pow_pos (x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            first = math.ceil(n / 2)
            second = math.floor(n / 2)
            ans = pow_pos (x, first) * pow_pos (x, second)
            memo[n] = ans
            return ans
        
        def pow_neg (x, n):
            if n == -1:
                return 1 / x
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            first = math.ceil(n / 2)
            second = math.floor(n / 2)
            ans = pow_neg (x, first) * pow_neg (x, second)
            memo[n] = ans
            return ans
        
        if n >= 0:
            return pow_pos (x, n)
        else:
            return pow_neg(x, n)