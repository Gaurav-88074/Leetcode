from sortedcontainers import SortedList
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = SortedList(nums)

    def add(self, val: int) -> int:
        self.l.add(val)
        return self.l[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)