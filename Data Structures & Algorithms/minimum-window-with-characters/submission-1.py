class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}

        for c in t:
            if c in t_counts:
                prev = t_counts[c]
                t_counts[c] = prev + 1
            else:
                t_counts[c] = 1

        reg_counts = t_counts.copy()

        d = {} # a, [1, 4, 9]
        window = ""

        for idx, val in enumerate(s):
            print("original dict: ", d)
            print("t counts: ", t_counts)
            print("idx: ", idx, ", val: ", val)
            if val in t:
                # decrease count
                if val in t_counts:
                    prev = t_counts[val]
                    prev -= 1
                    if prev > 0:
                        t_counts[val] = prev
                    else:
                        del t_counts[val]
                # append to list
                l = d[val] if val in d else []
                og_count = reg_counts[val]
                l.append(idx)
                print("new dict: ", d)
                l = l[-og_count:]
                d[val] = l 
                if len(t_counts) <= 0: # check other d is empty, make prev d have list of whatever
                    arr = []
                    for c, l in d.items():
                        arr.extend(l)

                    minimum = min(arr)
                    maximum = max(arr) + 1
                    diff = maximum - minimum
                    print(diff)
                    if diff < len(window) or window=="":
                        window = s[minimum:maximum]
            
        return window