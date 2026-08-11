class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        res = []
        start, end = newInterval
        before = []
        after = []

        for interval in intervals:
            s, e = interval 
            # if start is before this end or this end is greater than start
            if s <= end and e >= start:
                start = min(s, start)
                end = max(end, e)
            if end < s:
                after.append(interval)
            if start > e:
                before.append(interval)
        
        return before + [[start, end]] + after

            

            