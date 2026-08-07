class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)

        idx = 0
        memo = {} # idx start: True

        def dp(start, end):

            if start in memo:
                return memo[start]

            if end == len(s) - 1:
                if s[start:end + 1] in wordDict:
                    return True
                return False
            
            if end > len(s) - 1:
                return False

            if s[start:end+1] in wordDict:
                memo[start] = dp(end + 1, end + 1) or dp(start, end+1)
            else:
                memo[start] = dp(start, end+1)

            return memo[start]


        return dp(0, 0)

