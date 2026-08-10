class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for i, c in enumerate(s):
            if c in d:
                other_half = d[c]
                if not stack:
                    return False
                popped = stack.pop()
                if popped != other_half:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        return True