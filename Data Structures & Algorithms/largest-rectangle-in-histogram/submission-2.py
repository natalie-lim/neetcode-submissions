class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        stack = []
        stack.append((0, heights[0]))
        heights.append(0)

        max_area = 0

        for i, h in enumerate(heights[1:]):
            idx = i + 1
            
            if h > max_area:
                max_area = h
            
            if len(stack) >= 1:
                _, peek = stack[-1]
                if peek >= h:
                    prev_idx = 0
                    while len(stack) >= 1 and peek >= h:
                        prev_idx, prev_height = stack.pop()
                        area = (idx - prev_idx) * prev_height
                        if (area > max_area):
                            max_area = area
                        if len(stack) >= 1:
                            _, peek = stack[-1]
                    idx = prev_idx
                

            stack.append((idx, h))

        return max_area
        
            
