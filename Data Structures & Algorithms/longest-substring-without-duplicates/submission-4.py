class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        sub = ""
        most = 0
        for i, c in enumerate(s):
            if c in sub:
                l = len(sub)
                if l > most:
                    most = l
                start = sub.find(c)
                sub = sub[(start + 1):]
            sub = sub + c
        
        l = len(sub)
        if l > most:
            most = l
            
        print(sub)
        return most
