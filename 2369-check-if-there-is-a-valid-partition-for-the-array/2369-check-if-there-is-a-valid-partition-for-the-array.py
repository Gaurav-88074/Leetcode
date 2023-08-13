class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def op1(nums,index):
            if index+1>=len(nums) : return False
            return nums[index]==nums[index+1]
        def op2(nums,index):
            if index+2>=len(nums) : return False
            return nums[index]==nums[index+1]==nums[index+2]
        def op3(nums,index):
            if index+2>=len(nums) : return False
            return nums[index+2]-nums[index+1]==1 and nums[index+1] - nums[index]==1
        @lru_cache(None)
        def check(index):
            if index==len(nums):
                return True
            if op1(nums,index) and check(index+2):
                return True
            if op2(nums,index) and check(index+3):
                return True
                 
            if op3(nums,index) and check(index+3):
                return True
            
            return False
        def iterative():
            n = len(nums)
            dp = [False] * (n+1)
            dp[-1]=True
            for i in range(n-1,-1,-1):
                res = False
                if op1(nums,i) and dp[i+2]:
                    res|=True
                if op2(nums,i) and dp[i+3]:
                    res|=True
                if op3(nums,i) and dp[i+3]:
                    res|=True
                dp[i] = res
            # print(dp)
            return dp[0]
        
        # print(right)
        # res =check(0)
        res =iterative() 
        check.cache_clear()
        return res