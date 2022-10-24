class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num>0:
            self.arr.append(self.arr[-1]*num)
        else:
            self.arr=[1]

    def getProduct(self, k: int) -> int:
        arr = self.arr
        # print(arr)
        if len(arr)<k+1:
            return 0
        else:
            return arr[-1]//arr[-(k+1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)