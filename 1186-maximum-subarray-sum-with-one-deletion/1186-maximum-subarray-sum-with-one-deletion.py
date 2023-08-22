class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def compute(i,isRemoved):
            if i==n:
                return float('-inf')
            #--------------------------------
            takeIt = float('-inf')
            dropIt = float('-inf')
            #--------------------------------
            takeIt = nums[i] + compute(i+1,isRemoved)
            #--------------------------------
            if isRemoved==False:
                dropIt = compute(i+1,True)
            #--------------------------------
            return max(takeIt,dropIt,nums[i])
            #--------------------------------
        res = float('-inf')
        for i,v in enumerate(nums):
            res = max(res,compute(i,False))
        # if res==0:
        #     return max(nums)
        compute.cache_clear()
        return res