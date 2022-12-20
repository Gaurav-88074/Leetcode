from sortedcontainers import SortedList,SortedDict
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        l = SortedList()
        index = 0
        res = []
        for i,v in enumerate(nums):
            if i>=k:
                if (k&1)==1:
                    res.append(l[k//2])
                else:
                    value = l[k//2] + l[(k//2)-1]
                    res.append(value/2)
                l.discard(nums[index])
                index+=1
            l.add(v)
        if (k&1)==1:
            res.append(l[k//2])
        else:
            value = l[k//2] + l[(k//2)-1]
            res.append(value/2)
        return res