class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:

        if (len(self.stack) == 0):
            self.stack.append(val)
            self.minStack.append(val)
        else:
            if (self.minStack[-1] > val):
                self.stack.append(val)
                self.minStack.append(val)
            else:
                self.stack.append(val)
                self.minStack.append(self.minStack[-1])

        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return int(self.stack[-1])
        
    def getMin(self) -> int:
        return int(self.minStack[-1])