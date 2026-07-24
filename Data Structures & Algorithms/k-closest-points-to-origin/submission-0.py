class Bubble:
    def __init__(self, x, y):
        self.dist = math.sqrt(x**2 + y**2)
        self.x = x
        self.y = y
        
    def __lt__ (self, other):
        return self.dist > other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # bubbles
        for x, y in points:
            b = Bubble(x, y)
            heapq.heappush(heap, b)
            if len(heap) > k:
                heapq.heappop(heap)
        bubble = heap[0]
        arr = []
        for b in heap:
            x = b.x
            y = b.y
            arr.append([x, y])
        return arr