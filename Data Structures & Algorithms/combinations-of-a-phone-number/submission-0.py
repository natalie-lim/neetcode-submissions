class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(i, subset):
            if i >= len(digits):
                res.append(subset)
                return
            digit = digits[i]
            for l in d[digit]:
                subset += l
                backtrack (i + 1, subset)
                subset = subset[:-1]
        if digits == "":
            return []
        backtrack(0, "")
        return res
