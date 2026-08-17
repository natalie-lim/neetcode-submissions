class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        d = {} # query, [indexes]

        for idx, q in enumerate(queries):
            if q in d:
                prev = d[q]
                prev.append(idx)
                d[q] = prev
            else:
                d[q] = [idx]

        queries.sort()

        heap = [] # (size, start, end)
        arr = []
        pointer = 0

        for q in queries: # in means that start <= q <= end
            while heap and heap[0][2] < q:  # heap[0] = (size, start, end); end < q means stale
                heapq.heappop(heap)
            while pointer < len(intervals):
                start, end = intervals[pointer]
                pointer += 1
                if end < q:
                    continue
                if start <= q <= end:
                    heapq.heappush(heap, ((end-start+1), start, end))
                if q < start:
                    pointer -= 1
                    break

            if heap:
                size, start, end = heapq.heappop(heap)
                arr.append((size, q))
                heapq.heappush(heap, (size, start, end))
            else:
                arr.append((-1, q))

        res = [-1] * len(queries)
        for a in arr:
            size, q = a
            indexes = d[q]
            idx = indexes.pop()
            d[q] = indexes
            res[idx] = size
        return res
        