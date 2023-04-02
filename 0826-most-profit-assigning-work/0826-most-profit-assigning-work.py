from sortedcontainers import SortedList
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        #--------------------------------
        n = len(difficulty)
        arr = []
        #--------------------------------
        for i in zip(difficulty,profit):
            arr.append(list(i))
        #--------------------------------
        arr.sort(key = lambda x : x[0])
        #--------------------------------
        mx = -float('inf')
        for i in range(n):
            mx = max(mx,arr[i][1])
            arr[i][1] = mx
        #------------------------------------
        l = SortedList(arr,key =  lambda x : x[0])
        res = 0
        #-----------------------------------
        # print(l)
        for i in worker:
            index = l.bisect_right([i,0])
            if index==0:
                continue
            # print(index)
            res += l[index-1][1]
        #-----------------------------------
        return res