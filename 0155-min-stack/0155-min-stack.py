class MinStack:

    def __init__(self):
        self.stack = []
        self.minv =0
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack)==1:
            self.minv = val
        else:
            self.minv = min(self.minv,val)
    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack)>0:
            self.minv = min(self.stack)
        # else:
        #     self.minv = 
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minv
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()