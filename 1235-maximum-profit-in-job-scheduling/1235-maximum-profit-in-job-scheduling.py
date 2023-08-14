class Task:
    def __init__(self,a,b,c):
        self.start = a
        self.end = b
        self.reward = c
    def __str__(self) -> str:
        return f"{self.start}-{self.end}:{self.reward}"

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def binarySearch(start,end,arr,myStart):
            while start<=end:
                # print(f"we stuck for {myStart} at{start}-{end} ")
                mid = (start+end)//2
                if myStart >= arr[mid].end:
                    start = mid+1
                else:
                    end   = mid-1
            return end
        def project(arr):
            n = len(arr)
            dp = [0]*n
            arr.sort(key= lambda x : x.end)
            # print(*arr)
            dp[0] = arr[0].reward
            for i in range(1,n):
                bs = binarySearch(0,i-1,arr,arr[i].start)
                # print(f"at {i} we got {bs}")
                p=arr[i].reward
                if (bs!=-1):
                    p+= dp[bs]
                
                dp[i] = max(p,dp[i-1])
            # print(dp)
            return dp[-1]
        n = len(startTime)
        arr = []
        for i in range(n):
            arr.append(Task( startTime[i] , endTime[i],profit[i]))
        # print(*arr)
        return project(arr)