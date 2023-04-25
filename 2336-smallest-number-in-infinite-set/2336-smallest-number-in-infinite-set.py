from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.st = SortedSet([i for i in range(1,1001)])

    def popSmallest(self) -> int:
        return self.st.pop(0)
            
        

    def addBack(self, num: int) -> None:
        self.st.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)