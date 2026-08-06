class Solution:
    def longestPalindrome(self, s: str) -> str:
        # solved earlier but need a faster solution

        if not s:
            return ""

        start, end = 0, 0 # best pal found 

        def expand(l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1, r-1

        ll, lr = 0, 0
        for i in range(len(s)):
            l, r = expand(i, i + 1)
            if r-l > lr - ll:
                ll = l
                lr = r
            l, r = expand(i, i)
            if r-l > lr-ll:
                ll = l
                lr = r
            
        return s[ll:lr+1]
