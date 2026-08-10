class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = {} # [start, end]

        for interval in intervals:
            start, end = interval
            # prev start will always be less
            merged = False
            for rs, re in res.items():
                if start <= re:
                    res[rs] = max(end, re)
                    merged = True
            if not res or not merged:
                res[start] = end

        arr = []
        for start, end in res.items():
            arr.append([start, end])

        return arr