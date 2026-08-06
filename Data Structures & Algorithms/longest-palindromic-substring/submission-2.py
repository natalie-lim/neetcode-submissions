class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        memo = {} # idx: palindrome starting there 

        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        longest = ""

        def pal(pt1, pt2, val):
            nonlocal longest
            c1 = s[pt1]
            c2 = s[pt2]
            while pt1 >= 0 and pt2 < len(s) and c1 == c2:
                val = (c1 + val + c2)
                pt1 -= 1
                pt2 += 1
                if pt1 >= 0 and pt2 < len(s):
                    c1 = s[pt1]
                    c2 = s[pt2]

            if len(val) > len(longest):
                longest = val

        for idx, val in enumerate(s):
            pt1 = idx-1
            pt2 = idx+1

            starter = ""

            if idx > 0 and idx < len(s) - 1:
                if s[pt1] == val and s[pt2] != val:
                    pt2 -= 1
                    pal(pt1, pt2, "")
                elif s[pt2] == val and s[pt1] != val:
                    pt1 += 1
                    pal(pt1, pt2, "")
                elif s[pt2] == val and s[pt1] == val:
                    pal(pt1, pt2, val)
                    pal(pt1 + 1, pt2, "")
                    pal(pt1, pt2-1, "")
                else:
                    pal(pt1, pt2, val)

                

        return longest
