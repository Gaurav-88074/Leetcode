class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def computeTrips(time,val):
            res  =0
            for i in time:
                res+=(val//i)
            return res
        
        low = min(time)
        high= max(time)*totalTrips
        res = 10**7
        while low<high:
            mid = (low+high)//2
            
            v = computeTrips(time,mid)
            # print("we got",v ,"at",mid)
            # if v>=totalTrips:
            #     res = min(mid,res)
                
            if v>=totalTrips:
                high = mid
            else:
                low = mid+1
        # print(low,high)
        return low