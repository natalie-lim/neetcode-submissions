class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        num_cols = len(grid[0])
        num_rows = len(grid)

        found = [[0] * num_cols for _ in range(num_rows)]

        def findIsland(r, c) -> int:
            if r < 0 or c < 0 or r >= num_rows or c >= num_cols:
                return 0
            if found[r][c] == 1:
                return 0
            if grid[r][c] == 1:
                found[r][c] = 1
            else:
                return 0
            
            return (1 + findIsland(r - 1, c) + findIsland(r + 1, c) 
                + findIsland(r, c - 1) + findIsland(r, c + 1))

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if found[r][c] == 0 and val == 1:
                    max_area = max(max_area, findIsland(r, c))

        return max_area