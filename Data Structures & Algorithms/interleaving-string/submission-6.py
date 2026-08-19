class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1) # rows
        m = len(s2) # cols
        
        if n + m != len(s3):
            return False
        
        arr = [[None] * (m+1) for _ in range(n+1)]
        arr[n][m] = True

        def interleave(r, c, idx):
            nonlocal arr
            if arr[r][c] != None:
                return arr[r][c]

            first = False
            second = False

            if r < n and s1[r] == s3[idx]:
                first = interleave(r+1, c, idx+1)
            if c < m and s2[c] == s3[idx]:
                second = interleave(r, c+1, idx+1)

            arr[r][c] = first or second
            return arr[r][c]
        
        ans = interleave(0, 0, 0)
        print(arr)
        return ans