class Solution(object):
    def compute(self,n,k,index,target,dp):
        
        if(target==0 and n==0):
            # print(v)
            # dp[n][index][target] = 1
            return 1
        if n<=0 or target<0:
            # dp[n][index][target] = 0
            return 0
        if dp[n][index][target] !=-1:
            return dp[n][index][target]
        #-----------
        res =0
        for i in range(k):
            # v.append(array[i])
            # print()
            if  n-1<0 or i<0 or target-(i+1)<0:
                continue
            if dp[n-1][i][target-(i+1)]!=-1:
                res+=dp[n-1][i][target-(i+1)]
            else:
                value=self.compute(n-1,k,i,target-(i+1),dp)
                dp[n-1][i][target-(i+1)] = value
                res+=value
            # v.pop()

        return res
    def numRollsToTarget(self, n, k, target):
        if n==1:
            if k>=target:
                return 1
            else:
                return 0
        # array= [i for i in range(1,k+1)]
        dp = []
        for i in range(n+1):
            dp.append([0]*(k+1))
        for i in range(n+1):
            for j in range(k+1):
                dp[i][j] = [-1] * (target+1)
        m = 1000000000 +7
        return self.compute(n,k,0,target,dp)%m
        