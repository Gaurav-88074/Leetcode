class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if len(nums)<3:return 0
        dp = {}
        def compute(index,size):
            if index==len(nums):
                return 0
            key = (index,size)
            if key in dp : return dp[key]
            
            if nums[index-1]-nums[index-2]==nums[index] - nums[index-1]:
                dp[key]= 1 + size + compute(index+1,size+1)
            else:
                dp[key]= compute(index+1,0) 
            return dp[key]
            
        return compute(2,0)
        