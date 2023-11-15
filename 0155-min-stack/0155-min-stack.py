class MinStack:

    def __init__(self):
        self.stack = []
        self.minvstack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack)==1:
            self.minvstack.append(val)
        else:
            self.minvstack.append(min(self.minvstack[-1],val))
            
    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)>0:
            self.minvstack.pop()
        # else:
        #     self.minv = 
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()