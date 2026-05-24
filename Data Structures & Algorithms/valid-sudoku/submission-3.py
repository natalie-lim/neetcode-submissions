class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # dict of row sets (key idx, val list)
        d_row = {}
        
        # dict of col sets
        d_col = {}

        # dict of box sets
        d_box = {} # key is row, val is dict of lists

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":  
                    # check for row
                    if r in d_row:
                        if val in d_row[r]:
                            return False
                        d_row[r].append(val)
                    else:
                        d_row[r] = [val]

                    # check for col
                    if c in d_col:
                        if val in d_col[c]:
                            return False
                        d_col[c].append(val)
                    else:
                        d_col[c] = [val]

                    # check for box
                    row_box = r // 3
                    col_box = c // 3
                    print(row_box, col_box)
                    relevant_list = []

                    if row_box in d_box and col_box in d_box[row_box]:
                        relevant_list = d_box[row_box][col_box]
                        if val in relevant_list: 
                            return False
                        else:
                            d_box[row_box][col_box].append(val)
                    elif row_box in d_box:
                        d_box[row_box][col_box] = [val]
                    else:
                        d_box[row_box] = {col_box: [val]}

        return True

