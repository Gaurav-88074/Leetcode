class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(1,len(nums)):
            if inc and nums[i]<nums[i-1]:
                inc = False
            if dec and nums[i]>nums[i-1]:
                dec = False
            
        return inc or dec