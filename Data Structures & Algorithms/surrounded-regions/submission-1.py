class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])

        def surround(r, c):
            if r < 0 or c < 0:
                return
            if r >= num_rows or c >= num_cols:
                return
            if board[r][c] == "X":
                return
            board[r][c] = "X"
            # up
            surround(r-1, c)
            # down
            surround(r+1, c)
            # left
            surround(r, c-1)
            # right
            surround(r, c+1)

        def isIsland(r, c, blank):
            if r < 0 or c < 0:
                return False
            if r >= num_rows or c >= num_cols:
                return False
            if board[r][c] == "X":
                return True
            if blank[r][c] == 1:
                return True

            blank[r][c] = 1
            return (isIsland(r-1, c, blank) 
                and isIsland(r+1, c, blank) 
                and isIsland(r, c-1, blank) 
                and isIsland(r, c+1, blank))

        
        for r, row in enumerate(board):
            if r > 0 and r < num_rows - 1:
                for c, val in enumerate(row):
                    if c > 0 and c < num_cols - 1: 
                        blank = [[0] * num_cols for _ in range(num_rows)]
                        if val == "O" and isIsland(r, c, blank):
                            surround(r, c)