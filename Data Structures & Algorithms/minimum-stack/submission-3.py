class MinStack:

    def __init__(self):
        self.stack = []
        minVal = 0

    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
             self.stack.append(val - self.minVal)
             if (val < self.minVal):
                self.minVal = val       

    def pop(self) -> None:
        
        topVal = self.stack.pop()

        if (topVal < 0):
            self.minVal =  self.minVal - topVal

    def top(self) -> int:
        if (self.stack[-1] < 0):
            return (self.minVal)
        else:
            return (self.minVal + self.stack[-1])
        
    def getMin(self) -> int:
        return self.minVal