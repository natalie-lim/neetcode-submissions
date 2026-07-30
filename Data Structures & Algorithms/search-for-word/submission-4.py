class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        curr_char = word[0]

        def find(r, c, idx, arr):

            if idx >= len(word):
                return True

            curr_char = word[idx]
            up = board[r-1][c] if r-1 >= 0 and arr[r-1][c] == 0 else None

            if up == curr_char:
                print("up")
                arr[r-1][c] = 1
                if find(r-1, c, idx + 1, arr):
                    return True
                arr[r-1][c] = 0

            down = board[r+1][c] if r+1 < len(board) and arr[r+1][c] == 0 else None
            if down == curr_char:
                print("down")
                arr[r+1][c] = 1
                if find(r+1, c, idx + 1, arr):
                    return True
                arr[r+1][c] = 0

            left = board[r][c-1] if c-1 >= 0 and arr[r][c-1] == 0 else None
            if left == curr_char:
                print("left")
                arr[r][c - 1] = 1
                if find(r, c - 1, idx + 1, arr):
                    return True
                arr[r][c - 1] = 0

            right = board[r][c + 1] if c+1 < len(board[0]) and arr[r][c + 1] == 0 else None
            if right == curr_char:
                print("right")
                arr[r][c+1] = 1
                if find(r, c + 1, idx + 1, arr):
                    return True
                arr[r][c+1] = 0
                
            return (False)

        for r, row in enumerate(board):
            for c, let in enumerate(row):
                if let == curr_char:
                    print("should tx")
                    arr = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                    arr[r][c] = 1
                    if find(r, c, 1, arr):
                        return True
        return False
    