from sortedcontainers import SortedList, SortedDict,SortedSet
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        res = SortedList(key = lambda x : x[0]+x[1])
        # res = []
        for i in nums1:
            for j in nums2:
                s = i+j
                if len(res)==0 or len(res)<k:
                    res.add([i,j])
                else:
                    if s< sum(res[-1]):
                        res.pop()
                        res.add([i,j])
                    elif s>sum(res[-1]):
                        break
        return res[ : k]
        