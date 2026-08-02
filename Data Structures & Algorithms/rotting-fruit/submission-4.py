class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        rotten_q = deque()
        fresh_q = deque()

        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    rotten_q.append((r, c))
                if val == 1:
                    fresh_q.append((r, c))

        if len(rotten_q) == 0 and len(fresh_q) == 0:
            return 0
        
        def canMove (r, c):
            if (r >= 0 and r < num_rows and c >= 0 and c < num_cols and grid[r][c] == 1):
                return True
            else:
                return False

        def spreadRotten(q, minutes):
            if len(q) == 0:
                return minutes - 1
            new_q = []
            # have to mark the grid right away so recursion doesnt dupe it
            for r, c in q:
                # up
                if canMove(r - 1, c):
                    grid[r-1][c] = 2
                    new_q.append((r-1, c))
                # down
                if canMove(r + 1, c):
                    grid[r+1][c] = 2
                    new_q.append((r+1, c))
                # left
                if canMove(r, c-1):
                    grid[r][c-1] = 2
                    new_q.append((r, c-1))
                # right
                if canMove(r, c+1):
                    grid[r][c+1] = 2
                    new_q.append((r, c+1))
            return spreadRotten(new_q, minutes + 1)
        
        minutes = spreadRotten (rotten_q,0)

        for r, c in fresh_q:
            if grid[r][c] == 1:
                return -1
        
        return minutes