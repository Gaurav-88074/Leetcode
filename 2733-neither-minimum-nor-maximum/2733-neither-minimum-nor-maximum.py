class Solution(object):
    def findNonMinOrMax(self, nums):
#         minimum = maximum = nums[0]

#         for num in nums[1:]:
#             minimum = min(minimum, num)
#             maximum = max(maximum, num)

#         for num in nums:
#             if num != minimum and num != maximum:
#                 return num

#         return -1
        if len(nums)<=2:
            return -1
        # nums.sort()
        # return nums[1]
        
        mn = float('inf')
        mx = float('-inf')
        for i in nums:
            mn = min(mn,i)
            mx = max(mx,i)
        nums.remove(mn)
        nums.remove(mx)
        return nums[0]
        