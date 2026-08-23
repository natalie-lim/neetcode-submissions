class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # let's make s the rows and p the cols (s going down p going accross)
        rows = len(s) + 1
        cols = len(p) + 1
        arr = [[None] * cols for _ in range(rows)]

        # col fill
        arr[rows-1][cols-1] = True
        for r in range(rows-1):
            arr[r][cols-1] = False

        
        def lock(r, c):
            if arr[r][c] is not None:
                return arr[r][c]
            pc = p[c] # across

            res = False

            if c + 1 < len(p) and p[c+1] == "*":
                res = lock(r, c+2) # zero occurances
                if r < len(s) and (pc == "." or pc == s[r]):
                    res = res or lock(r+1, c) # one or more occurance
            else:
                if r < len(s) and (pc == "." or pc == s[r]):
                    res = lock(r+1, c+1)
            arr[r][c] = res
            return res

        return lock(0, 0)