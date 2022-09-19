class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize;

    def push(self, x: int) -> None:
        if len(self.stack)<self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return -1 if len(self.stack)==0 else self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        m = min(len(self.stack),k)
        for i in range(m):
            self.stack[i]+=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)