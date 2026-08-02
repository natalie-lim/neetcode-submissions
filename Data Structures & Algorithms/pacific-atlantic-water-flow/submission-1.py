class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        num_rows = len(heights)
        num_cols = len(heights[0])

        def canReachPacific(r, c, prev, touched):
            if r < 0 or c < 0:
                return True
            if r >= num_rows or c >= num_cols:
                return False 
            if touched[r][c] == 1:
                return False
                
            val = heights[r][c]

            if prev < val:
                return False
            
            touched[r][c] = 1

            return (canReachPacific (r-1, c, val, touched) or 
                canReachPacific(r+1, c, val, touched) or 
                canReachPacific(r, c-1, val, touched) or 
                canReachPacific(r, c+1, val, touched))
        
        # down and right
        def canReachAtlantic(r, c, prev, touched):
            if r >= num_rows or c >= num_cols:
                return True
            if r < 0 or c < 0:
                return False
            if touched[r][c] == 1:
                return False
            
            val = heights[r][c]

            if prev < val:
                return False
            
            touched[r][c] = 1
            
            return (canReachAtlantic (r-1, c, val, touched) or 
                canReachAtlantic(r+1, c, val, touched) or 
                canReachAtlantic(r, c-1, val, touched) or 
                canReachAtlantic(r, c+1, val,touched))



        for r, row in enumerate(heights):
            for c, val in enumerate(row):
                t1 = [[0] * num_cols for _ in range(num_rows)]
                t2 = [[0] * num_cols for _ in range(num_rows)]
                if (canReachPacific(r, c, float('inf'), t1) 
                    and canReachAtlantic(r, c, float('inf'), t2)):
                    res.append([r, c])

        return res