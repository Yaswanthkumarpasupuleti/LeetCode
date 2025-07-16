class MinStack:
    def __init__(self):
        self.stack = []
        self.top1 = -1
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top1 = self.top1 + 1

    def pop(self) -> None:
        self.stack.pop()
        self.top1 = self.top1 - 1
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self) -> int:
        self.minEle = (2**31)-1
        if self.stack:
            for i in range(self.top1,-1,-1):
                if self.stack[i] < self.minEle:
                    self.minEle = self.stack[i]
            return self.minEle
        else:
            return None

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()