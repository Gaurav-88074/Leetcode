class Solution(object):
    def maxProfit(self, k, prices):
        #state
        #sell 0
        #buy  1
        # @lru_cache(None)
        dp = {}
        def compute(k,index,state):
            if index==len(prices): return 0
            
            if k==0 : return 0
            
            key = (k,index,state)
            
            if key in dp : return dp[key]
            
            buyValue = 0
            sellValue= 0
            skip = 0
            
            if state==1:
                # print("buying at index",index,"value",prices[index])
                buyValue = -prices[index] + compute(k,index+1,1-state)
            else:
                # print("selling at index",index)
                sellValue = prices[index] + compute(k-1,index+1,1-state)
            
            skip = compute(k,index+1,state)
            
            res = max(buyValue,sellValue,skip)
            dp[key] = res
            return res
        return compute(k,0,1)
        