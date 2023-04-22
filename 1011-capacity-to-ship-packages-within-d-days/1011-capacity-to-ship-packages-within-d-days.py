class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        
        def compute(capacity):
            day = 0
            w = 0
            for i in weights:
                if w+i > capacity:
                    day+=1
                    w = i
                else:
                    w+=i
            return 1 + day
        low = max(weights)
        high= sum(weights)
        # print(compute(15))
        while low<high:
            mid = (low+high)//2
            if compute(mid)<=days:
                high=mid
            else:
                low = mid+1
        return low