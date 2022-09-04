class Solution:
    def numberOfWays(self, s: int, e: int, k: int) -> int:
        # res = 0
        @lru_cache(None)
        def compute(s,e,k):
            if k==0 and s==e:
                # print("yes")
                return 1
            if k==0 and s!=e:
                return 0
            
            # return sum([compute(s+1,e,k-1),compute(s-1,e,k-1)])
            return compute(s+1,e,k-1) + compute(s-1,e,k-1)
        res = compute(s,e,k)
        # print(res)
        mod = 10**9 + 7
        return res%mod
                