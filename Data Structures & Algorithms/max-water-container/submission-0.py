class Solution:
    def maxArea(self, heights: List[int]) -> int:
        head = 0
        tail = len(heights) - 1
        best_prod = 0
        while (head < tail):
            dist = tail-head
            print(dist)
            val1 = heights[head]
            val2 = heights[tail]
            prod = dist * min(val1, val2)
            if (prod > best_prod):
                best_prod = prod
            if val1 < val2:
                head += 1
            else:
                tail -= 1
        return best_prod
                