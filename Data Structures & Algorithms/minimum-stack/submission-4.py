class MinStack:

    def __init__(self):
        self.stack = []
        #lists of val, min_val at the time
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        if val < self.min_val:
            self.min_val = val
        self.stack.append(val)
        self.stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        temp = self.stack.pop()
        if len(self.stack) > 0: 
            self.min_val = self.stack[-1]
        else:
            self.min_val = float('inf')
        return temp
        

    def top(self) -> int:
        return self.stack[-2]
        

    def getMin(self) -> int:
        return self.min_val
        
