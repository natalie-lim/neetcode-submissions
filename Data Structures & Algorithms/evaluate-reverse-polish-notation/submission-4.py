class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        d = {
            "+": lambda a, b: int(a + b),
            "-": lambda a, b:  a-b,
            "*": lambda a, b: a*b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        for i in tokens:
            try:
                num = int(i)
                stack.append(num)
            except:
                sec = stack.pop()
                first = stack.pop()
                new_num = d[i](first,sec)
                stack.append(new_num)
        
        return stack[0]
