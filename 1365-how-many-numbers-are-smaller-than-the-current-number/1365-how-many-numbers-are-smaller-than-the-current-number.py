class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            nums[i] = [
                i,nums[i]
            ]
        nums.sort(key = lambda x : x[1])
        res = [0]*len(nums)
        
        # print(nums)
        i = 0
        pre = -1
        for index,v in nums:
            ac = i
            while i>0 and nums[i-1][1]==nums[i][1] : i-=1
            res[index] = i
            i = ac
            i+=1
        return res
            