class Solution:
    def check(self, k, piles):
        # True for left, False for right
        hrs = 0
        for i in piles:
            hrs += math.ceil (i / k)
        return hrs
        

    def binSearch(self, lower, upper, piles, h):
        mid = (upper + lower) // 2 
        hrs = self.check(mid, piles)
        if upper-lower <= 1:
            if hrs <= h:
                return lower
            else:
                return upper
        if hrs <= h:
            return self.binSearch(lower, mid, piles, h)
        else:
            return self.binSearch(mid, upper, piles, h)
            

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_k = max(piles)
        return self.binSearch(1, upper_k, piles, h)
        

        