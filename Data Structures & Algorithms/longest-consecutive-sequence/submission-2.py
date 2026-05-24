class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in nums:
            count = 1
            if (i-1) not in nums:
                n = i + 1
                while n in nums:
                    n = n + 1
                    count += 1
            if count > longest:
                longest = count

        return longest