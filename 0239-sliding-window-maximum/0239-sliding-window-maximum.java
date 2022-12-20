from sortedcontainers import SortedList,SortedDict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = SortedList()
        index = 0
        res = []
        for i,v in enumerate(nums):
            if i>=k:
                res.append(l[-1])
                l.discard(nums[index])
                index+=1
            l.add(v)
        res.append(l[-1])
        return res