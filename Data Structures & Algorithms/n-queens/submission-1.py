class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # no same rows, no same cols, no diags

        all_res = []

        def solve(col_set, diag1, diag2, row, res):
            if row >= n:
                to_app = res.copy()
                all_res.append(to_app)

            curr_row = "." * n

            for c in range(n):
                if c not in col_set and row - c not in diag1 and row + c not in diag2:

                    s = curr_row[:c] + "Q" + curr_row[c + 1:]
                    copyset = col_set.copy()
                    copyset.add(c)
                    copydiag1 = diag1.copy()
                    copydiag1.add(row - c)
                    copydiag2 = diag2.copy()
                    copydiag2.add(row + c)
                    res.append(s)

                    solve(copyset, copydiag1, copydiag2, row + 1, res)

                    res.pop()
        
        solve(set(), set(), set(), 0, [])
        return all_res
