class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        idx = len(digits) - 1
        add = 0

        val = digits[idx]
        val += 1
        add = val // 10
        digits[idx] = val % 10
        idx -= 1
 
        while idx >= 0 and add != 0:
            val = digits[idx]
            val += add
            add = val // 10
            digits[idx] = val % 10
            idx -= 1

        if add > 0:
            digits.insert(0, add)
        
        return digits
