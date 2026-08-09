class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {} # char: idx
        max_window = 0
        window = 0

        for i, c in enumerate(s):
            if c in d:
                max_window = max(window, max_window)
                window = min(window, i - d[c] - 1)
                d[c] = i
            else:
                d[c] = i
            window += 1

        return max(window, max_window)