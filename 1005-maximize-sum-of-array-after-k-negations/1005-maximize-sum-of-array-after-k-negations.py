from sortedcontainers import SortedList
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #[index,value]
        p = SortedList(key = lambda x :  x)
        n = SortedList(key = lambda x :  x)
        for i,v in enumerate(nums):
            if v>=0:
                p.add(v)
            else:
                n.add(v)

        while len(n)>0 and k>0 and n[0]<0:
            value = n[0]
            n.remove(value)
            n.add(-value)
            k-=1
        for i in n:
            p.add(i)
        #----------------------
        if k>0:
            value = p[0]
            p.remove(value)
            if k%2==0:
                p.add(value)
            else:
                p.add(-value)
        # print(p)
        return sum(p)