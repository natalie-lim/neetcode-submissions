class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        tally = 0
        
        explored = [[0] * n for _ in range(m)]

        memo = {}

        def explore(r, c, explored):
            nonlocal tally
            if r == m-1 and c == n-1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            if r < 0 or c < 0:
                return 0
            if r > m-1 or c > n-1:
                return 0
            if explored[r][c] == 1:
                return 0
            
            explored[r][c] = 1
            # down + right
            memo[(r, c)] = explore(r+1, c, explored)+ explore(r, c+1, explored)
            explored[r][c] = 0
            return memo[(r, c)]

        return explore(0, 0, explored)
        