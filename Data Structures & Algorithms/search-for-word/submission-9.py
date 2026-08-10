class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows = len(board)
        num_cols = len(board[0])

        def explore(idx, r, c, explored):
            if idx >= len(word):
                return True
            if r < 0 or c < 0:
                return False
            if r >= num_rows or c >= num_cols:
                return False
            if board[r][c] != word[idx]:
                return False
            if explored[r][c] != 0:
                return False

            explored[r][c] = 1
            up = explore(idx+1, r-1, c, explored)
            down = explore(idx+1, r+1, c, explored)
            left = explore(idx + 1, r, c-1, explored)
            right = explore(idx + 1, r, c+1, explored)
            found = up or down or left or right
            if not found:
                explored[r][c] = 0
            return found

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val == word[0]:
                    explored = [[0] * num_cols for _ in range(num_rows)]
                    if explore(0, r, c, explored):
                        return True

        return False
