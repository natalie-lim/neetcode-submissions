class Solution:
    def findOneWord(self, start_r, start_c, board, word, idx, checker):
        if idx >= len(word):
            return True
        if start_r < 0 or start_r >= len(board):
            return False
        if start_c < 0 or start_c >= len(board[0]):
            return False
        if checker[start_r][start_c] == 1:
            return False
        
        next_char = word[idx]
        board_char = board[start_r][start_c]
        if next_char == board_char:
            checker[start_r][start_c] = 1
        if next_char != board_char:
            return False
        # check up
        up = self.findOneWord((start_r - 1), start_c, board, word, (idx + 1), checker)
        # check right
        right = self.findOneWord(start_r, (start_c + 1), board, word, (idx + 1), checker)
        # check down
        down = self.findOneWord((start_r + 1), start_c, board, word, (idx + 1), checker)
        # check left
        left = self.findOneWord(start_r, (start_c - 1), board, word, (idx + 1), checker)
        return up or right or down or left


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = {}
        # step 1: log coordinates of letters
        for r, row in enumerate(board):
            for c, letter in enumerate(row):
                if letter not in d:
                    d[letter] = [(r, c)]
                else:
                    a = d[letter]
                    a.append((r, c))
                    d[letter] = a

        arr = set()
        # step 2: recursive helper method 
        for word in words:
            first_char = word[0]
            if first_char in d: 
                for r, c in d[first_char]:
                    checker = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                    if self.findOneWord(r, c, board, word, 0, checker):
                        arr.add(word)

        return list(arr)