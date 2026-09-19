class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1):
            heapq.heappush(heap, (-nums[i], i))

        left = 0
        right = k - 1
        res = []

        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            top, idx = None, -1
            while idx < left:
                top, idx = heapq.heappop(heap)
            res.append(-top)
            heapq.heappush(heap, (top, idx))
            left += 1
            right += 1

        return res