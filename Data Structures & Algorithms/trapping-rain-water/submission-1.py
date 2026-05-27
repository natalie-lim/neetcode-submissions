class Solution:
    def trap(self, height: List[int]) -> int:
        
        tallest_left = []
        tallest_right = []

        tallest = height[0]
        tallest_left.append(0)

        for idx, val in enumerate(height[1:]):
            tallest_left.append(tallest)
            if val > tallest:
                tallest = val

        tallest = height[-1]
        tallest_right.insert(0, 0)

        for val in (reversed(height[:-1])):
            tallest_right.insert(0, tallest)
            if val > tallest:
                tallest=val

        
        print(tallest_left)
        print(tallest_right)

        sum = 0
        for i, val in enumerate(height):
            h = min(tallest_left[i], tallest_right[i])
            to_add = max(h - val, 0)
            sum += (to_add)


        return sum