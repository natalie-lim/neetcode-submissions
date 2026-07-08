class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        pt1 = 0
        pt2 = 1
        d = {}
        d[s[0]] = 1
        window = 1

        while pt2 < len(s) and pt1 < pt2:
            c = s[pt2]

            w = pt2 - pt1 + 1
            
            if c in d:
                val = d[c]
                d[c] = (val + 1)
            else:
                d[c] = 1
            m = max(d.values())
            allowance = w - m
            if allowance > k:
                print("allowance: ", allowance)

                val = d[s[pt1]]
                if val - 1 == 0:
                    del d[s[pt1]]
                else:
                    d[s[pt1]] = val - 1
                pt1 += 1
            else:
                if w > window:
                    window = w
            
            pt2 += 1

        w = pt2 - pt1

        return max(w, window)