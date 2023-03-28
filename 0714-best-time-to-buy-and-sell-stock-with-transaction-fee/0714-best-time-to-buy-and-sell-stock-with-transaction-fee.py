class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        @lru_cache(None)
        def compute(i,buyState):
            if i==len(prices):
                return 0
            
            take = 0
            skip = 0
            
            #most important logic
            #only people like me can understand this
            if buyState==False:
                take = -prices[i] - fee + compute(i+1,True)
            else:
                take =  prices[i] + compute(i+1,False)
            
            skip = compute(i+1,buyState)
            
            return max(take,skip)
        return compute(0,False)
            