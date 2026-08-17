class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def jump(idx):
            print("idx: ", idx)
            if idx >= len(nums) - 1:
                return True
            if idx in memo:
                return memo[idx]
            num = nums[idx]
            if num == 0:
                return False
            else:
                can = False
                for i in range(1, num+1):
                    can = can or jump(idx + i)
            memo[idx] = can
            return memo[idx]
        
        return jump(0)