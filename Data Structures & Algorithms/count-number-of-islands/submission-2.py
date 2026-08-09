class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        checked = [[0] * len(grid[0]) for _ in range(len(grid))]

        def explore(r, c):
            if r < 0 or r >= len(grid):
                return
            if c < 0 or c >= len(grid[0]):
                return
            if checked[r][c] == 1:
                return
            if grid[r][c] == "0":
                return

            checked[r][c] = 1
            # up
            explore(r-1, c)
            # down
            explore(r+1, c)
            # left
            explore(r, c-1)
            # right
            explore(r, c+1)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1" and checked[r][c] == 0:
                    explore(r, c)
                    num_islands += 1

        return num_islands

