class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        num_rows = len(text1)
        num_cols = len(text2)

        arr = [[-1] * num_cols for _ in range(num_rows)]

        def dp(r, c):
            if r < 0 or c < 0 or r >= num_rows or c >= num_cols:
                return 0
            if arr[r][c] != -1:
                return arr[r][c] 

            c1 = text1[r]
            c2 = text2[c]
            if c1 == c2:
                arr[r][c] = 1 + dp(r+1, c+1)
            else:
                arr[r][c] = max((dp(r+1, c), dp(r, c+1)))

            return arr[r][c]
        
        return dp(0, 0)