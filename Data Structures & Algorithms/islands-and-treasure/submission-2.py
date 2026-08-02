class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # not super pressing, initially solved w flooding dfs instead of multi-source bfs
        inf = 2147483647

        rows, cols = len(grid), len(grid[0])
        q = deque()

        # creating all the source points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))