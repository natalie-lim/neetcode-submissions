class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in reversed(matrix):
            if target >= r[0]:
                for c in r:
                    print(c)
                    if c == target:
                        return True
        return False