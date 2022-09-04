class Solution(object):
    def numberOfWays(self, s, e, k):
        dp = dict()
        def compute(s,e,k):
            if k==0 and s==e:
                # print("yes")
                return 1
            if k==0 and s!=e:
                return 0
            key = (s,k)
            if key in dp:
                return dp[key]
            # return sum([compute(s+1,e,k-1),compute(s-1,e,k-1)])
            dp[key] =  compute(s+1,e,k-1) + compute(s-1,e,k-1)
            return dp[key]
        res = compute(s,e,k)
        # print(res)
        mod = 10**9 + 7
        return res%mod
        