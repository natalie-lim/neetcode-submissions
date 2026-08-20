class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # iterate through matrix, check if u can increase in a direction (if not, store 1)
        # use a helper func to explore, dont need empty explore arr cuz strictly inc
        # 2d memo storing max path from the start
        # start w a reverse pq: (-val, r, c)
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        pq = []
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                heapq.heappush(pq, (-val, r, c))

        storage = [[0] * num_cols for _ in range(num_rows)]
        res = -1

        while pq:
            neg, r, c = heapq.heappop(pq)
            val = -neg
            top = storage[r-1][c] if r-1 >= 0 else 0
            top_val = matrix[r-1][c] if r-1 >= 0 else -1
            bottom = storage[r+1][c] if r + 1 < num_rows else 0
            bottom_val = matrix[r+1][c] if r + 1 < num_rows else -1
            left = storage[r][c-1] if c-1 >= 0 else 0
            left_val = matrix[r][c-1] if c-1 >= 0 else -1
            right = storage[r][c+1] if c+1 < num_cols else 0
            right_val = matrix[r][c+1] if c+1 < num_cols else -1

            temp = [top, bottom, left, right]
            prevs = [top_val, bottom_val, left_val, right_val]
            include = [0]

            for i in range(len(temp)):
                if prevs[i] != val:
                    include.append(temp[i])

            m = max(include) + 1
            storage[r][c] = m
            res = max(res, m)


        return res