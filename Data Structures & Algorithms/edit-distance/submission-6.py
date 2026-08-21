class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == len(word2) == 0:
            return 0
        elif len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        memo = {}

        def whatever(idx1, idx2):
            if idx1 >= len(word1):
                return float('inf')
            if idx2 >= len(word2):
                return float('inf')
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            c1 = word1[idx1]
            c2 = word2[idx2]


            if idx1 == len(word1) - 1 and idx2 == len(word2) - 1 and c1 == c2:
                return 0
            
            # delete last letter(s)
            if idx2 == len(word2) - 1 and c1 == c2:
                return (len(word1) - idx1 - 1)
            
            # insert last letter(s)
            if idx1 == len(word1) - 1 and c1 == c2:
                return (len(word2) - idx2 - 1)
            
            # replace last letter
            if idx1 == len(word1) - 1 and idx2 == len(word2) - 1:
                return 1


            if c1 == c2:
                return whatever(idx1+1, idx2+1)
            
            insert = 1 + whatever(idx1, idx2+1)
            delete = 1 + whatever(idx1+1, idx2)
            replace = 1 + whatever(idx1+1, idx2+1)

            memo[(idx1, idx2)] = min(insert, delete, replace)
            return memo[(idx1, idx2)]
        
        return whatever(0, 0)

            