from sortedcontainers import SortedList , SortedDict
class Solution: 
    def maximumProduct(self, nums: List[int], k: int) -> int:
        l = SortedList(nums)
        res=1
        mod = (10**9 + 7)
        while k>0:
            v=l[0]
            l.discard(v)
            v+=1
            l.add(v)
            k-=1
        for i in l:
            res*=i
            res%=mod
        return res%mod
        