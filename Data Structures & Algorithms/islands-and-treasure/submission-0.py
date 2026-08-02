class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def spread(r, c, dist):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            curr_dist = grid[r][c]
            if curr_dist < dist:
                return

            grid[r][c] = dist

            # up
            spread(r - 1, c, dist + 1)
            # down
            spread(r + 1, c, dist + 1)
            # left
            spread(r, c - 1, dist + 1)
            # right
            spread(r, c + 1, dist + 1)

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    spread(r, c, 0)
