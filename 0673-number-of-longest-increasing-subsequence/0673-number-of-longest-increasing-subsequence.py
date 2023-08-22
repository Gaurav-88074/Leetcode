class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        count = [None]*len(nums)
        for i in range(len(nums)):
            count[i]=defaultdict(int)
            count[i][1] = 1
        
        dp =[1]*len(nums)
        mx = 0
        res = 0
        for i,v in enumerate(nums):
            for j in range(0,i):
                if nums[j]<v:
                    x = dp[j] + 1
                    if x>=dp[i]:
                        dp[i] = max(dp[i],x)
                        count[i][x] += count[j][x-1]
        mx = max(dp)
        if mx==1:
            return len(nums)
        # print(dp,mx)
        # print(count)
        for i,v in enumerate(dp):
            if v==mx:
                res += count[i][mx]
        return res