"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        arr = []
        for i in intervals:
            arr.append((i.start, i.end))
        arr.sort()

        if len(intervals) == 0:
            return 0
        heap = [] # earliest end (end, start)
        heapq.heappush(heap, float('inf'))
        tally = 0
        
        for interval in arr:
            start, end = interval
            e = heapq.heappop(heap) # smallest end
            if start < e:
                # can not overlap with either one, so we flip the global
                heapq.heappush(heap, end)
                heapq.heappush(heap, e)
                tally += 1
            # if not overlapping, widen the bounds
            else:
                heapq.heappush(heap, max(end, e))

        return tally
