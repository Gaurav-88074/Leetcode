class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i]=0
                nums[i+1]*=2
                i+=2
            else:
                i+=1
        res = []
        z=0
        for i in nums:
            if i>0:
                res.append(i)
            else:
                z+=1
        for i in range(z):
            res.append(0)
        return res