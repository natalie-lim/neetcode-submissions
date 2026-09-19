class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1]) # sort by end times
        
        count = 0
        end = float('-inf')

        for s, e in intervals:
            if s >= end:
                end = e
            else:
                count += 1

        return count