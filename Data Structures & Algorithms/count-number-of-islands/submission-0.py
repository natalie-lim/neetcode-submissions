class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_cols = len(grid[0])
        num_rows = len(grid)

        found = [[0] * num_cols for _ in range(num_rows)]

        def findIsland(r, c):
            if r < 0 or c < 0:
                return
            if r >= num_rows or c >= num_cols:
                return
            if found[r][c] == 1:
                return

            if grid[r][c] == "1":
                found[r][c] = 1
            else:
                return

            # go right
            findIsland(r, c-1)
            # go left
            findIsland(r, c+1)
            # go up
            findIsland(r - 1, c)
            # go down
            findIsland(r + 1, c)

        numIslands = 0

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1" and found[r][c] == 0:
                    findIsland(r, c)
                    numIslands += 1

        return numIslands