class MyStack:

    def __init__(self):
        self.queue1 =deque()
        
    def push(self, x: int) -> None:
        self.queue1.append(x) 
        

    def pop(self) -> int:
        i = len(self.queue1)-1
        while i>0:
            val = self.queue1.popleft()
            self.queue1.append(val)
            i-=1
            
        
        val = self.queue1.popleft()
        return val

    def top(self) -> int:
        i = len(self.queue1)
        while i>0:
            val = self.queue1.popleft()
            self.queue1.append(val)
            i-=1
        return val
        

    def empty(self) -> bool:
        return len(self.queue1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()