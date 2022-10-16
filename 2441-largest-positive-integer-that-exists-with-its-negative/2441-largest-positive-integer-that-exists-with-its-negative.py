class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = 0
        f=0
        s = set(nums)
        for i in nums:
            if -i in s:
                f=1
                res = max(res,i)
        if f==1:return res
        return -1