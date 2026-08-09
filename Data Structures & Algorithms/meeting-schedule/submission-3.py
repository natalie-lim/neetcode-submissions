"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        start = float('inf')
        end = float('-inf')

        for i in intervals:
            s = i.start
            e = i.end
            if (s >= start and s < end) or (e >= start and s < start):
                print(s, e)
                return False
            if s < start:
                start = s
            if e > end:
                end = e
        
        return True