class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_pt = 0
        col_pt = -1
        l = []
        max_col = len(matrix[0]) - 1
        max_row = len(matrix) - 1
        arr_size = len(matrix[0]) * len(matrix)
        min_col = 0
        min_row = 1
        went_up = True

        while col_pt <= max_col and went_up and len(l) < arr_size:
            # go right
            while col_pt < max_col:
                col_pt += 1
                l.append(matrix[row_pt][col_pt])       
            max_col -= 1

            # go down
            went_down = False
            while row_pt < max_row:
                went_down = True
                row_pt += 1
                l.append(matrix[row_pt][col_pt])
            max_row -= 1

            # go left
            went_left = False
            while col_pt > min_col and went_down:
                went_left = True
                col_pt -= 1
                l.append(matrix[row_pt][col_pt])
            min_col += 1

            # go up:
            went_up = False
            while row_pt > min_row and went_left:
                went_up = True
                row_pt -= 1
                l.append(matrix[row_pt][col_pt])
            min_row += 1

        return l