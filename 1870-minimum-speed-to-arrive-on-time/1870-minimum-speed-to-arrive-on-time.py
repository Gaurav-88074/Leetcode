class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left = 1
        right = 10**7 + 1
        
        def computeSpeed(assumeSpeed):
            res = 0
            n = len(dist)
            for i in range(0,n-1):
                val = math.ceil(dist[i]/assumeSpeed)
                res+=val
            res+=dist[-1]/assumeSpeed
            return res
        res = -1
        while left<right:
            mid= (left+right)//2
            computedHours = computeSpeed(mid)
            # print("Assume Speed =",mid,"Computed Hours =",computedHours)
            if computedHours<=hour:
                res = mid
                right = mid
            else:
                left = mid+1
            # print(left,right,"last response")
        return res