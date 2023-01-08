from sortedcontainers import SortedList, SortedDict
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        l = SortedList(nums)
        res = 0
        for i in range(k):
            val = l[-1]
            l.remove(val)
            res+=val
            val = math.ceil(val/3)
            l.add(val)
        return res