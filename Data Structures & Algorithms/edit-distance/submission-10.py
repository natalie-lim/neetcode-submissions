class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        memo = {}

        def recurse(pt1, pt2):
            if pt1 >= len(word1) or pt2 >= len(word2):
                return abs((pt1 - len(word1)) + (pt2 - len(word2)))

            val1 = word1[pt1]
            val2 = word2[pt2]

            if (pt1, pt2) in memo:
                pass
            elif val1 == val2:
                memo[(pt1, pt2)] = recurse(pt1 + 1, pt2 + 1)
            else:
                # insert: move pt2
                insert = 1 + recurse(pt1, pt2 + 1)
                # delete: move pt1
                delete = 1 + recurse(pt1 + 1, pt2)
                # replace
                replace = 1 + recurse(pt1 + 1, pt2 + 1)
                memo[(pt1, pt2)] = min(insert, delete, replace)

            return memo[(pt1, pt2)]
        
        return recurse(0, 0)