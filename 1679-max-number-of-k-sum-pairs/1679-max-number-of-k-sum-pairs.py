from sortedcontainers import SortedList
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=SortedList()
        res = 0
        for i in nums:
            if i in l:
                res+=1
                l.remove(i)
            else:
                l.add(k-i)
        return res