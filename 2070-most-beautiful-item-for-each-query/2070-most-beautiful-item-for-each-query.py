from sortedcontainers import SortedList
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        #--------------------------------
        n = len(items)
        arr = items
        arr.sort(key = lambda x : x[0])
        #--------------------------------
        mx = -float('inf')
        for i in range(n):
            mx = max(mx,arr[i][1])
            arr[i][1] = mx
        #------------------------------------
        l = SortedList(arr,key =  lambda x : x[0])
        res = []
        #-----------------------------------
        # print(l)
        for i in queries:
            index = l.bisect_right([i,0])
            if index==0:
                res.append(0)
                continue
            else:
                res.append(l[index-1][1])
            # print(index)

        #-----------------------------------
        return res