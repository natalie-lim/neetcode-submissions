class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        pt1 = 0
        pt2 = n-1
        d = {} # index, col

        # switch
        while pt1 < pt2:
            top_row = matrix[pt1]
            bottom_row = matrix[pt2]
            matrix[pt1] = bottom_row
            matrix[pt2] = top_row 
            d[pt1] = bottom_row
            d[pt2] = top_row
            pt1 += 1
            pt2 -= 1

        been = set()

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if (r, c) not in been:
                    to_switch = matrix[c][r]
                    matrix[r][c] = to_switch
                    matrix[c][r] = val
                    been.add((r, c))
                    been.add((c, r))
        
                
        

