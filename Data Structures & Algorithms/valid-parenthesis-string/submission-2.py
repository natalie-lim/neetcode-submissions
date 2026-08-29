class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def explore(idx, stack):
            if idx == len(s):
                return len(stack) == 0
            if (idx, len(stack)) in memo:
                return memo[(idx, len(stack))]

            c = s[idx]

            if c == "(":
                stack.append(c)
                res = explore(idx + 1, stack)
                stack.pop()
                memo[(idx, len(stack))] = res
                return memo[(idx, len(stack))]
            elif c == ")":
                if not stack:
                    return False
                prev = stack.pop()
                res = explore(idx + 1, stack)
                stack.append(prev)
                memo[(idx, len(stack))] = res
                return memo[(idx, len(stack))]
            else:
                nothing = explore(idx + 1, stack)
                stack.append(c)
                left = explore(idx + 1, stack)
                right = False
                stack.pop()
                if stack:
                    prev = stack.pop()
                    right = explore(idx + 1, stack)
                    stack.append(prev)
                memo[(idx, len(stack))] =  (nothing or left or right)
                return memo[(idx, len(stack))]

        return explore(0, [])