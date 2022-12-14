class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        s = set(forbidden)
        # sys.setrecursionlimit(10**5)
        # @lru_cache(None)
        dp = [[-1,-1] for i in range(6001)]
        def compute(position,back):
            
            if position==x:
                return 0
            
            if position<0:
                return float('inf')
            if position>6000:
                return float('inf')
            if back>=2:
                return float('inf')
            if position in s:
                return float('inf')
            
            if dp[position][back]!=-1:
                return dp[position][back]
            
            right = 1 + compute(position + a,0)
            dp[position][back] = right
            if not back:
                right =  min(right,1 + compute(position - b,back + 1))
            dp[position][back] = right
            return right
        # left = compute(0,0)
        # right= compute(0,0)
        # print(left,right)
        # res  = min(left,right)
        res = compute(0,0)
        return -1 if res == float('inf') else res