class MyQueue:

    def __init__(self):
        self.s = []
        self.p= 0
        self.size = 0

    def push(self, x: int) -> None:
        self.size+=1
        self.s.append(x)

    def pop(self) -> int:
        value = self.s[self.p]
        self.p+=1
        # self.size-=1
        return value

    def peek(self) -> int:
        value = self.s[self.p]
        return value

    def empty(self) -> bool:
        return self.p==self.size


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()