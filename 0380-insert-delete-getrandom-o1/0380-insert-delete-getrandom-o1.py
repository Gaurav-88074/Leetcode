class RandomizedSet:

    def __init__(self):
        self.l = []
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.l.append(val)
            self.s.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.discard(val)
            return True
        return False

    def getRandom(self) -> int:
        v = random.choice(self.l)
        while v not in self.s:
            v=random.choice(self.l)
        return v


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()