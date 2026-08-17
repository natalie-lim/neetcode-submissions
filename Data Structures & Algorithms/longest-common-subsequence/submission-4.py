class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        longer = text1
        shorter = text2
        if l1 != l2:
            longer = max([text1, text2], key=len)
            shorter = min([text1, text2], key=len)

        d = {} # longer c: [idx]

        for idx, c in enumerate(longer):
            if c in d:
                prev = d[c]
                prev.append(idx)
                d[c] = prev
            else:
                d[c] = [idx]
        
        memo = {}

        # iterating through shorter
        def dp(idx, prev_longer_idx):
            if idx >= len(shorter):
                return 0
            if (idx, prev_longer_idx) in memo:
                return memo[(idx, prev_longer_idx)]
            
            # include or dont include
            c = shorter[idx]

            # include (must be in d and idx must be > prev)
            if c in d:
                idxs = d[c]
                for i in idxs:
                    if i > prev_longer_idx:
                        memo[(idx, prev_longer_idx)] = 1 + dp(idx+1, i)
                        return max(dp(idx + 1, prev_longer_idx), memo[(idx, prev_longer_idx)])
                        break
                
            # don't include
            return dp(idx + 1, prev_longer_idx)
        
        return dp(0, -1)