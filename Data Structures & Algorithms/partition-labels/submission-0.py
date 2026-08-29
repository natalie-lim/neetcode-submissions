from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # lowk find the (start, end) of each letter, then do unions

        d = defaultdict(list) # letter: idx
    
        for i, c in enumerate(s):
            d[c].append(i)
        # heap, pop until no overlap, then return
        res = []
        heap = []

        for key, val in d.items():
            start = val[0]
            end = val[-1]
            heapq.heappush(heap, (start, end))

        start, end = heapq.heappop(heap)
        tally = 1

        while heap:
            popstart, popend = heapq.heappop(heap)
            if popstart > end:
                res.append(end-start+1)
                start, end = popstart, popend
            else:
                start = min(popstart, start)
                end = max(popend, end)
        res.append(end-start+1)
        return res