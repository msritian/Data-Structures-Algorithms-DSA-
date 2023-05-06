class MinStack:
    def __init__(self):
        self.min_ele=0
        self.stack=[]
    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.min_ele=val
        elif val>=self.min_ele:
            self.stack.append(val)
        elif val<self.min_ele:
            self.stack.append(2*val-self.min_ele)
            self.min_ele=val

    def pop(self) -> None:
        if len(self.stack)==0:
            return -1
        elif self.stack[-1]>=self.min_ele:
            self.stack.pop()
        elif self.stack[-1]<self.min_ele:
            self.min_ele=2*(self.min_ele)-self.stack[-1]
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack)==0:
            return -1
        elif self.stack[-1]>=self.min_ele:
            return self.stack[-1]
        else:
            return self.min_ele

    def getMin(self) -> int:
        return self.min_ele


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()