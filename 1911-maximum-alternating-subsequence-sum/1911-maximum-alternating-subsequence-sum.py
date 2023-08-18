class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def compute(index,lastWasEven):
            if index==len(nums):
                return 0
            if lastWasEven :
                #why - : if last was even then this is odd
                #so we have to subtract it now
                take = -nums[index] + compute(index+1,False)
                skip = compute(index+1,lastWasEven)
                return max(take,skip)
            else:
                take = nums[index] + compute(index+1,True)
                skip = compute(index+1,lastWasEven)
                return max(take,skip)
        
        res = compute(0,False)
        # compute.cache_clear()
        return res