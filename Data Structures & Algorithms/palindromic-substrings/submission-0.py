class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        def expand(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l-= 1
                r += 1

            return count

        total = 0
        for i in range(len(s)):
            total += (expand(i, i + 1) + expand(i, i))
        
        return total


        