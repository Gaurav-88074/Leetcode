class Solution(object):
    def findNonMinOrMax(self, nums):

        if len(nums)<=2:
            return -1
        nums.sort()
        return nums[1]
        
        # mn = float('inf')
        # mx = float('-inf')
        # for i in nums:
        #     mn = min(mn,i)
        #     mx = max(mx,i)
        # nums.remove(mn)
        # nums.remove(mx)
        # return nums[0]
        