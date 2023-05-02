from sortedcontainers import SortedList
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        arr = [[i,c[i]] for i in c]
        l = SortedList(key = lambda x : x[1])
        # arr.sort(key = lambda x : c[x])
        # print(arr)
        for i,v in arr:
            l.add([i,v])
        
        while l and k>0:
            head = l.pop(0)
            head[1]-=1
            if head[1]>0:
                l.add(head)
            k-=1
        return len(l)