class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap of size k with (freq, char) tuples
        heap = [] # min heap
        d = {} # val: freq

        for n in nums:
            if n in d:
                val = d[n]
                d[n] = val + 1
            else:
                d[n] = 1
        
        for val, freq in d.items():
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            freq, val = heapq.heappop(heap)
            res.append(val)

        return res
            