class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")

        n = ""
        for i in s:
            if i.isalnum():
                n += i
        s = n
        pt1 = 0
        pt2 = len(s) - 1

        while (pt1 <= pt2):
            if s[pt1] != s[pt2]:
                return False
            pt1 += 1
            pt2 -= 1
        
        return True
