from sortedcontainers import SortedList, SortedDict,SortedSet
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if len(nums)==1:
            return 0
#         dmn = defaultdict(int)
#         dmx = defaultdict(int)
        def compute(key,l):
            a = l.bisect_left(key)
            res = float('inf')
            # print(key,l)
            if a<len(l):
                res = min(res,abs(l[a] - key))
            a = l.bisect_right(key)
            if a<len(l):
                res = min(res,abs(l[a] - key))
            if a-1<len(l):
                res = min(res,abs(l[a-1] - key))
            # print(key,l,res)
            return res
        res = float('inf')
        l = SortedList()
        for i,v in enumerate(nums):
            # l.add(v)#huge mistake i did leasson for lifetime
            if i-x>=0:
                l.add(nums[i-x])
                c = compute(v,l)
                res = min(res,c)
        return res