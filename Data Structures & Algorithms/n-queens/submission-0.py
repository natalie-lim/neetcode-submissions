class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # current_pos is a list of coords (tuples)
        # cur
        res = []
        subset = []

        # claude hint: track 3 sets, cols used, 2 diagonals
        def backtrack(r, cols_used, add_diag, sub_diag):
            if r == n:
                res.append(subset.copy())
                return

            valid_c = []
            for c in range(n):
                if (c not in cols_used
                    and (r + c) not in add_diag 
                    and (r-c) not in sub_diag):

                    valid_c.append(c)
            
            for c in valid_c:
                s = ""
                for i in range(n):
                    if i == c:
                        s += "Q"
                    else:
                        s += "."
                subset.append(s)
                cols_used.add(c)
                add_diag.add(r+c)
                sub_diag.add(r-c)
                backtrack(r + 1, cols_used, add_diag, sub_diag)
                subset.pop()
                cols_used.remove(c)
                add_diag.remove(r+c)
                sub_diag.remove(r-c)

        backtrack(0, set(), set(), set())
        return res