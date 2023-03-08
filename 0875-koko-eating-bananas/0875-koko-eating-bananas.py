class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high= max(piles)
        
        def compute(piles,val):
            res = 0
            for i in piles:
                res+= math.ceil(i/val)
            return res
        # if len(piles)==1:
        #     return math.ceil(piles[0]/h)
        while low<high:
            mid = (low+high)//2
            
            v = compute(piles,mid)
            # print("At ",mid,"computed value",v,"[Time Consumed]")
            if v<=h:
                high = mid
            else:
                low = mid+1
        return high