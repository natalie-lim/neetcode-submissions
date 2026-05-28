class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #pair [temp, idx]
        
        for i, t in enumerate(temperatures):
            print("loop: ", i, t)
            while stack and t > stack[-1][0]:
                print("stack :", stack)
                print("res: ", res)
                # while stack has smth and temp is greater than the top of the stack
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
                print("stack after: ", stack)
                print("res after: ", res)
            stack.append((t, i))
        
        return res
