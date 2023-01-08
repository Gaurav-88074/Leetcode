class DataStream:

    def __init__(self, value: int, k: int):
        self.problem = -1
        self.call = 0
        self.value = value
        self.k=k
        self.i= 0

    def consec(self, num: int) -> bool:
        self.i+=1
        if num!=self.value:
            self.problem=self.i
        if self.i<self.k:
            return False 
        res =  (self.i - self.problem)>=self.k
        return res


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)