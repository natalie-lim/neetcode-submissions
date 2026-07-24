class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        stones = sorted(stones)
        y = stones.pop()
        x = stones.pop()
        if x == y:
            return self.lastStoneWeight(stones)
        else:
            stones.append((y-x))
            return self.lastStoneWeight(stones)
