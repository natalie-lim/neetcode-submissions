class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        explored = [[0] * len(grid[0]) for _ in range(len(grid))]

        def explore(r, c):
            if r < 0 or c < 0:
                return 
            if r >= len(grid) or c >= len(grid[0]):
                return 
            if explored[r][c] == 1:
                return
            if grid[r][c] == "0":
                return

            explored[r][c] = 1
            explore(r+1, c)
            explore(r-1, c)
            explore(r, c+1)
            explore(r, c-1)

        total = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == "1" and explored[r][c] == 0:
                    explore(r, c)
                    total += 1

        return total