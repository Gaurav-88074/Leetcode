class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(None)
        def compute(i,isRemoved):
            if i==n:
                return 0
            #--------------------------------
            takeIt = float('-inf')
            dropIt = float('-inf')
            skipIt = float('-inf')
            #--------------------------------
            takeIt = nums[i] + compute(i+1,isRemoved)
            #--------------------------------
            if isRemoved==False:
                dropIt = compute(i+1,True)
            #--------------------------------
            # skipIt = compute(i+1,isRemoved)
            #--------------------------------
            return max(takeIt,dropIt,skipIt,nums[i])
            #--------------------------------
        res = float('-inf')
        for i,v in enumerate(nums):
            res = max(res,compute(i,False))
        if res==0:
            return max(nums)
        return res