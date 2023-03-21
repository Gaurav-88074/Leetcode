class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        c = 0
        for i in nums:
            if i==0:
                c+=1
                res+=c
            else:
                c=0
        return res