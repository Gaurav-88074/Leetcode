class SmallestInfiniteSet(object):

    def __init__(self):
        self.popped = set()
        self.m = 1
        self.n = set()
        self.all = True

    def popSmallest(self):
        if len(self.n)==0:
            v = self.m
            self.m+=1
            self.popped.add(v)
            return v
        else:
            v = min(self.n)
            self.popped.add(v)
            self.n.discard(v)
            return v
            
        

    def addBack(self, num) :
        if num in self.popped:
            self.n.add(num)
            self.popped.discard(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)