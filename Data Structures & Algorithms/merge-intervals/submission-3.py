class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [] # [start, end]

        for interval in intervals:
            start, end = interval
            # prev start will always be less
            if res:
                print(res[-1])
                rs, re = res[-1]
                if not (start > re):
                    res.pop()
                    res.append([min(rs, start), max(re, end)])
                else:
                    res.append([start, end])
            else:
                res.append([start, end])

        return res