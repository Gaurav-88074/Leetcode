class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        obj = {
            "price" : price,
            "value" : 1
        }
        # v = 0
        while len(self.stack)!=0 and self.stack[-1]["price"]<=price:
            last = self.stack.pop()
            obj["value"]+=last["value"]
        self.stack.append(obj)
        return obj["value"]
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)