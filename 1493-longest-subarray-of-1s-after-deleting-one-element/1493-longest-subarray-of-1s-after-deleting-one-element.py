class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        pre  =0
        zero = 0
        for i,v in enumerate(nums):
            if v==0:
                zero+=1
            
            while zero>1 and pre<i:
                if nums[pre]==0:
                    zero-=1
                pre+=1
            res = max(res,i-pre)
        return res
                