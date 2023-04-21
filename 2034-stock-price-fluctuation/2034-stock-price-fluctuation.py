from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.l= SortedList()
        self.d = dict()
        self.current_time=0
        self.current_time_value=0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.d:
            value = self.d[timestamp]
            self.l.remove(value)
            self.d[timestamp] = price
            self.l.add(price)
        else:
            self.d[timestamp] = price
            self.l.add(price)
        if timestamp>=self.current_time:
            self.current_time  = timestamp
            self.current_time_value = price

    def current(self) -> int:
        return self.current_time_value

    def maximum(self) -> int:
        return self.l[-1]

    def minimum(self) -> int:
        return self.l[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()