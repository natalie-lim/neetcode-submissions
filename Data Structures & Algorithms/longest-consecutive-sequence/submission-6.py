class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = []
        for i in nums:
            if (i-1) not in nums:
                starts.append(i)

        counter = 0
        max_counter = 0

        for i in starts:
            num = i
            while num in nums:
                counter += 1
                num = num + 1
            
            if counter > max_counter:
                max_counter = counter
            counter = 0
        
        return max_counter