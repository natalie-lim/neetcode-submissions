class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {} # (i, j, k) : answer
        def interleave(i, j, k):
            if k >= len(s3):
                return True
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            first = False
            second = False
            if i < len(s1) and s3[k] == s1[i]:
                first = interleave(i+1, j, k+1)
            if j < len(s2) and s3[k] == s2[j]:
                second = interleave(i, j+1, k+1)

            memo[(i, j, k)] = first or second
            return memo[(i, j, k)]

        return interleave(0, 0, 0)