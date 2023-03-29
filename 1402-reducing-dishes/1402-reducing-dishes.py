from collections import defaultdict, deque
from functools import cmp_to_key
from typing import List, Tuple, Optional
# from sortedcollections import OrderedSet
from collections import defaultdict, Counter
from sortedcontainers import SortedList, SortedDict,SortedSet

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res=[]
        l = SortedList(satisfaction)
        while len(l)!=0:
            i = 1
            value = 0
            for x in l:
                value += (x*i)
                i += 1
            l.remove(l[0])
            res.append(value)
        return max(max(res),0)
            
            
        