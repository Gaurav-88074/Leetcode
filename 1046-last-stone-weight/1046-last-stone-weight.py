from sortedcontainers import SortedList
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l=SortedList(stones)
        while len(l)>1:
            a=l.pop()
            b=l.pop()
            if a!=b:
                l.add(a-b)
        if l:
            return l[0]
        return 0
    
 
            