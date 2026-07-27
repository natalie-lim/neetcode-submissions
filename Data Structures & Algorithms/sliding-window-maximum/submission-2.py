# python
# flip = lambda t: t[::-1]

# # example
# pairs = [(1, 2), (3, 4), (5, 6)]
# flipped = list(map(flip, pairs))

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        heap = []
        for idx, n in enumerate(nums):
            limit = idx - k + 1
            heapq.heappush(heap, (-n, idx))
            val, i = heapq.heappop(heap)
            val = -val
            while i < limit and limit >= 0:
                val, i = heapq.heappop(heap)
                val = -val
            heapq.heappush(heap, (-val, i))
            if limit >= 0:
                arr.append(val)
        return arr
