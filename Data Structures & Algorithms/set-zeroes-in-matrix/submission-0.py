class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # go through each row and store the zero cols, have an extra arr to track the changed cols?
        # 0 1 0 1
        # 1 1 1 1
        cols = set()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    cols.add(c)

        for r, row in enumerate(matrix):
            zero_row = False
            for c, val in enumerate(row):
                if val == 0:
                    zero_row = True
                if c in cols:
                    matrix[r][c] = 0
            if zero_row:
                matrix[r] = [0] * len(matrix[0])