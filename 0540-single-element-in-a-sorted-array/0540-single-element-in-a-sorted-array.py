class Solution(object):
    def compute(self,nums,i):
        if i==len(nums):
            return 0
        return nums[i]^self.compute(nums,i+1)
    def singleNonDuplicate(self, nums):
        return self.compute(nums,0)
        