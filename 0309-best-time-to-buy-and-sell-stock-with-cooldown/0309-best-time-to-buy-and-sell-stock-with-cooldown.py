class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        @lru_cache(None)
        def compute(index,buy):
            if index>=len(prices):
                return 0
            
            take = 0
            if buy==False:
                take = - prices[index] + compute(index+1,True)
            else:
                take =   prices[index] + compute(index+2,False)
            
            skip = compute(index+1,buy)
            
            return max(take,skip)
        return compute(0,False)