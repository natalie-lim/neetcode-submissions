class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pt1 = 0
        pt2 = 0
        sub = ""
        longest = 0
        idx = 0
        while pt2 < len(s):
            print("loop: ", idx, "char: ", s[pt2])
            idx += 1
            l = pt2 - pt1
            if l > longest:
                longest = l
            c = s[pt2]
            if c in sub:
                pt1 += 1
            else:
                pt2 += 1
            sub = s[pt1:pt2]
            print(sub)

        return max(longest, pt2 - pt1)
        