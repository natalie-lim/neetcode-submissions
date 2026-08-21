class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} # (idx, sub): val
        
        def find(idx, sub_idx):
            if idx >= len(s) or sub_idx >= len(t):
                return 0
            c1 = s[idx]
            c2 = t[sub_idx]
            to_add = 0
            if c1 == c2 and sub_idx == len(t) - 1:
                print("really?")
                to_add = 1
            if (idx, sub_idx) in memo:
                return memo[(idx, sub_idx)]
            
            # yay match
            first = 0
            if c1 == c2:
                first = find(idx+1, sub_idx+1)
            second = find(idx+1, sub_idx)
            
            memo[(idx, sub_idx)] = first + second + to_add
            return memo[(idx, sub_idx)]
        
        ans = find(0, 0)
        print(memo)
        return ans

